"""
Best practices hands-on - Step 04c: configuration files (JSON and YAML).

Run:
  python3 config_file.py json     -> uses config.json  (stdlib only)
  python3 config_file.py yaml     -> uses config.yaml  (needs PyYAML)

JSON: strict, no comments, no dependency.
YAML: readable, supports comments, needs `pip install pyyaml`.
Always use yaml.safe_load(), never yaml.load().
"""

import json
import sys
from pathlib import Path

HERE = Path(__file__).parent

def load_json():
    with open(HERE / "config.json") as f:
        return json.load(f)

def load_yaml():
    try:
        import yaml
    except ModuleNotFoundError:
        sys.exit("PyYAML is not installed. Run:  pip install pyyaml")
    with open(HERE / "config.yaml") as f:
        return yaml.safe_load(f)

def main():
    fmt = sys.argv[1] if len(sys.argv) > 1 else "json"
    config = load_yaml() if fmt == "yaml" else load_json()
    print(f"loaded {fmt} config: {config}")
    print("device_id           =", config["device_id"])
    print("sample_rate_seconds =", config["sample_rate_seconds"])

if __name__ == "__main__":
    main()
