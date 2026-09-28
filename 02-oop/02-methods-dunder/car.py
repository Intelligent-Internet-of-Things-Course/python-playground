"""
OOP hands-on - Step 02: instance methods and dunder (magic) methods.
Covers instance methods, __str__, __eq__, __new__ + __init__, __del__.
"""

class Car:
    # __new__ is left un-annotated on purpose: typing it correctly is an
    # advanced topic, beyond references python_best_practices.md 4.5.
    def __new__(cls, *args, **kwargs):
        # 2.4.4 - __new__ ALLOCATES the instance and runs BEFORE __init__.
        # In everyday code you never need to write this; it is here only to
        # make the two-step creation visible.
        print("  [__new__] allocating a new Car instance")
        return super().__new__(cls)

    def __init__(self, manufacturer: str, model: str) -> None:
        print("  [__init__] initialising the Car instance")
        self.manufacturer = manufacturer
        self.model = model

    # 2.4.1 - a plain instance method
    def description(self) -> str:
        return f"Manufacturer: {self.manufacturer} Model: {self.model}"

    # 2.4.2 - the Pythonic replacement for a custom description():
    # used automatically by print() and str().
    def __str__(self) -> str:
        return f"Manufacturer: {self.manufacturer} - Model: {self.model}"

    # 2.4.3 - custom equality: compare by CONTENT instead of identity.
    # `other: object` -> beyond references 4.5: `object` means "any type at
    # all", used here because __eq__ may be called with any kind of value.
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Car):
            return NotImplemented
        return (self.manufacturer, self.model) == (other.manufacturer, other.model)

    # 2.4.5 - destructor, called by the garbage collector
    def __del__(self) -> None:
        print(f"  [__del__] {self.manufacturer} {self.model} destroyed!")
