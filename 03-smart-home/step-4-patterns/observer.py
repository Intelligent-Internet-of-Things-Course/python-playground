"""
Smart Home capstone - Step 4c: Observer pattern.

Problem: notify other parts of the program when something changes here,
without tightly coupling them. Solution: a Subject keeps a list of Observers
and calls a common update() method on each when its state changes.

SmartHome (the Subject) knows nothing about what Dashboard/Logger actually
do - only that they expose update(event).
"""

class Subject:
    def __init__(self) -> None:
        # `observer: object` -> any object that has an update() method; there
        # is no shared base class on purpose (duck typing, python_oop.md 2.8.1).
        self._observers: list[object] = []

    def add_observer(self, observer: object) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: object) -> None:
        self._observers.remove(observer)

    def notify(self, event: str) -> None:
        for observer in self._observers:
            observer.update(event)

class DashboardObserver:
    def update(self, event: str) -> None:
        print(f"[Dashboard] {event}")

class LoggerObserver:
    def update(self, event: str) -> None:
        print(f"[Logger] {event}")

class SmartHome(Subject):
    def __init__(self, home_id: str) -> None:
        super().__init__()
        self.home_id = home_id

    def set_state(self, value: str) -> None:
        self.notify(f"home {self.home_id} state changed to {value}")
