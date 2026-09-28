"""Makes `python3 -m smart_home` work.

Running a package with -m executes this file with __name__ == "__main__"
(python_best_practices.md 2.3 / 10.3).
"""

from smart_home.interface.cli import main

if __name__ == "__main__":
    main()
