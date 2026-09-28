## `02-oop/` — object-oriented Python, one pillar per folder

Goal: from `class` syntax up to the four pillars — encapsulation, inheritance,
polymorphism, abstraction — each demonstrated in its own step.

| Step | Demonstrates |
|---|---|
| [`01-class-basics/`](01-class-basics/) | `class`, `__init__`, `self`, instance attributes; identity vs equality; a missing required argument raises `TypeError`, default parameter values fix it |
| [`02-methods-dunder/`](02-methods-dunder/) | instance methods and dunder methods: `__str__`, `__eq__`, `__new__`, `__del__` |
| [`03-class-static-methods/`](03-class-static-methods/) | class attributes, `@classmethod` + `cls`, `@staticmethod`, an alternative constructor; plus two class-attribute pitfalls (a shared mutable list, an accidentally-shadowed counter) and why Python has no real constants |
| [`04-encapsulation/`](04-encapsulation/) | public / protected / private by convention (incl. name mangling), plain getters/setters, then `@property` / `.setter` / `.deleter` |
| [`05-inheritance/`](05-inheritance/) | `super()`, method overriding, `type()` / `isinstance()`; multilevel and multiple inheritance; the MRO, including a real name conflict between two parents |
| [`06-polymorphism/`](06-polymorphism/) | duck typing (`len`, `max`, and your own functions/classes), operator polymorphism, class-based polymorphism across unrelated classes, polymorphism via overriding inside a hierarchy (dynamic dispatch, the Open/Closed Principle), no method overloading (a redefinition silently replaces the old one), `*args` and default parameter values as the two replacements |
| [`07-abstraction/`](07-abstraction/) | informal interface (`NotImplementedError`) vs `abc.ABC` + `@abstractmethod`; mixing abstract and concrete methods in the same `ABC` |
| [`08-custom-exceptions/`](08-custom-exceptions/) | a domain-specific exception (`BatteryLowError`) carrying structured data |

Each step is self-contained and runnable on its own — `python3 main.py`.
