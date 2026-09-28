"""
OOP hands-on - Step 06 (extra): Python has no method overloading.

Reference: python_oop.md 2.8.5.

Unlike Java or C++, defining a function (or method) twice under the same
name, with different parameters, does NOT create two overloads - the second
definition simply REPLACES the first. Only the last one ever exists; calling
it with the "old" signature fails.
"""


def product(a, b):
    return a * b


def product(a, b, c):          # this silently REPLACES the definition above
    return a * b * c


def main() -> None:
    print("product(4, 5, 5) ->", product(4, 5, 5))    # 100 - the only product() left

    try:
        product(4, 5)                                   # the 2-argument version is gone
    except TypeError as e:
        print(f"product(4, 5) fails now -> {e}")


if __name__ == "__main__":
    main()
