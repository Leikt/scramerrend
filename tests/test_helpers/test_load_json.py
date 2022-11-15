import os
import unittest

from smr import load_json, save_json


class TestHelpers(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        try:
            os.remove("test_helpers/data/test_save.json")
        except FileNotFoundError:
            pass

    def test_load_json(self):
        data = load_json("test_helpers/data/test.json")
        self.assertEqual("AAA", data["value"])

    def test_save_json(self):
        data = {
            "value": "AAA"
        }
        self.assertTrue(save_json("test_helpers/data/test_save.json", data))
