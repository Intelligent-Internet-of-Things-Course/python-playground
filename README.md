<!-- omit in toc -->
# Python Playground — Python Best Practices, OOP & Use Case Modelling

<!-- omit in toc -->
## Lecture Information

| **Master's Degree** | Intelligent Internet of Things (D.M.270/04)                                      |
|---------------------|----------------------------------------------------------------------------------|
| **Course**          | Intelligent Internet of Things                                                   |
| **Lecture Title**   | Python Playground — Python Best Practices, OOP & Use Case Modelling              |
| **Author**          | Prof. Marco Picone (marco.picone@unimore.it)                                     |
| **License**         | [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/) | 

A practical, run-it-live Python learning playground: small, self-contained
examples organized into progressive tracks, one concept per folder. Every
`main.py` docstring states what it demonstrates and what to look at while it runs.

## Playground structure

- **[`01-best-practices/`](01-best-practices/)** — Python habits that apply to
  any code, OOP or not: the `__main__` guard, exceptions, type hints,
  configuration, logging.
  - [`01-main-guard/`](01-best-practices/01-main-guard/) — `if __name__ == "__main__"`, run vs import, the `main()` pattern
  - [`02-exceptions/`](01-best-practices/02-exceptions/) — `try` / `except` / `else` / `finally`, several handlers, a custom `Exception`
  - [`03-type-hints/`](01-best-practices/03-type-hints/) — three type bugs that crash far from their cause, then hints as documentation + `isinstance()` as the real check
  - [`04-config/`](01-best-practices/04-config/) — moving values out of the code: `argparse`, environment variables, JSON / YAML config files
  - [`05-logging/`](01-best-practices/05-logging/) — `logging` instead of `print()`: severity levels, threshold filtering, output to a file

- **[`02-oop/`](02-oop/)** — object-oriented Python, one pillar per folder: from
  `class` syntax up to encapsulation, inheritance, polymorphism and abstraction.
  - [`01-class-basics/`](02-oop/01-class-basics/) — `class`, `__init__`, `self`, instance attributes; identity vs equality; a missing required argument raises `TypeError`, default parameter values fix it
  - [`02-methods-dunder/`](02-oop/02-methods-dunder/) — instance methods and dunder methods: `__str__`, `__eq__`, `__new__`, `__del__`
  - [`03-class-static-methods/`](02-oop/03-class-static-methods/) — class attributes, `@classmethod` + `cls`, `@staticmethod`, an alternative constructor; plus two class-attribute pitfalls (a shared mutable list, an accidentally-shadowed counter) and why Python has no real constants
  - [`04-encapsulation/`](02-oop/04-encapsulation/) — public / protected / private by convention (incl. name mangling), plain getters/setters, then `@property` / `.setter` / `.deleter`
  - [`05-inheritance/`](02-oop/05-inheritance/) — `super()`, method overriding, `type()` / `isinstance()`; multilevel and multiple inheritance; the MRO, including a real name conflict between two parents
  - [`06-polymorphism/`](02-oop/06-polymorphism/) — duck typing (`len`, `max`, and your own functions/classes), operator polymorphism, class-based polymorphism across unrelated classes, polymorphism via overriding inside a hierarchy (dynamic dispatch, the Open/Closed Principle), no method overloading (a redefinition silently replaces the old one), `*args` and default parameter values as the two replacements
  - [`07-abstraction/`](02-oop/07-abstraction/) — informal interface (`NotImplementedError`) vs `abc.ABC` + `@abstractmethod`; mixing abstract and concrete methods in the same `ABC`
  - [`08-custom-exceptions/`](02-oop/08-custom-exceptions/) — a domain-specific exception (`BatteryLowError`) carrying structured data

- **[`03-smart-home/`](03-smart-home/)** — the OOP capstone: a Smart Home IoT case
  study built incrementally, step by step, ending in a production-style `src/`
  project layout (full walk-through further down in this README).
  - [`step-1-devices/`](03-smart-home/step-1-devices/)
  - [`step-2-data-manager/`](03-smart-home/step-2-data-manager/)
  - [`step-3-smart-home/`](03-smart-home/step-3-smart-home/)
  - [`step-4-patterns/`](03-smart-home/step-4-patterns/)
  - [`step-5-src-layout/`](03-smart-home/step-5-src-layout/)

- **[`04-networking/`](04-networking/)** — UDP/TCP sockets and JSON-over-TCP,
  refactored to use the best practices above.
  - [`udp/`](04-networking/udp/) — `udp_server.py` + `udp_client.py` — connectionless echo
  - [`tcp/`](04-networking/tcp/) — `tcp_server.py` + `tcp_client.py` — connection-oriented echo
  - [`json/`](04-networking/json/) — an `IoTDevice` / `ServiceMessage` model sent as JSON over TCP; nested-object serialization and rebuild


