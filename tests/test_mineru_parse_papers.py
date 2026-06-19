import importlib.util
import json
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from zipfile import ZipFile


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "mineru_parse_papers.py"


def load_module():
    spec = importlib.util.spec_from_file_location("mineru_parse_papers", MODULE_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules["mineru_parse_papers"] = module
    spec.loader.exec_module(module)
    return module


class MineruParsePapersTest(unittest.TestCase):
    def test_data_id_removes_spaces_and_non_word_separators(self):
        mineru = load_module()

        self.assertEqual(
            mineru.make_data_id(Path("Axtell_2013_Annual Review of Plant Biology.pdf")),
            "Axtell_2013_Annual_Review_of_Plant_Biology",
        )

    def test_already_parsed_requires_done_meta_and_full_md(self):
        mineru = load_module()
        with TemporaryDirectory() as temp_dir:
            tmp_path = Path(temp_dir)
            pdf = tmp_path / "paper one.pdf"
            pdf.write_bytes(b"%PDF")
            output_dir = tmp_path / "mineru-parsed"
            parsed_dir = output_dir / "paper one"
            parsed_dir.mkdir(parents=True)
            (parsed_dir / "full.md").write_text("# parsed\n", encoding="utf-8")
            (parsed_dir / "meta.json").write_text(json.dumps({"state": "done"}), encoding="utf-8")

            self.assertTrue(mineru.is_already_parsed(pdf, output_dir))

            (parsed_dir / "meta.json").write_text(json.dumps({"state": "failed"}), encoding="utf-8")
            self.assertFalse(mineru.is_already_parsed(pdf, output_dir))

    def test_chunks_enforce_batch_size(self):
        mineru = load_module()
        items = list(range(101))

        chunked = list(mineru.chunks(items, 50))

        self.assertEqual([len(chunk) for chunk in chunked], [50, 50, 1])

    def test_store_success_extracts_expected_files_and_writes_meta(self):
        mineru = load_module()
        with TemporaryDirectory() as temp_dir:
            tmp_path = Path(temp_dir)
            pdf = tmp_path / "Paper Name.pdf"
            pdf.write_bytes(b"%PDF fake")
            output_dir = tmp_path / "mineru-parsed"
            zip_path = tmp_path / "result.zip"
            with ZipFile(zip_path, "w") as archive:
                archive.writestr("nested/full.md", "# Full text\n")
                archive.writestr("nested/content_list.json", "[]\n")
                archive.writestr("nested/extra.html", "<html></html>")

            result = {
                "data_id": "Paper_Name",
                "file_name": "Paper Name.pdf",
                "state": "done",
                "full_zip_url": "https://example.invalid/result.zip",
            }

            record = mineru.store_success(
                pdf_path=pdf,
                output_root=output_dir,
                batch_id="batch-1",
                result=result,
                downloaded_zip=zip_path,
                model_version="vlm",
                language="en",
            )

            parsed_dir = output_dir / "Paper Name"
            self.assertTrue((parsed_dir / "source.pdf").is_file())
            self.assertTrue((parsed_dir / "result.zip").is_file())
            self.assertEqual((parsed_dir / "full.md").read_text(encoding="utf-8"), "# Full text\n")
            self.assertEqual((parsed_dir / "content_list.json").read_text(encoding="utf-8"), "[]\n")
            meta = json.loads((parsed_dir / "meta.json").read_text(encoding="utf-8"))
            self.assertEqual(meta["original_pdf"], str(pdf))
            self.assertEqual(meta["data_id"], "Paper_Name")
            self.assertEqual(meta["batch_id"], "batch-1")
            self.assertEqual(meta["state"], "done")
            self.assertEqual(meta["model_version"], "vlm")
            self.assertEqual(meta["language"], "en")
            self.assertNotIn("token", json.dumps(meta).lower())
            self.assertEqual(record.full_md_path, str(parsed_dir / "full.md"))
            self.assertEqual(record.content_list_path, str(parsed_dir / "content_list.json"))


if __name__ == "__main__":
    unittest.main()
