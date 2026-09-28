"""
OOP hands-on - Step 04a: access modifiers (public / protected / private).

Reference: python_oop.md 2.6.1.

Python has no enforced access control - these are CONVENTIONS, not real
restrictions. A single leading underscore signals "protected" (use only
inside the class and its subclasses); a double leading underscore triggers
NAME MANGLING, which only makes the attribute a little harder to reach by
accident from outside, never impossible.
"""


class Car:
    def __init__(self, manufacturer: str, model: str, engine_serial: str) -> None:
        self.manufacturer = manufacturer       # public
        self._model = model                    # protected (one underscore): a convention
        self.__engine_serial = engine_serial    # private (two underscores): name-mangled


def main() -> None:
    car = Car("Toyota", "Corolla", "X123")

    # public: works exactly as expected
    print("car.manufacturer ->", car.manufacturer)

    # protected: nothing stops external code from reading/writing it anyway -
    # the leading underscore is only a signal, not an enforced restriction
    print("car._model ->", car._model)

    # private: `car.__engine_serial` would raise AttributeError - Python
    # renamed it internally to `_Car__engine_serial` ("name mangling")
    try:
        print(car.__engine_serial)
    except AttributeError as e:
        print("car.__engine_serial fails ->", e)

    print("car._Car__engine_serial ->", car._Car__engine_serial, "<- still reachable")


if __name__ == "__main__":
    main()
