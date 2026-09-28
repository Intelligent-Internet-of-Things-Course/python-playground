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
  configuration, logging — see its own [README](01-best-practices/README.md).
  - [`01-main-guard/`](01-best-practices/01-main-guard/)
  - [`02-exceptions/`](01-best-practices/02-exceptions/)
  - [`03-type-hints/`](01-best-practices/03-type-hints/)
  - [`04-config/`](01-best-practices/04-config/)
  - [`05-logging/`](01-best-practices/05-logging/)

- **[`02-oop/`](02-oop/)** — object-oriented Python, one pillar per folder: from
  `class` syntax up to encapsulation, inheritance, polymorphism and abstraction —
  see its own [README](02-oop/README.md).
  - [`01-class-basics/`](02-oop/01-class-basics/)
  - [`02-methods-dunder/`](02-oop/02-methods-dunder/)
  - [`03-class-static-methods/`](02-oop/03-class-static-methods/)
  - [`04-encapsulation/`](02-oop/04-encapsulation/)
  - [`05-inheritance/`](02-oop/05-inheritance/)
  - [`06-polymorphism/`](02-oop/06-polymorphism/)
  - [`07-abstraction/`](02-oop/07-abstraction/)
  - [`08-custom-exceptions/`](02-oop/08-custom-exceptions/)

- **[`03-smart-home/`](03-smart-home/)** — the OOP capstone: a Smart Home IoT case
  study built incrementally, step by step, ending in a production-style `src/`
  project layout — see its own [README](03-smart-home/README.md) for the scenario
  and the full step-by-step walk-through.
  - [`step-1-devices/`](03-smart-home/step-1-devices/)
  - [`step-2-data-manager/`](03-smart-home/step-2-data-manager/)
  - [`step-3-smart-home/`](03-smart-home/step-3-smart-home/)
  - [`step-4-patterns/`](03-smart-home/step-4-patterns/)
  - [`step-5-src-layout/`](03-smart-home/step-5-src-layout/)

- **[`04-networking/`](04-networking/)** — UDP/TCP sockets and JSON-over-TCP,
  refactored to use the best practices above — see its own
  [README](04-networking/README.md).
  - [`udp/`](04-networking/udp/)
  - [`tcp/`](04-networking/tcp/)
  - [`json/`](04-networking/json/)


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
