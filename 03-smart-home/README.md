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
[README](step-5-src-layout/README.md), since it is meant to be lifted
into its own repository later).
