# =========================================
# __name__ VARIABLE IN PYTHON
# =========================================

print("Top Level Execution")
print("__name__ value:", __name__)


def greet():
    print("Hello from greet() function")


# -----------------------------------------
# DIRECT EXECUTION CHECK
# -----------------------------------------

if __name__ == "__main__":
    print("\nThis file is running directly")
    greet()
else:
    print("\nThis file was imported")


# =========================================
# IMPORTANT NOTES
# =========================================

"""
Case 1:
When this file runs directly:

python 04_main_dunder.py

Then:
__name__ = "__main__"


Case 2:
When this file is imported
inside another file:

import main_dunder

Then:
__name__ becomes the module name

Example:
__name__ = "main_dunder"


------------------------------------------------

IMPORTANT:

Python imports use module names,
which must follow Python identifier rules.

Valid:
    import calculator
    import main_dunder

Invalid:
    import 01_calculator
    import 04_main_dunder

Why invalid?

Because Python identifiers cannot
start with numbers.

------------------------------------------------

TRY THIS YOURSELF:

1. Rename this file:

    04_main_dunder.py

to:

    main_dunder.py

2. Create another file:

    test_import.py

3. Write:

    import main_dunder

4. Run:
    
    python test_import.py

Observe:
- __name__ changes
- imported files execute top-level code
- __main__ block does not run
"""