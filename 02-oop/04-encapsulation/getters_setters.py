"""
OOP hands-on - Step 04b: plain getters and setters (before @property).

Reference: python_oop.md 2.6.2.

A setter is genuinely useful: it can VALIDATE a new value before accepting
it. But this style changes how callers use the attribute - `car.model` is
no longer enough, everyone now has to remember `car.get_model()` /
`car.set_model(...)`. car.py (Step 04) removes exactly this drawback with
@property.
"""


class Car:
    def __init__(self, manufacturer: str, model: str) -> None:
        self._manufacturer = manufacturer
        self._model = model

    def get_model(self) -> str:
        return self._model

    def set_model(self, model: str) -> None:
        if not model:
            raise ValueError("model cannot be empty")
        self._model = model


def main() -> None:
    car = Car("Toyota", "Corolla")

    car.set_model("Yaris")
    print("get_model() ->", car.get_model())

    try:
        car.set_model("")
    except ValueError as e:
        print("rejected:", e)


if __name__ == "__main__":
    main()
