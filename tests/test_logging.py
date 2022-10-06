import logging
import unittest

from smr.logging import SmrLogger


class TestLogging(unittest.TestCase):
    def setUp(self) -> None:
        self.logger = SmrLogger(name="test_logger", level=logging.DEBUG)

    def test_default(self):
        with self.assertLogs(self.logger, logging.DEBUG):
            self.logger.debug("Test")

    def test_disable(self):
        self.logger.disable()
        try:
            with self.assertLogs(self.logger, logging.DEBUG):
                self.logger.debug("Test")
            raise Exception("Logs were generated")
        except AssertionError as ex:
            self.assertTrue(True)

    def test_enable(self):
        self.logger.disable()
        try:
            with self.assertLogs(self.logger, logging.DEBUG):
                self.logger.debug("Test")
            raise Exception("Logs were generated")
        except AssertionError as ex:
            self.assertTrue(True)
        self.logger.enable()
        with self.assertLogs(self.logger, logging.DEBUG):
            self.logger.debug("Test")