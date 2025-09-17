"""Core shared logic used by both the Django app and the standalone CLI.

This module also exposes a simple debug logging hook `debug_log` that core
functions use instead of printing directly. Clients/tests can override it
via `set_debug_logger` to silence or redirect messages.
"""

from typing import Callable, Optional


def _default_debug_logger(message: str) -> None:  # default behavior: print
	print(message)


# Public hook used by bfcore modules
debug_log: Callable[[str], None] = _default_debug_logger


def set_debug_logger(logger: Optional[Callable[[str], None]]) -> None:
	"""Set a custom debug logger function or disable logging if None.

	Example to silence:
		from bfcore import set_debug_logger
		set_debug_logger(None)
	"""
	global debug_log
	if logger is None:
		debug_log = lambda _msg: None
	else:
		debug_log = logger
