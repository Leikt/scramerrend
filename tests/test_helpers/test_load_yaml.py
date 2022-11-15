import os
import unittest

from smr import load_yaml, save_yaml


class TestHelpers(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        try:
            os.remove("test_helpers/data/test_save.yml")
        except FileNotFoundError:
            pass

    def test_load_yaml(self):
        data = load_yaml("test_helpers/data/test.yml")
        self.assertEqual("AAA", data["value"])

    def test_save_yaml(self):
        data = {
            "value": "AAA"
        }
        self.assertTrue(save_yaml("test_helpers/data/test_save.yml", data))
