## `01-best-practices/` — habits for *any* Python code

Goal: the practices that make a script robust and maintainable, whether or not
it uses classes.

| Step | Demonstrates |
|---|---|
| [`01-main-guard/`](01-main-guard/) | `if __name__ == "__main__"` — run vs import, the `main()` pattern |
| [`02-exceptions/`](02-exceptions/) | `try` / `except` / `else` / `finally`, several handlers, a custom `Exception` |
| [`03-type-hints/`](03-type-hints/) | three type bugs that crash far from their cause, then hints as documentation + `isinstance()` as the real check |
| [`04-config/`](04-config/) | moving values out of the code: `argparse`, environment variables, JSON / YAML config files |
| [`05-logging/`](05-logging/) | `logging` instead of `print()`: severity levels, threshold filtering, output to a file |

Each step is self-contained and runnable on its own — `python3 main.py` (or the
file named in that step's module docstring).
