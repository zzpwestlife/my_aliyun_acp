import base64
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "export_notebooks.py"


def load_module():
    spec = importlib.util.spec_from_file_location("export_notebooks", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def write_notebook(path: Path, cells):
    notebook = {
        "cells": cells,
        "metadata": {
            "language_info": {"name": "python"},
            "kernelspec": {"display_name": "Python 3", "name": "python3"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(notebook, ensure_ascii=False), encoding="utf-8")


class ExportNotebooksTests(unittest.TestCase):
    def test_discover_notebooks_sorts_by_relative_path(self):
        module = load_module()
        with tempfile.TemporaryDirectory() as tmp_dir:
            source_root = Path(tmp_dir) / "source"
            output_root = source_root / "markdown_export"
            write_notebook(source_root / "b" / "2.ipynb", [])
            write_notebook(source_root / "a" / "10.ipynb", [])
            write_notebook(output_root / "ignored.ipynb", [])

            notebooks = module.discover_notebooks(source_root, output_root)

            rel_paths = [path.relative_to(source_root).as_posix() for path in notebooks]
            self.assertEqual(rel_paths, ["a/10.ipynb", "b/2.ipynb"])

    def test_export_tree_rewrites_links_copies_assets_and_exports_outputs(self):
        module = load_module()
        tiny_png = (
            "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8"
            "/w8AAgMBAp0X2uoAAAAASUVORK5CYII="
        )
        with tempfile.TemporaryDirectory() as tmp_dir:
            root = Path(tmp_dir) / "course"
            output_root = root / "markdown_export"
            write_notebook(
                root / "C1" / "lesson.ipynb",
                [
                    {
                        "cell_type": "markdown",
                        "metadata": {},
                        "source": (
                            "查看[补充资料](guide.md)\n\n"
                            "继续阅读[下一课](../C2/next.ipynb)\n\n"
                            "<img src=\"diagram.png\">"
                        ),
                    },
                    {
                        "cell_type": "code",
                        "execution_count": 1,
                        "metadata": {},
                        "source": "print('hello')",
                        "outputs": [
                            {"name": "stdout", "output_type": "stream", "text": "hello\n"},
                            {
                                "output_type": "display_data",
                                "data": {"image/png": tiny_png},
                                "metadata": {},
                            },
                        ],
                    },
                ],
            )
            write_notebook(root / "C2" / "next.ipynb", [])
            (root / "assets" / "guide.md").parent.mkdir(parents=True, exist_ok=True)
            (root / "assets" / "guide.md").write_text("# guide", encoding="utf-8")
            (root / "C1" / "diagram.png").write_bytes(base64.b64decode(tiny_png))

            report = module.export_notebook_tree(root, output_root)

            target_md = output_root / "C1" / "lesson.md"
            self.assertTrue(target_md.exists())
            content = target_md.read_text(encoding="utf-8")
            self.assertIn("[补充资料](../assets/guide.md)", content)
            self.assertIn("[下一课](../C2/next.md)", content)
            self.assertIn('<img src="diagram.png">', content)
            self.assertIn("```python\nprint('hello')\n```", content)
            self.assertIn("```text\nhello\n```", content)
            self.assertRegex(content, r"!\[png\]\(lesson_files/output_2_2\.png\)")
            self.assertTrue((output_root / "assets" / "guide.md").exists())
            self.assertTrue((output_root / "C1" / "diagram.png").exists())
            self.assertEqual(report["notebook_count"], 2)


if __name__ == "__main__":
    unittest.main()
