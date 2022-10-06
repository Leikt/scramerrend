import unittest

from smr.core import PWorkflow, Workflow
from test_core.mocks.module_dummy import factory, SmrModule


class TestWorkflow(unittest.TestCase):
    def test_simple(self):
        workflow: PWorkflow = Workflow([factory() for _ in range(5)])
        self.assertIsInstance(workflow, Workflow)
        self.assertTrue(hasattr(workflow, '_smr_modules'))
        self.assertTrue(hasattr(workflow, 'execute'))
        self.assertEqual(5, len(workflow._smr_modules))
        [self.assertIsInstance(m, SmrModule) for m in workflow._smr_modules]

    def test_builder(self):
        builder = Workflow.Builder()
        self.assertIsInstance(builder, Workflow.Builder)
        self.assertEqual(0, len(builder._smr_modules))
        builder.add(factory())
        self.assertEqual(1, len(builder._smr_modules))
        workflow = builder.build()
        self.assertIsInstance(workflow, Workflow)
