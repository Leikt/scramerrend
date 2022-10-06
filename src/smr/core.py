"""Core module for Scramerrend."""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Protocol


class PSmrModule(Protocol):
    """A module usable in the SMR architecture."""

    def execute(self) -> None:
        """Execute the module with its parameters."""


class PWorkflow(PSmrModule):
    """Create a workflow of modules. A workflow is a SMR modules itself. It can be composed with other workflows."""


@dataclass
class Workflow(PWorkflow):
    """A basic workflow module."""

    _smr_modules: list[PSmrModule] = field(default_factory=list)

    def execute(self) -> None:
        """Execute all its modules in order."""
        for m in self._smr_modules:
            m.execute()

    class Builder:
        """A builder for the Workflow class"""
        def __init__(self):
            self._smr_modules = []

        def build(self) -> PWorkflow:
            """Create the workflow."""
            return Workflow(_smr_modules=self._smr_modules)

        def add(self, smr_module: PSmrModule) -> Workflow.Builder:
            """Add the smr module to the workflow. It will be executed in the add order."""
            self._smr_modules.append(smr_module)
            return self
