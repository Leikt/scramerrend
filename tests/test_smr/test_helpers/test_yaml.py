import os
import unittest

from smr import load_yaml, save_yaml, UnknownExtensionError


class TestHelpers(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        try:
            os.remove("test_smr/test_helpers/data/test_save.yml")
        except FileNotFoundError:
            pass

    def test_load(self):
        data = load_yaml("test_smr/test_helpers/data/test.yml")
        self.assertEqual("AAA", data["value"])

    def test_save(self):
        data = {
            "value": "AAA"
        }
        self.assertTrue(save_yaml("test_smr/test_helpers/data/test_save.yml", data))

    def test_extension_error_on_load(self):
        with self.assertRaises(UnknownExtensionError):
            load_yaml("somefile.ext")

    def test_extension_error_on_save(self):
        with self.assertRaises(UnknownExtensionError):
            save_yaml("somefile.ext", {})
