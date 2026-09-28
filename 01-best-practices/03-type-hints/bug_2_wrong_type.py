"""
Best practices hands-on - Step 03, bug 2 of 3: passing an object of the
wrong type into a function.

Run:  python3 bug_2_wrong_type.py     -> it CRASHES on purpose.

------------------------------------------------------------------------
WHAT THE BUG IS
------------------------------------------------------------------------
get_user_email() was written assuming `user` is a dictionary, so it does
`user["email"]`. But it is called with a `User` OBJECT, whose email is an
attribute (`user.email`), not a dict key.

WHERE IT IS INTRODUCED    -> the call site: get_user_email(u), with `u`
                             being a User instance.
WHERE IT ACTUALLY CRASHES -> inside get_user_email(), at `user["email"]`:
    TypeError: 'User' object is not subscriptable

WHY DYNAMIC TYPING LETS IT THROUGH
Nothing in the language records that get_user_email() expects a dict.
Any object can be passed; the mismatch is discovered only the moment
`user["email"]` actually executes. A `def get_user_email(user: dict)`
hint (step 03b) plus a type checker would flag this before running.

HOW TO FIX IT (see the two *_fixed helpers below, and sections 4.2 - 4.3)
Either commit to one representation and name the parameter for it, or
guard with isinstance() and handle both. Both are shown below.
"""

def get_user_email(user):
    return user["email"]          # assumes a dict - the bug

class User:
    def __init__(self, email):
        self.email = email

def get_user_email_fixed_attr(user):
    """Corrected: expect a User object and read the attribute."""
    return user.email

def get_user_email_fixed_both(user):
    """Corrected: accept either a dict or an object with an .email attribute."""
    if isinstance(user, dict):
        return user["email"]
    return user.email

def main():
    u = User("alice@example.com")
    print(f"u is a {type(u).__name__} with u.email = {u.email!r}")
    print("calling get_user_email(u) ...")
    print(get_user_email(u))      # <-- TypeError happens HERE

if __name__ == "__main__":
    # Fixed versions, for comparison:
    # print(get_user_email_fixed_attr(User("bob@example.com")))
    # print(get_user_email_fixed_both({"email": "carol@example.com"}))
    main()
