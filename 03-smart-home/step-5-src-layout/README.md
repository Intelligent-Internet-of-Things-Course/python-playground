# Smart Home IoT — `src/` layout example

A small, self-contained IoT domain model — sensors, actuators, a data store, an
automation rule, and a command-line runner — organised as a realistic Python
project: a `src/` package split into folders **by responsibility**, driven by a
YAML config file, using `logging` and type hints throughout.

It is a teaching example for how to *structure* a Python project once it grows
past a single script.

---

## Requirements

- Python **3.10+** (the code uses `X | None` type-hint syntax).
- One third-party package, `PyYAML`, listed in [`requirements.txt`](requirements.txt).

## Setup

Use a **virtual environment** so the dependency is installed for this project
only, not system-wide.

**Linux / macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**Windows — PowerShell**

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

**Windows — cmd.exe**

```bat
py -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
```

`requirements.txt` is the reproducible recipe; `.venv/` is disposable — delete
and recreate it any time from the recipe. Never commit `.venv/`. Run
`deactivate` to leave the environment.

## Run

From this directory:

```bash
python3 run.py                                   # default config
python3 run.py --config config/settings.yaml --verbose
```

`run.py` is a tiny shim that puts `src/` on the import path and calls the CLI.
The equivalent module forms (same result):

```bash
PYTHONPATH=src python3 -m smart_home
PYTHONPATH=src python3 -m smart_home.interface.cli --verbose
```

Expected output (values are randomised each run):

```
2026-... [INFO] smart_home: loaded config from .../config/settings.yaml
2026-... [INFO] smart_home.logic.automation_rules: 22.9 <= 26.0 -> light bulb_1 OFF
2026-... [INFO] smart_home: sensor_1 -> 22.86
2026-... [INFO] smart_home: sensor_2 -> 60.00
2026-... [INFO] smart_home: bulb_1 -> OFF
```

---

## Project layout

```
.
├── README.md
├── requirements.txt          # the one dependency (PyYAML)
├── run.py                    # convenience entry point (no install needed)
├── config/
│   └── settings.yaml         # home id, location, automation threshold
└── src/
    └── smart_home/
        ├── __init__.py
        ├── __main__.py       # enables `python -m smart_home`
        ├── home.py           # SmartHome — the top-level entity
        ├── devices/          # what a device IS
        │   ├── base.py       #   Device
        │   ├── sensors.py    #   Sensor, TemperatureSensor, HumiditySensor
        │   └── actuators.py  #   Actuator, SmartLight
        ├── storage/          # how device data is kept and retrieved
        │   └── data_manager.py
        ├── logic/            # what the system DECIDES to do
        │   └── automation_rules.py
        └── interface/        # how the outside world talks to it
            └── cli.py        #   argparse + logging + config loading
```

### Why `src/`

Putting the package one level down, inside `src/`, means it can only be imported
once it is actually on the path (via an editable install, or the `run.py` /
`PYTHONPATH` shims used here) — not by accident just because you happen to be
standing in the project root. That makes local runs behave the same way an
installed copy would.

### Why the responsibility folders

Each subpackage answers one question about the code in it:

| Folder | Question | Depends on |
|---|---|---|
| `devices/` | what a device *is* | nothing else here |
| `storage/` | how device data is *kept* | `devices/` |
| `logic/` | what the system *does* with the data | `devices/` |
| `interface/` | how a human/other system *drives* it | all of the above |

Swapping in-memory storage for a database would only touch `storage/`. Replacing
the CLI with an HTTP API would only touch `interface/`. This is the same
separation-of-concerns idea as the `SmartHome` → `DataManager` delegation, scaled
up to the whole project.

---

## Concepts demonstrated

- **`src/` project layout** and packages split by responsibility.
- **Modules & packages**: `__init__.py` files, absolute imports
  (`from smart_home.storage import DataManager`), `__main__.py` for `python -m`.
- **Configuration in a file**, not hardcoded: `config/settings.yaml`, loaded with
  `yaml.safe_load()`.
- **`argparse`** for command-line options (`--config`, `--verbose`).
- **`logging`** with levels and a configurable threshold, instead of `print()`.
- **Type hints** on every function and method.
- **Delegation / separation of concerns**: `SmartHome` owns nothing about
  storage; `DataManager` owns nothing about automation; `logic/` owns nothing
  about I/O.
