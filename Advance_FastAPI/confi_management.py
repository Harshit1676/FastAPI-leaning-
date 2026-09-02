"""Backward-compatible alias for :mod:`config_management`.

Use ``config_management`` in new code; this module keeps existing imports
that use the older ``confi_management`` spelling working.
"""

from Advance_FastAPI.config_management import *  # noqa: F403
