# Deprecated: validation.py moved to src/utils/validation.py
# This stub keeps backward compatibility for a short transition period.
import warnings
from src.utils.validation import validate_timeseries  # re-export

warnings.warn(
    "validation.py at the repository root is deprecated and will be removed. "
    "Please import from src.utils.validation instead.",
    DeprecationWarning,
    stacklevel=2,
)