Nothing here needs a third-party package except two spots that need `PyYAML` —
see [Setup](#setup).

---

## Setup

Python **3.10+** is required (the examples use `X | None` type-hint syntax).

### 1. Check your Python version(s)

**Linux / macOS**

```bash
python3 --version           # version of the default python3
which -a python3            # every python3 on your PATH
```

List each installed minor version:

```bash
ls /usr/bin/python3.*                                        # Linux (system)
ls /opt/homebrew/bin/python3.* /usr/local/bin/python3.* 2>/dev/null   # macOS (Homebrew)
pyenv versions                                               # if you use pyenv (any OS)
```

**Windows — PowerShell or cmd.exe**

```bat
py --version
py --list
where python
```

`py --version` shows the version the launcher picks by default; `py --list`
shows every Python version installed on the machine; `where python` shows the
paths.

If the default is below 3.10, install a newer one
(<https://www.python.org/downloads/> · Linux: your package manager · macOS:
`brew install python@3.12`). You can then aim `venv` at a specific version:
`python3.12 -m venv .venv` (Linux/macOS) or `py -3.12 -m venv .venv` (Windows).

### 2. Create and activate a virtual environment

A virtual environment is a private, isolated copy of Python and its packages for
this project only, so nothing is installed into the system Python. Create it
once, **at the repo root**:

**Linux / macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows — PowerShell**

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

> If PowerShell blocks the script, run once:
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`

**Windows — cmd.exe**

```bat
py -m venv .venv
.venv\Scripts\activate.bat
```

Your prompt now shows `(.venv)`. Run `deactivate` at any time to return to the
system Python. The `.venv/` folder is git-ignored — never commit it.

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

- [`requirements.txt`](requirements.txt) is the **recipe** (which packages, which
  versions); the `.venv/` folder is the disposable **kitchen** built from it. If
  `.venv/` ever breaks, delete it and recreate it from the recipe.
- `pip freeze > requirements.txt` regenerates the file after adding a package.
- `pyproject.toml` is a richer, modern alternative for declaring dependencies —
  not used anywhere in this repo, which deliberately stays on `requirements.txt`
  end to end (`03-smart-home/step-5` included).

### What actually needs the dependencies

Only two spots (`01-best-practices/04-config` YAML demo and `03-smart-home/step-5`).
Everything else is standard-library only and runs directly:

```bash
cd 02-oop/05-inheritance
python3 main.py
```

---

## Running in VS Code

The examples run from any editor, but VS Code adds one-click run and a debugger.

1. **Install the Python extension** (`ms-python.python`). It pulls in Pylance
   (autocomplete + type-checking, which reads the hints throughout this repo) and
   the debugger.
2. **Point VS Code at the virtual environment**: `Ctrl+Shift+P` →
   **Python: Select Interpreter** → pick the one inside `.venv`:
   - Linux / macOS: `./.venv/bin/python`
   - Windows: `.venv\Scripts\python.exe`

   VS Code usually lists it at the top as `('.venv')`. The choice is saved per
   workspace and shown in the status bar; new integrated terminals then
   auto-activate the venv (you see `(.venv)` in the prompt), and Pylance resolves
   `PyYAML` and friends from it.
3. **Run**: open any `main.py` and click ▶ *Run Python File* (top-right) or press
   `Ctrl+F5`. These multi-folder examples (`from car import Car`) work with no
   extra config — Python automatically adds the script's own folder to `sys.path`.
4. **Debug**: click in the gutter left of a line number to set a breakpoint,
   press `F5`, and choose **Python File** the first time. You get the variables
   pane, call stack, watch, and step controls (`F10` step over, `F11` step into).

---

## `03-smart-home/` — the Smart Home IoT case study

### The scenario

The proposed modeling is associated with a **Smart Home** equipped with various
IoT devices:

- Temperature sensors
- Humidity sensors
- Smart lights

The exercise consists of designing the data structures, identifying the classes
needed to model these devices — and implementing them in Python — and building a
**central system** that collects and manages the data coming from all of them.
The Smart Home itself is identified by an id and a location
(latitude/longitude), and keeps a list of connected devices it can add to,
remove from, and list.

### Why it's incremental, and how

Every `step-N-*/` folder is **runnable on its own**. Each step copies forward,
**unchanged**, the device files from the step before it, and adds exactly **one**
new modeling decision on top — nothing already built is ever rewritten or removed.
That means `diff`-ing two consecutive step folders shows precisely the one new
concept that step introduces, which is the point of walking through them live.

| Step | Builds on | Adds | Concept |
|---|---|---|---|
| `step-1-devices/` | — | `Device` → `Sensor` / `Actuator` → `TemperatureSensor`, `HumiditySensor`, `SmartLight`, each with its own id, manufacturer, and last reading/status | the class hierarchy, and the informal interfaces `update_value()` / `invoke_action()` |
| `step-2-data-manager/` | step 1's device files, verbatim | `DataManager` — pulls device storage *out* of the home | delegation / separation of concerns |
| `step-3-smart-home/` | step 2's files, verbatim | `SmartHome` — the central system: home id + location, delegating every device operation to the `DataManager`; a full monitoring scenario | composing the whole system |
| `step-4-patterns/` | step 3's files, verbatim | **Singleton** (one shared `DataManager`), **Factory** (`DeviceFactory`, plus a new `SmartLock` added with one class + one branch), **Observer** (a dashboard and a logger notified of state changes) | design patterns on top of the same model |
| `step-5-src-layout/` | the step-4 system, reorganized | the same classes split into a real `devices/ storage/ logic/ interface/` package, driven by a YAML config file, with logging and type hints throughout | production-style project layout |

Run order matches the table — `python3 main.py` inside each `step-N-*/` folder in
turn (`step-5-src-layout/` instead uses `python3 run.py`; see its own
[README](03-smart-home/step-5-src-layout/README.md), since it is meant to be lifted
into its own repository later).

