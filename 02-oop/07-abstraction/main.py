"""
Run:  python3 main.py

Walk-through (python_oop.md 2.9):
  1. informal interface: instantiating Vehicle() succeeds; it only fails
     when start() is actually called;
  2. formal abc: Vehicle() fails immediately at instantiation, and so does
     Motorcycle() because it implements start() but not stop();
  3. mixing_abstract_concrete.py: an ABC is not all-or-nothing - it can mix
     @abstractmethod methods (must be overridden) with ordinary concrete
     methods (inherited as-is, for free).
"""

import informal
import formal
import mixing_abstract_concrete


def main() -> None:
    print("--- informal interface (2.9.1) ---")
    car = informal.Car()
    print(car.start())

    v = informal.Vehicle()          # this succeeds...
    try:
        v.start()                   # ...and only THIS fails
    except NotImplementedError as e:
        print("NotImplementedError:", e)

    print("--- formal abc (2.9.2) ---")
    try:
        formal.Vehicle()
    except TypeError as e:
        print("cannot instantiate Vehicle:", e)

    try:
        formal.Motorcycle()         # start() ok, stop() missing
    except TypeError as e:
        print("cannot instantiate Motorcycle:", e)

    print(formal.Car().start())     # the complete subclass works

    print("--- mixing abstract and concrete methods (2.9) ---")
    mixing_abstract_concrete.main()


if __name__ == "__main__":
    main()
