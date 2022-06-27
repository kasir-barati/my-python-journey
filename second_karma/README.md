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
-   [Modules/packages naming convention](https://peps.python.org/pep-0008/#package-and-module-names)
    -   short, all lowercase
    -   Do not use underscore if you can do namespacing. This is just my comprehension, Do not take it as something which reflects a PEP guideline.
        ```
        math_sum/
            __init__.py
            sum.py
        math_multiply/
            __init__.py
            multiply.py
        ```
        And then doing this:
        ```py
        from .math_sum.sum import sum
        from .math_multiply.multiply import multiply
        ```
        **Instead**
        ```
        math/
            __init__.py
            sum.py
            multiply.py
        ```
        and then do this:
        ```py
        from .math.sum import sum
        from .math.multiply import multiply
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

# Import from local modules

-   Create an `__init__.py` which is empty
-   To import local file and prevent misunderstanding we need to use `..` or `.`
    -   But in my code it does not work. Why? IDK. But I will understand it.
        -   [I find answer here](https://discord.com/channels/238666723824238602/308729304949194752/990825149559369728)
        -   What's happening here is a byproduct of the way you are launching python
            -   Side note: I did launch like this: `$ python3 second-karma/import.py`
        -   So, what's happening here is a byproduct of the way you are launching python
            -   What is byproduct?
                -   Python has a concept of packages, which is basically a folder containing one or more modules, and zero-or-more packages.
                -   When we launch python, there are two ways of doing it:
                    -   Asking python to **execute a specific module** (`python3 path/to/file.py`).
                    -   Asking python to **execute a package**.
                -   The issue is that `import.py` makes reference to importing `.math`
                    -   The `.math` in this context means "go find a module/package in the current package with the name math"
                    -   Trouble:
                        -   When I execute as `$ python3 second-karma/import.py` I was executing a module, not a package. thus python has no idea what `.` means in this context
                        -   Secondarily, `second-karma` isn't a valid python name, so it cannot be a package.
                        -   Fix:
                            ```cmd
                            mv second-karma second_karma  # rename directory to be a valid python name
                            touch second_karma/__init__.py  # ensure second_karma can be treated as a package
                            python3 -m second_karma.import
                            ```
                        -   Now `import.py` is of parent package `second_karma`, and thus your relative import will work.
