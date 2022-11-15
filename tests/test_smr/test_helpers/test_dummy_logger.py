import unittest

from smr import get_dummy_logger


class TestDummyLogger(unittest.TestCase):
    def test_dummy_logger(self):
        logger = get_dummy_logger()
        self.assertTrue(logger.disabled)
        try:
            with self.assertLogs(logger):
                logger.info('Should not be logged')
        except AssertionError:
            pass
        else:
            raise AssertionError('logs are presents.')