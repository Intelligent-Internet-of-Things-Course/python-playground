"""
OOP hands-on - Step 04: encapsulation and access control.
Covers public / protected / private by convention, getters & setters,
and the Pythonic @property / .setter / .deleter.
"""

class Car:
    def __init__(self, manufacturer: str, model: str, license_plate: str) -> None:
        self.manufacturer = manufacturer        # public
        self._model = model                     # "protected" by convention (one underscore)
        # goes THROUGH the setter below, so an invalid plate cannot even be created
        self.license_plate = license_plate

    # ---- model: @property + .setter + .deleter (2.6.3) -------------------
    @property
    def model(self) -> str:
        return self._model

    @model.setter
    def model(self, value: str) -> None:
        if not value:
            raise ValueError("model cannot be empty")
        self._model = value

    @model.deleter
    def model(self) -> None:
        del self._model

    # ---- license_plate: validation on write (2.6.3, "Let's See How It Works")
    @property
    def license_plate(self) -> str:
        return self._license_plate

    @license_plate.setter
    def license_plate(self, value: str) -> None:
        if not isinstance(value, str) or len(value) != 7:
            raise ValueError("license_plate must be a 7-character string")
        self._license_plate = value

    def __str__(self) -> str:
        return f"{self.manufacturer} {self._model} [{self._license_plate}]"
