"""
Entry point for running the Smart Home demo without installing it.

Run:  python3 run.py            # or:  python3 run.py --verbose

The package lives under src/ (the "src/ layout", python_best_practices.md 9).
The clean way to make it importable is an editable install
(`pip install -e .` with a pyproject.toml) — this repo deliberately stays on
requirements.txt only, so this tiny shim puts src/ on the import path instead
and then hands control to the real CLI.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

from smart_home.interface.cli import main

if __name__ == "__main__":
    main()
