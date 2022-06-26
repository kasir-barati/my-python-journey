# What is python

- Pretty branches
  - Python 2
  - Python 3
- Python is built around two focal point:
  - simplicity
  - readability
- Installation:
  - In Linux most of time is preinstalled
    - Maybe you need to upgrade
  - `sudo apt-get install python3`
  - `sudo pacman -Syu python3`

# Interpreter VS Compiled

- Compiling programming language:
  - You wrote code and then compile it with another application
- Interpreter programming language:
  - You wrote code, execute it right away
  - Just in time compilation/interpolation into machine language

# IDE

- Efficient IDE for python is not PyCharm
  - In my experience it was not even close to good. I could type things that were not exists in python and no error in IDE.
  - Really tough with CPU
- Installation
  - `sudo yay pycharm-community`
  - `sudo snap install pycharm-community --classic`
- My prefer is VSCode. [Install these extensions](https://bas.codes/posts/best-vscode-extensions-python). Press ctrl+p and:
  - `ext install KevinRose.vsc-python-indent`
  - `ext install KevinRose.vsc-python-indent`
  - `ext install njqdev.vscode-python-typehint`
  - `ext install njpwerner.autodocstring`
  - `ext install thebarkman.vscode-djaneiro`

# Variables

- No need to specify the variable type
  - Things like `string var1 = ''`
- No keyword to define a variable.
  - Things like `let var1 = 1`, `const cons1 = '2'` in TS/JS

# Types

- Numbers
  - Integer: 1
  - Floating point: 1.1
- Strings

  - `"ad"`
  - `'ad'`
  - String manipulation
    - `str`
      - Return a string version of object.
      - If object is not provided, returns the empty string. Otherwise, the behavior of `str()` depends on whether encoding or errors is given, as follows.
      - [Official Doc](https://docs.python.org/3/library/stdtypes.html#str)
    - `split`
      - Return a list of the words in the string, using sep as the delimiter string.
      - [Official Doc](https://docs.python.org/3/library/stdtypes.html#str.split)

- Converting
  - `int`
    - If x is not a number. x must be a string, bytes, or bytearray instance representing an integer literal in radix base.
    - [Official Doc](https://docs.python.org/3/library/functions.html?highlight=int#int)
- Boolean
  - In python: `True` and `False`
  - IDK what can I do about prettier in python
- Lists
  - Their medieval name is array.
- Dictionaries
  - Their venerable name is objects
  - A little harder compare to TS/JS

# Functions

- Built-in ones:
  - e.x. `print`, `str`, `sort`, `int`, `bool`, `len`, `sorted`, etc
- Custom ones
  - We follow some [PEP](#pep-guideline)
  - Type hint:
    - **Python doesn't check any of the type annotations**. If you just run the file normally, the hints are just for readers (and you can also access type hints within code, e.g. with typing.get_type_hints). To really use the type hints, use a tool like [MyPy](https://mypy.readthedocs.io/en/stable/) which is a static analyzer.
    - Void return type: Python doesn't have functions with void return type. Any function (or branch in a function) without an explicit return will return None. [ref](https://stackoverflow.com/questions/36797282/).
    - [`list` vs `List` in python](https://stackoverflow.com/a/56506137/8784518). Short answer there is not difference, you can use them as each other's successor
  - Default arguments

# PEP guideline

- They are counterpose of perttier in TS/JS world.
- It is supposed to be styling guideline
- Abbreviation form of Python Enterprise Proposal.
- Creator of Python, Guido van Rossum said, <q>Code is much more often than it is written.</q>
- I specified my chosen style with a :capricorn:
- Conventions:
  - Naming:
    - Functions:
      - `myfunction`
      - `my_function` :capricorn:
    - Variables:
      - `variable_name`
    - Classes:
      - `MyClass`
    - Methods:
      - `find_all`
    - Constants:
      - `MYCONSTANT`
      - `MY_CONSTANT` :capricorn:
    - Modules: IDK but I guess it means files name
      - `module_name.py`
    - Packages:
      - `mypackage`
      - `my_package` :capricorn:
  - Line width:
    - [ref1](https://note.nkmk.me/en/python-method-chain-line-break/), [ref2](https://realpython.com/python-pep8/), and [ref3](https://www.javatpoint.com/pep-8-in-python)
    - Keep the line to fewer than 79. I wish to the start, I wanted my venerable prettier in python :sob:.
    - Line Break convention :capricorn:
      ```py
      #  delimiter.
      obj = func_name(
          argument_one,
          argument_two,
          argument_three,
          argument_four)
      # first line doesn't has any argument
      # We add 4 spaces from the second line to discriminate arguments from the rest.
      # Double indent on the line continuation. Aid you to distinguish between function args & body
      def function_name(
              argument_one, argument_two, argument_three,
              argument_four):
          print(argument_two)
      # break lines only where there are many characters.
      dfdf_mc_break_mc = pd.read_csv(
          'data/src/sample_pandas_normal.csv', index_col=0
      ).assign(
          point_ratio=df['point'] / 100
      ).drop(columns='state').sort_values('age').head(3)
      # Enclose in parentheses to break lines
      df_mc_break_parens = (
          pd.read_csv('data/src/sample_pandas_normal.csv', index_col=0)
          .assign(point_ratio=df['point'] / 100)
          .drop(columns='state')
          .sort_values('age')
          .head(3)
      )
      list_of_numbers = [
          1, 2, 3,
          4, 5, 6,
          7, 8, 9
      ]
      ```
  - Indentation :capricorn:
    - Use tabs or whitespace. Do not use them in conjunction.
    - 4 **space** for indentation
    - :warning:It defines the code block.
  - White spacing :capricorn:
    ```py
    # Recommended
    my_list = [1, 2, 3]
    # Not recommended
    my_list = [ 1, 2, 3, ]
    ```
    ```py
    x = 5
    y = 6
    # Recommended
    print(x, y)
    # Not recommended
    print(x , y)
    ```
    ```py
    def double(x):
    return x * 2
    # Recommended
    double(3)
    # Not recommended
    double (3)
    ```
    ```py
    # Recommended
    list[3]
    # Not recommended
    list [3]
    ```
    ```py
    # Recommended
    tuple = (1,)
    # Not recommended
    tuple = (1, )
    ```
    ```py
    # Recommended
    var1 = 5
    var2 = 6
    some_long_var = 7
    # Not recommended
    var1          = 5
    var2          = 6
    some_long_var = 7
    ```
  - Programming Recommendations
    ```py
    # Not recommended
    my_bool = 6 > 5
    if my_bool == True:
        return '6 is bigger than 5'
    # Recommended
    if my_bool:
        return '6 is bigger than 5'
    ```
    ```py
    # Not recommended
    my_list = []
    if not len(my_list):
        print('List is empty!')
    # Recommended
    my_list = []
    if not my_list:
        print('List is empty!')
    ```
    ```py
    # Not recommended
    if not x is None:
        return 'x exists!'
    # Recommended
    if x is not None:
        return 'x exists!'
    ```
    ```py
    # Not Recommended
    if arg:
        # Do something with arg...
    # Recommended
    if arg is not None:
        # Do something with arg...
    ```
    ```py
    # Not recommended
    if word[:3] == 'cat':
        print('The word starts with "cat"')
    # Recommended
    if word.startswith('cat'):
        print('The word starts with "cat"')
    ```
    ```py
    # Not recommended
    if file_name[-3:] == 'jpg':
        print('The file is a JPEG')
    # Recommended
    if file_name.endswith('jpg'):
        print('The file is a JPEG')
    ```
  - Importing module
    ```py
    # Correct
    import pygame
    import os
    import sys
    # Wrong
    import sys, os
    ```
  - Aid to ensure PEP:
    - Linters: these libs works as we had eslint with one difference, They have not a flag to fix our code.
      - pycodestyle:
        1. `pip install pycodestyle`
        2. `pycodestyle code.py`
      - flake8:
        1. `pip install flake8`
        2. `flake8 code.py`
    - Autoformatters: These libs do refactor our code to follow PEP.
      - [black](https://pypi.org/project/black/)
        1. `pip install black`
        2. `black --line-length=79 code.py`
      - [autopep8](https://pypi.org/project/autopep8/)
        1. `pip install autopep8`
        2. `autopep8 --in-place --aggressive --aggressive <filename>`
    - [A good article](https://realpython.com/python-code-quality/)
