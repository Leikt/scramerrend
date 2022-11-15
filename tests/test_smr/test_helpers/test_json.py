import os
import unittest

from smr import load_json, save_json, UnknownExtensionError


class TestHelpers(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        try:
            os.remove("test_smr/test_helpers/data/test_save.json")
        except FileNotFoundError:
            pass

    def test_load(self):
        data = load_json("test_smr/test_helpers/data/test.json")
        self.assertEqual("AAA", data["value"])

    def test_save(self):
        data = {
            "value": "AAA"
        }
        self.assertTrue(save_json("test_smr/test_helpers/data/test_save.json", data))

    def test_extension_error_on_load(self):
        with self.assertRaises(UnknownExtensionError):
            load_json("somefile.ext")

    def test_extension_error_on_save(self):
        with self.assertRaises(UnknownExtensionError):
            save_json("somefile.ext", {})