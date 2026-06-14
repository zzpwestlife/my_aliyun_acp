#!/usr/bin/env python3

import argparse
import base64
import json
import re
import shutil
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from urllib.parse import urlsplit


MARKDOWN_LINK_RE = re.compile(r"(!?\[[^\]]*\]\()([^)]+)(\))")
HTML_ATTR_RE = re.compile(r'((?:src|href)\s*=\s*["\'])([^"\']+)(["\'])', re.IGNORECASE)
CODE_FENCE_RE = re.compile(r"(```[\s\S]*?```)")
SKIP_SCHEMES = ("http://", "https://", "mailto:", "data:", "#")
IMAGE_MIME_ORDER = [
    ("image/png", "png"),
    ("image/jpeg", "jpg"),
    ("image/gif", "gif"),
    ("image/svg+xml", "svg"),
]


def read_notebook(notebook_path: Path) -> Dict:
    return json.loads(notebook_path.read_text(encoding="utf-8"))


def discover_notebooks(source_root: Path, output_root: Path) -> List[Path]:
    notebooks = []
    for path in source_root.rglob("*.ipynb"):
        if output_root == path or output_root in path.parents:
            continue
        notebooks.append(path)
    return sorted(notebooks, key=lambda item: item.relative_to(source_root).as_posix())


def build_basename_index(source_root: Path, output_root: Path) -> Dict[str, List[Path]]:
    index: Dict[str, List[Path]] = {}
    for path in source_root.rglob("*"):
        if path.is_dir():
            continue
        if output_root == path or output_root in path.parents:
            continue
        index.setdefault(path.name, []).append(path)
    return index


def ensure_text(value) -> str:
    if isinstance(value, list):
        return "".join(str(item) for item in value)
    return str(value or "")


def is_external_reference(reference: str) -> bool:
    if not reference:
        return True
    if reference.startswith(SKIP_SCHEMES):
        return True
    return bool(urlsplit(reference).scheme)


def split_reference(reference: str) -> Tuple[str, str]:
    for marker in ("#", "?"):
        index = reference.find(marker)
        if index != -1:
            return reference[:index], reference[index:]
    return reference, ""


def safe_relative_to(path: Path, root: Path) -> Optional[Path]:
    try:
        return path.relative_to(root)
    except ValueError:
        return None


def resolve_candidate(
    raw_reference: str,
    current_source_dir: Path,
    source_root: Path,
    basename_index: Dict[str, List[Path]],
) -> Optional[Path]:
    candidate = (current_source_dir / raw_reference).resolve()
    rel = safe_relative_to(candidate, source_root)
    if rel is not None and candidate.exists():
        return candidate

    basename = Path(raw_reference).name
    matches = basename_index.get(basename, [])
    if len(matches) == 1:
        return matches[0]
    return None


def relative_href(target_path: Path, current_target_dir: Path, suffix: str = "") -> str:
    return target_path.relative_to(current_target_dir) if False else f"{Path(shutil.os.path.relpath(target_path, current_target_dir)).as_posix()}{suffix}"


def copy_asset(source_path: Path, target_path: Path) -> None:
    target_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source_path, target_path)


def write_placeholder_markdown(target_path: Path, original_reference: str) -> None:
    if target_path.exists():
        return
    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(
        "\n".join(
            [
                "# 资源占位说明",
                "",
                "当前课程目录中未提供该链接指向的源 Notebook 文件。",
                "",
                f"- 原始引用：`{original_reference}`",
                "- 处理方式：为保持链接可访问性，导出时生成此占位页面。",
            ]
        )
        + "\n",
        encoding="utf-8",
    )


def rewrite_reference(
    reference: str,
    current_source_dir: Path,
    current_target_dir: Path,
    source_root: Path,
    output_root: Path,
    basename_index: Dict[str, List[Path]],
    copied_assets: set,
    unresolved_references: List[Dict[str, str]],
) -> str:
    if is_external_reference(reference):
        return reference

    path_part, suffix = split_reference(reference)
    if not path_part:
        return reference

    candidate = resolve_candidate(path_part, current_source_dir, source_root, basename_index)
    if candidate is None:
        if path_part.endswith(".ipynb"):
            placeholder_path = (current_target_dir / path_part).with_suffix(".md").resolve()
            if safe_relative_to(placeholder_path, output_root) is not None:
                write_placeholder_markdown(placeholder_path, reference)
                return f"{Path(shutil.os.path.relpath(placeholder_path, current_target_dir)).as_posix()}{suffix}"
        unresolved_references.append({"reference": reference, "source_dir": current_source_dir.as_posix()})
        return reference

    source_rel = candidate.relative_to(source_root)
    if candidate.suffix == ".ipynb":
        target_path = output_root / source_rel.with_suffix(".md")
        return f"{Path(shutil.os.path.relpath(target_path, current_target_dir)).as_posix()}{suffix}"

    target_path = output_root / source_rel
    copied_key = target_path.as_posix()
    if copied_key not in copied_assets:
        copy_asset(candidate, target_path)
        copied_assets.add(copied_key)
    return f"{Path(shutil.os.path.relpath(target_path, current_target_dir)).as_posix()}{suffix}"


