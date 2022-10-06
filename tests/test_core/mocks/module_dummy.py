from smr.core import PSmrModule


class SmrModule:
    """A mock SmrModule that does nothing."""
    def execute(self):
        pass


def factory() -> PSmrModule:
    """A mock factory to create a mock.SmrModule"""
    return SmrModule()
