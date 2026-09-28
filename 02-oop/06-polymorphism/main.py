"""
Run:  python3 main.py

Walk-through (python_oop.md 2.8), in the lecture's own incremental order:
  1. built-in duck typing / operator polymorphism come for free (2.8.1/2.8.2);
  2. duck_typing.py - the same benefit, with no extra effort, on a function
     and on two of YOUR OWN classes (2.8.1);
  3. a loop over 2 unrelated classes calls start() without any type check
     (2.8.3);
  4. polymorphism_via_overriding.py - the SAME call gives a DIFFERENT result
     depending on the actual class, inside an inheritance hierarchy (2.8.4);
  5. no_overloading.py - Python has no method overloading: redefining
     product() with a different signature just replaces it (2.8.5);
  6. add(*args) and add_with_defaults(...) are the two idiomatic replacements
     (2.8.5);
  7. "Let's See How It Works" - a third, still-unrelated class (HybridCar)
     joins the same list, and the exact same loop keeps working unmodified.
"""

import duck_typing
import no_overloading
import polymorphism_via_overriding
from vehicles import Car, Motorcycle, HybridCar, add, add_with_defaults


def main() -> None:
    # 2.8.1 - duck typing: the same call adapts to whatever type it receives
    print(len("Hello"), len([1, 2, 3]))          # 5 3 -> string length, list length
    print(max(1, 3, 2), max("a", "z", "m"))      # 3 z -> numeric max, alphabetic max

    # 2.8.2 - operators are polymorphic too: + means something different each time
    print(5 + 10, "Hello " + "World!", [1, 2] + [3, 4])

    print()
    print("=== duck_typing.py: your own functions and classes (2.8.1) ===")
    duck_typing.main()

    # 2.8.3 - class-based polymorphism, baseline: 2 unrelated classes
    print()
    vehicles = [
        Car("Toyota", "Corolla"),
        Motorcycle("Ducati", "Monster"),
    ]
    for v in vehicles:
        print(v.start())          # no isinstance() check anywhere

    print()
    print("=== polymorphism_via_overriding.py: inside a hierarchy (2.8.4) ===")
    polymorphism_via_overriding.main()

    # 2.8.5 - Python has no method overloading (see no_overloading.py)
    print()
    no_overloading.main()

    # 2.8.5 - two idiomatic replacements: unbounded *args, or a small fixed
    # set of named optional parameters with default values
    print()
    print(add(2, 3))
    print(add(2, 3, 4))
    print(add("Hello, ", "World!"))

    print()
    print(add_with_defaults(2, 3))         # 5  -> only a and b provided
    print(add_with_defaults(2, 3, 4))      # 9  -> a, b and c all provided
    try:
        add_with_defaults(a=2, c=4)        # b was skipped, but c was provided
    except TypeError as e:
        print("add_with_defaults(a=2, c=4) fails ->", e)

    # "Let's See How It Works" - add a THIRD unrelated class to the same list;
    # nothing about the loop above needs to change
    print()
    vehicles.append(HybridCar("Toyota", "Prius"))
    for v in vehicles:
        print(v.start())


if __name__ == "__main__":
    main()
