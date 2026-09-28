"""
OOP hands-on - Step 01: class basics.
Covers defining a class, the __init__ constructor, `self`, instance attributes.
"""

class Car:
    """A minimal class: only data (attributes), no behaviour yet.

    Attributes:
        manufacturer (str): the company that produced the car.
        model (str): the specific model name.
    """

    def __init__(self, manufacturer: str, model: str) -> None:
        # `self` is the instance being created; these are INSTANCE attributes,
        # unique to each object built from this class.
        self.manufacturer = manufacturer
        self.model = model


class CarWithDefaults:
    """Same idea, but every parameter has a default (2.3.3)."""

    def __init__(self, manufacturer: str = "Unknown", model: str = "Unknown") -> None:
        self.manufacturer = manufacturer
        self.model = model
