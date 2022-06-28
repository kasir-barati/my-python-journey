# Battle project

-   [Literal Types](https://peps.python.org/pep-0586)
-   [`__init__` return type annotation](https://peps.python.org/pep-0484/)
-   [formatted string literals](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)
    -   It is the equivalent for template literal in javascript
-   [zip ](https://docs.python.org/3/library/functions.html#zip)
    -   Iterate over several iterables in parallel, producing tuples with an item from each one.
    -   There's two possible scenario here:
        -   How can you iterate over the combination of lists' variables simultaneously
        -   How can you loop over the combination of multiple list.
-   [enums](https://docs.python.org/3/library/enum.html)
-   [TypedDict](https://peps.python.org/pep-0589/)
    -   Type Hints for Dictionaries with a Fixed Set of Keys
    -   It will throw error when you wanna use the undefined key. I mean it won't throw error when you are assigning value. But when you wanna use wrong value it will throw error.
-   [Optional](https://peps.python.org/pep-0484/)
-   [Special parameters](https://docs.python.org/3/tutorial/controlflow.html#special-parameters)
    ```py
    def standard_arg(arg):
    print(arg)
    def pos_only_arg(arg, /):
        print(arg)
    def kwd_only_arg(*, arg):
        print(arg)
    def combined_example(pos_only, /, standard, *, kwd_only):
        print(pos_only, standard, kwd_only)
    ```

# [Classes](https://docs.python.org/3/tutorial/classes.html)

-   **Read doc for sure. It is more detailed than an tutorial**
-   A namespace
    ```py
    class ClassName:
        <statement-1>
        .
        .
        .
        <statement-N>
    ```
-   An object
-   We have `__init__` which will be called when we create a new instance of our class by calling the class.
    -   It is comparable with `constructor`
-   Supported operations in a class object
    -   Attribute references
        -   We can do `Color.GREEN`.
        -   This is sorta countrposable with `static` properties in TS/JS
        -   Statements like `GREEN` is a attribute reference
        -   Remember adding new Attribute reference in a Class propagate it to all instances, unless the instance specify that attribute reference too.
    -   instantiation
        -   In python we can add new data attribute - what we call property in js - to the class after instantiation.
        -   In other word if we wanna have normal properties - Not static - we should define them inside the `__init__` to make them specific to that instance
-   [`vars`](https://docs.python.org/3/library/functions.html#vars)
    -   attribute for a module, class, instance, or any other object
    -   Without an argument, `vars()` acts like [`locals()`](https://docs.python.org/3/library/functions.html#locals)
        -   **Not in my case which showing another class attributes**
-   [`@abstractmethod`](https://docs.python.org/3/library/abc.html?highlight=abstractmethod#abc.abstractmethod)
    -   A decorator indicating abstract methods.
    -   Derived from `ABC`
        -   Cannot be instantiated unless all of its abstract methods and properties are overridden.
-   [`ABC` class](https://docs.python.org/3/library/abc.html?highlight=abstractmethod#abc.ABCMeta)
    -   Use this **metaclass** to create an ABC
    -   An ABC can be subclassed directly

# Functions

-   Be aware that in python like what we have in JS passed arguments to a function have two possible situation:
    1. Passed by value:
        ```py
        def test(number: int):
            number += 10
            print(number) # 11
        n = 1
        test(n)
        print(n) # 1
        ```
    2. Passed by reference: what we have: `print_player_and_enemy_status`. If in this function you change the values of person or enemy it will affect the original passed ones.
