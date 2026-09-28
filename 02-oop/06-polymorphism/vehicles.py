"""
OOP hands-on - Step 06: polymorphism.
Covers duck typing, class-based polymorphism, overriding, and *args instead of
method overloading (see also no_overloading.py, for the failure *args fixes).

Car and Motorcycle share NO common parent class - they only happen to agree
on having a start() method, which is already enough for class-based
polymorphism (2.8.3). HybridCar is added later in main.py ("Let's See How It
Works", 2.8.5) to show the same loop keeps working unmodified with a third,
still-unrelated class.

NOTE (2.8.3): this is usually NOT good design. Car/Motorcycle only look
convenient here because they share nearly identical code - in a real
codebase that overlap is the signal they should share a common Vehicle
PARENT instead (Section 2.7), not just a coincidental method name. Unrelated
class-based polymorphism is best reserved for classes that genuinely do not
belong to the same family (e.g. a plugin architecture), or where you do not
control one of the classes (e.g. a third-party library).
"""

class Car:
    def __init__(self, manufacturer: str, model: str) -> None:
        self.manufacturer = manufacturer
        self.model = model

    def start(self) -> str:
        return f"{self.manufacturer} {self.model}: engine starting..."

class Motorcycle:
    def __init__(self, manufacturer: str, model: str) -> None:
        self.manufacturer = manufacturer
        self.model = model

    def start(self) -> str:
        return f"{self.manufacturer} {self.model}: kick-starting..."

class HybridCar:
    def __init__(self, manufacturer: str, model: str) -> None:
        self.manufacturer = manufacturer
        self.model = model

    def start(self) -> str:
        return f"{self.manufacturer} {self.model}: starting in electric mode..."

# 2.8.5 - Python has no method overloading; *args is the idiomatic replacement.
# `*args` is left un-annotated on purpose: typing variadic arguments is beyond
# references python_best_practices.md 4.5, and here add() is deliberately used
# with both numbers and strings.
def add(*args):
    total = args[0]
    for value in args[1:]:
        total = total + value
    return total


# 2.8.5 - the other idiomatic replacement: default parameter values, for a
# SMALL, FIXED, known-in-advance set of optional parameters. Preferred over
# *args whenever it fits, because the signature stays named/self-documenting
# and keyword calls (add_with_defaults(a=2, c=4)) remain possible - at the
# cost of not scaling to an unknown number of arguments.
def add_with_defaults(a=None, b=None, c=None):
    if c is not None:
        return a + b + c
    if b is not None:
        return a + b
    return a
