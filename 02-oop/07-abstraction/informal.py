"""
OOP hands-on - Step 07a: INFORMAL interfaces.

A base class declares placeholder methods that raise NotImplementedError.
Nothing stops an incomplete subclass from being instantiated - the problem
only surfaces the first time the missing method is actually CALLED.
"""

class Vehicle:
    def start(self) -> str:
        raise NotImplementedError("Subclasses must implement start()")

    def stop(self) -> str:
        raise NotImplementedError("Subclasses must implement stop()")

class Car(Vehicle):
    def start(self) -> str:
        return "Car engine starting..."

    def stop(self) -> str:
        return "Car engine stopping..."
