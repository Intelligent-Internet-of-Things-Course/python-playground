"""
Best practices hands-on - Step 03, bug 1 of 3: a function that "forgets"
to return something on one branch.

Run:  python3 bug_1_missing_return.py     -> it CRASHES on purpose.

------------------------------------------------------------------------
WHAT THE BUG IS
------------------------------------------------------------------------
get_discount() has an `if` for "SUMMER" and an `elif` for "WINTER", and
nothing else. For ANY other code ("SPRING", "", None, a typo...) the
function falls off the end and Python makes it return None implicitly.

WHERE IT IS INTRODUCED   -> inside get_discount(), the missing `else`.
WHERE IT ACTUALLY CRASHES -> several lines later, at `price * discount`,
                             where `discount` is None:
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'

WHY DYNAMIC TYPING LETS IT THROUGH
A statically typed language would reject a function declared to return a
number that can also return nothing. Python has no such check: the
mismatch only surfaces when the exact line that misuses the None runs -
and only for the discount codes nobody thought to test. In a real
codebase get_discount() and `price * discount` could be in different
files, written months apart.

HOW TO FIX IT (see get_discount_fixed below, and section 4.2)
Guarantee the function returns the SAME KIND of value on every branch:
add an explicit `else: return 0.0`.
"""

def get_discount(code):
    if code == "SUMMER":
        return 0.20
    elif code == "WINTER":
        return 0.10
    # BUG: no branch for anything else -> implicitly returns None

def get_discount_fixed(code):
    """The corrected version - always returns a float, never None."""
    if code == "SUMMER":
        return 0.20
    elif code == "WINTER":
        return 0.10
    else:
        return 0.0

def main():
    price = 100
    discount = get_discount("SPRING")          # not handled -> None
    print(f"discount for 'SPRING' -> {discount!r}  (should have been a float)")
    final_price = price - (price * discount)   # <-- TypeError happens HERE
    print(f"final price -> {final_price}")

if __name__ == "__main__":
    # To watch the fixed version run cleanly instead, comment out main()
    # and uncomment the two lines below:
    # print(get_discount_fixed("SPRING"))                 # 0.0
    # print(100 - (100 * get_discount_fixed("SPRING")))   # 100.0
    main()
