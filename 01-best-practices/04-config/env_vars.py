"""
Best practices hands-on - Step 04b: environment variables.

Try it from the shell to see inheritance in action:
  export API_KEY=abc123
  python3 env_vars.py            -> reads abc123 from the environment
  python3 env_vars.py            (in a new shell, without export) -> falls back

os.environ does NOT create this data - it reads the OS-level environment the
process was started with.
"""

import os

def main():
    # In real deployments API_KEY is set OUTSIDE Python (shell `export`, or the
    # platform). Set here only if absent, so the example is self-contained.
    os.environ.setdefault("API_KEY", "demo-key-12345")

    api_key = os.getenv("API_KEY")
    missing = os.getenv("NOT_SET", "default-value")     # default when unset

    print("API_KEY   =", api_key)
    print("NOT_SET   =", missing)

    # For local dev, a .env file + python-dotenv is common:
    #   from dotenv import load_dotenv; load_dotenv()
    # (.env must never be committed - it is already in .gitignore)

if __name__ == "__main__":
    main()