def rewrite_html_references(
    text: str,
    current_source_dir: Path,
    current_target_dir: Path,
    source_root: Path,
    output_root: Path,
    basename_index: Dict[str, List[Path]],
    copied_assets: set,
    unresolved_references: List[Dict[str, str]],
) -> str:
    def replace(match):
        rewritten = rewrite_reference(
            match.group(2),
            current_source_dir,
            current_target_dir,
            source_root,
            output_root,
            basename_index,
            copied_assets,
            unresolved_references,
        )
        return f"{match.group(1)}{rewritten}{match.group(3)}"

    return HTML_ATTR_RE.sub(replace, text)


def rewrite_markdown_segment(
    text: str,
    current_source_dir: Path,
    current_target_dir: Path,
    source_root: Path,
    output_root: Path,
    basename_index: Dict[str, List[Path]],
    copied_assets: set,
    unresolved_references: List[Dict[str, str]],
) -> str:
    def replace(match):
        rewritten = rewrite_reference(
            match.group(2),
            current_source_dir,
            current_target_dir,
            source_root,
            output_root,
            basename_index,
            copied_assets,
            unresolved_references,
        )
        return f"{match.group(1)}{rewritten}{match.group(3)}"

    text = MARKDOWN_LINK_RE.sub(replace, text)
    return rewrite_html_references(
        text,
        current_source_dir,
        current_target_dir,
        source_root,
        output_root,
        basename_index,
        copied_assets,
        unresolved_references,
    )


def rewrite_markdown_text(
    text: str,
    current_source_dir: Path,
    current_target_dir: Path,
    source_root: Path,
    output_root: Path,
    basename_index: Dict[str, List[Path]],
    copied_assets: set,
    unresolved_references: List[Dict[str, str]],
) -> str:
    parts = CODE_FENCE_RE.split(text)
    rewritten_parts = []
    for index, part in enumerate(parts):
        if index % 2 == 1:
            rewritten_parts.append(part)
            continue
        rewritten_parts.append(
            rewrite_markdown_segment(
                part,
                current_source_dir,
                current_target_dir,
                source_root,
                output_root,
                basename_index,
                copied_assets,
                unresolved_references,
            )
        )
    return "".join(rewritten_parts)


def format_fenced_block(language: str, text: str) -> str:
    payload = text.rstrip("\n")
    return f"```{language}\n{payload}\n```"


def save_output_image(
    data: Dict,
    resources_dir: Path,
    cell_index: int,
    output_index: int,
) -> Optional[str]:
    for mime_type, extension in IMAGE_MIME_ORDER:
        if mime_type not in data:
            continue
        resources_dir.mkdir(parents=True, exist_ok=True)
        file_name = f"output_{cell_index}_{output_index}.{extension}"
        file_path = resources_dir / file_name
        payload = ensure_text(data[mime_type])
        if extension == "svg":
            file_path.write_text(payload, encoding="utf-8")
        else:
            file_path.write_bytes(base64.b64decode(payload))
        return file_name
    return None


def render_output(
    output: Dict,
    cell_index: int,
    output_index: int,
    resources_dir: Path,
    resources_ref_prefix: str,
    current_source_dir: Path,
    current_target_dir: Path,
    source_root: Path,
    output_root: Path,
    basename_index: Dict[str, List[Path]],
    copied_assets: set,
    unresolved_references: List[Dict[str, str]],
) -> List[str]:
    output_type = output.get("output_type")
    blocks: List[str] = []

    if output_type == "stream":
        blocks.append(format_fenced_block("text", ensure_text(output.get("text", ""))))
        return blocks

    if output_type == "error":
        traceback = ensure_text(output.get("traceback", []))
        blocks.append(format_fenced_block("text", traceback))
        return blocks

    data = output.get("data", {})
    image_file = save_output_image(data, resources_dir, cell_index, output_index)
    if image_file:
        blocks.append(f"![png]({resources_ref_prefix}/{image_file})")

    if "text/markdown" in data:
        blocks.append(
            rewrite_markdown_text(
                ensure_text(data["text/markdown"]),
                current_source_dir,
                current_target_dir,
                source_root,
                output_root,
                basename_index,
                copied_assets,
                unresolved_references,
            ).rstrip("\n")
        )
    elif "text/html" in data:
        blocks.append(
            rewrite_html_references(
                ensure_text(data["text/html"]),
                current_source_dir,
                current_target_dir,
                source_root,
                output_root,
                basename_index,
                copied_assets,
                unresolved_references,
            ).rstrip("\n")
        )
    elif "text/plain" in data:
        blocks.append(format_fenced_block("text", ensure_text(data["text/plain"])))

    return [block for block in blocks if block]


