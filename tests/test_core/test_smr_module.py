import unittest

from smr.core import PSmrModule
from test_core.mocks import module_dummy


class TestSmrModule(unittest.TestCase):
    def test_protocol(self):
        smr_module: PSmrModule = module_dummy.SmrModule()
        self.assertIsInstance(smr_module, module_dummy.SmrModule)
        self.assertTrue(hasattr(smr_module, 'execute'))

    def test_factory(self):
        smr_module: PSmrModule = module_dummy.factory()
        self.assertIsInstance(smr_module, module_dummy.SmrModule)
        self.assertTrue(hasattr(smr_module, 'execute'))
