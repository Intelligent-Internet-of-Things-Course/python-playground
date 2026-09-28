"""
OOP hands-on - Step 06a: duck typing, beyond the built-ins.

Reference: python_oop.md 2.8.1.

len()/max() already show duck typing "for free". This file shows the same
benefit extends, with NO extra effort, to code you write yourself: a plain
function that only relies on operations many types support (like len()),
and a method name that unrelated classes just happen to share.
"""


def combined_length(a, b):
    # No type hints, no isinstance() checks: `a` and `b` can be anything
    # that supports len().
    return len(a) + len(b)


class Duck:
    def make_sound(self) -> str:
        return "Quack!"


class Dog:
    # Note: Dog does NOT inherit from Duck, and shares no common parent with it.
    def make_sound(self) -> str:
        return "Woof!"


def announce(animal) -> None:
    # No type check here: `animal` can be any object, as long as it has make_sound().
    print(animal.make_sound())


def main() -> None:
    print("--- duck typing on a user-defined function ---")
    print(combined_length("Hi", "Bye"))         # 5 -> two strings
    print(combined_length([1, 2], [3, 4, 5]))   # 5 -> two lists
    print(combined_length("Hi", [1, 2, 3]))     # 5 -> a string and a list, mixed freely

    print("--- duck typing across two unrelated classes ---")
    announce(Duck())   # Quack!
    announce(Dog())    # Woof!


if __name__ == "__main__":
    main()
