# PEP 0 guideline

-   [Ref](https://peps.python.org/pep-0008/)
-   Imports
    -   [Lazy Imports](https://peps.python.org/pep-0690/):
        -   transparently defer the execution of imported modules until the moment when an imported object is used.
        -   improving startup time and memory usage.
        -   mostly eliminate the risk of import cycles
        -   [To see an example click](https://peps.python.org/pep-0690/#example).
    -   For python 2. So I do not need to care right now
        -   [Import As](https://peps.python.org/pep-0221/)
        -   [Import on Case-Insensitive Platforms](https://peps.python.org/pep-0235/)
        -   [Import Modules from Zip Archives](https://peps.python.org/pep-0273/)
    -   [Imports: Multi-Line and Absolute/Relative](https://peps.python.org/pep-0328/)
-   Function
    -   [Syntax for late-bound function argument defaults](https://peps.python.org/pep-0671/)
        -   Instead of default values which are calculated during function definition and saved. This proposal introduces a new form of argument default, defined by an expression to be evaluated at function call time.
        -   **draft**

# PEP 8 guideline

-   `import`
    1. No long import statements
    ```py
    import os
    import sys
    ```
    2. Ambiguous
    ```py
    # TODO
    ```
-   Functions
    -   [lowercase, with words separated by underscores](https://peps.python.org/pep-0008/#function-and-variable-names)
    -   [Indentation](https://peps.python.org/pep-0008/#indentation)
    -   [Blank Lines](https://peps.python.org/pep-0008/#blank-lines)
        -   Top-level functions/classes surrounded with two blank lines
        -   Method surrounded by a single blank line
        -   Extra blank lines to separate groups of related functions.
        -   Blank lines inside functions to indicate logical sections sparingly.
-   The closing brace/bracket/parenthesis on multiline constructs
-   Tabs or Spaces? **spaces**
-   Maximum line character is 79 character
-   [Avoid extraneous whitespace in the following situations](https://peps.python.org/pep-0008/#whitespace-in-expressions-and-statements)

# Classes

-   A blueprint for having the same data structure everywhere we need
-   `self` is the first parameter for every class's method
-   No `new` keyword
    -   `enemy = Enemy()`
-   `__init__` is a special method who is called when we create a new instance of our class. In other word it is the venerable `constructor`. It can accepts parameters to initialize parameters.
