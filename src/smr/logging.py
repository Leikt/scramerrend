"""Logging wrapper for Scramerrend."""

import logging


class SmrLogger(logging.Logger):
    """Logger with possibility to be enabled or disabled."""

    def __init__(self, *args, **kwargs):
        self._enabled: bool = True
        super().__init__(*args, **kwargs)

    def enable(self):
        """Activate the logging."""
        self._enabled = True

    def disable(self):
        """Deactivate the logging. Nothing will be logged whatsoever."""
        self._enabled = False

    def _log(self, *args, **kwargs) -> None:
        if self._enabled:
            super()._log(*args, **kwargs)
