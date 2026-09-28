"""
Best practices hands-on - Step 03, bug 3 of 3: iterating over a list that
mixes types.

Run:  python3 bug_3_mixed_list.py     -> it CRASHES on purpose.

------------------------------------------------------------------------
WHAT THE BUG IS
------------------------------------------------------------------------
`sensor_values` should be numbers only, but two bad values slipped in -
as happens with data from a file or an API:
    sensor_values = [21, 19, True, "22.5", 20]
                          ^^^^  ^^^^^^
                          bool  string that "looks like" a number

Walking the summing loop shows TWO opposite failure modes:
  21, 19   -> fine, total = 40
  True     -> NO crash. bool is a subclass of int, so True is silently
              treated as 1; total becomes 41 and the average is quietly
              WRONG, with no error at all.
  "22.5"   -> ONLY here does it crash:
              TypeError: unsupported operand type(s) for +=: 'int' and 'str'
              Python does not treat a string as a number just because it
              reads like one.
  20       -> never reached.

WHERE IT IS INTRODUCED    -> the list literal (mixing types is legal).
WHERE IT ACTUALLY CRASHES -> `total += value` on the "22.5" iteration -
                             but the `True` corruption happened silently
                             one iteration earlier.

HOW TO FIX IT (see average_valid below, and section 4.3)
Filter with isinstance() BEFORE using each value, and check `bool`
FIRST and separately, because isinstance(True, int) is itself True.
"""

sensor_values = [21, 19, True, "22.5", 20]

def average_broken(values):
    total = 0
    for value in values:
        total += value                 # <-- crashes on "22.5"
    return total / len(values)

def average_valid(values):
    """Corrected: skip anything that is not a real numeric reading."""
    total = 0.0
    count = 0
    for value in values:
        if isinstance(value, bool):            # must come BEFORE the int/float check
            print(f"  skipping {value!r}: a boolean, not a measurement")
            continue
        if isinstance(value, (int, float)):
            total += value
            count += 1
        else:
            print(f"  skipping {value!r}: not a number")
    return total / count if count else None

def main():
    print(f"sensor_values = {sensor_values}")
    print("computing average_broken(...) ...")
    print("average:", average_broken(sensor_values))   # <-- TypeError happens HERE

if __name__ == "__main__":
    # Fixed version, for comparison:
    # print("valid average:", average_valid(sensor_values))   # -> 20.0
    main()