def render_notebook(
    notebook_path: Path,
    target_md_path: Path,
    source_root: Path,
    output_root: Path,
    basename_index: Dict[str, List[Path]],
    copied_assets: set,
) -> Tuple[str, List[Dict[str, str]]]:
    notebook = read_notebook(notebook_path)
    current_source_dir = notebook_path.parent
    current_target_dir = target_md_path.parent
    language = notebook.get("metadata", {}).get("language_info", {}).get("name", "python")
    resources_dir = target_md_path.parent / f"{target_md_path.stem}_files"
    resources_ref_prefix = resources_dir.name
    unresolved_references: List[Dict[str, str]] = []
    chunks: List[str] = []

    for cell_index, cell in enumerate(notebook.get("cells", []), start=1):
        cell_type = cell.get("cell_type")
        source = ensure_text(cell.get("source", ""))

        if cell_type == "markdown":
            rendered = rewrite_markdown_text(
                source,
                current_source_dir,
                current_target_dir,
                source_root,
                output_root,
                basename_index,
                copied_assets,
                unresolved_references,
            ).rstrip("\n")
            if rendered:
                chunks.append(rendered)
            continue

        if cell_type == "raw":
            rendered = source.rstrip("\n")
            if rendered:
                chunks.append(rendered)
            continue

        if cell_type == "code":
            chunks.append(format_fenced_block(language, source))
            for output_index, output in enumerate(cell.get("outputs", []), start=1):
                chunks.extend(
                    render_output(
                        output,
                        cell_index,
                        output_index,
                        resources_dir,
                        resources_ref_prefix,
                        current_source_dir,
                        current_target_dir,
                        source_root,
                        output_root,
                        basename_index,
                        copied_assets,
                        unresolved_references,
                    )
                )

    markdown = "\n\n".join(chunk for chunk in chunks if chunk).rstrip() + "\n"
    return markdown, unresolved_references


def scan_relative_references(markdown_text: str) -> List[str]:
    markdown_text = CODE_FENCE_RE.sub("", markdown_text)
    references = []
    for match in MARKDOWN_LINK_RE.finditer(markdown_text):
        references.append(match.group(2))
    for match in HTML_ATTR_RE.finditer(markdown_text):
        references.append(match.group(2))
    return references


def verify_markdown_references(markdown_path: Path, markdown_text: str) -> List[str]:
    broken = []
    for reference in scan_relative_references(markdown_text):
        if is_external_reference(reference):
            continue
        path_part, _ = split_reference(reference)
        target = (markdown_path.parent / path_part).resolve()
        if not target.exists():
            broken.append(reference)
    return broken


def export_notebook_tree(source_root: Path, output_root: Path) -> Dict:
    output_root.mkdir(parents=True, exist_ok=True)
    notebooks = discover_notebooks(source_root, output_root)
    basename_index = build_basename_index(source_root, output_root)
    copied_assets: set = set()
    report = {
        "source_root": source_root.as_posix(),
        "output_root": output_root.as_posix(),
        "notebook_count": len(notebooks),
        "markdown_count": 0,
        "files": [],
        "unresolved_reference_count": 0,
        "broken_reference_count": 0,
    }

    for notebook_path in notebooks:
        target_md_path = output_root / notebook_path.relative_to(source_root).with_suffix(".md")
        target_md_path.parent.mkdir(parents=True, exist_ok=True)
        markdown, unresolved_references = render_notebook(
            notebook_path,
            target_md_path,
            source_root,
            output_root,
            basename_index,
            copied_assets,
        )
        target_md_path.write_text(markdown, encoding="utf-8")
        broken_references = verify_markdown_references(target_md_path, markdown)
        report["markdown_count"] += 1
        report["unresolved_reference_count"] += len(unresolved_references)
        report["broken_reference_count"] += len(broken_references)
        report["files"].append(
            {
                "source": notebook_path.relative_to(source_root).as_posix(),
                "target": target_md_path.relative_to(output_root).as_posix(),
                "unresolved_references": unresolved_references,
                "broken_references": broken_references,
            }
        )

    report_path = output_root / "export_report.json"
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    return report


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Export notebooks to markdown with mirrored paths.")
    parser.add_argument("--source-root", required=True, help="Notebook source root directory.")
    parser.add_argument("--output-root", required=True, help="Markdown output root directory.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    source_root = Path(args.source_root).resolve()
    output_root = Path(args.output_root).resolve()
    report = export_notebook_tree(source_root, output_root)
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
