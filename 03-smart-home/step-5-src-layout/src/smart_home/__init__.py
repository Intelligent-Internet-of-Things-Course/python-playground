"""smart_home package - Smart Home IoT case study, src/ layout.

Subpackages, grouped by RESPONSIBILITY (not by convenience):
  devices/    - what a device IS   (Device -> Sensor / Actuator -> concrete)
  storage/    - how device data is kept and retrieved (DataManager)
  logic/      - what the system DECIDES to do (automation rules)
  interface/  - how the outside world talks to it (a CLI, for now)
"""

__version__ = "0.1.0"
