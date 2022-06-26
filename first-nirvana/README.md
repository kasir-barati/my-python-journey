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

# Types

- Numbers
  - Integer: 1
  - Floating point: 1.1
- Strings
  - `"ad"`
  - `'ad'`
- Converting
  - `int`
    - If x is not a number. x must be a string, bytes, or bytearray instance representing an integer literal in radix base.
    - [Official Doc](https://docs.python.org/3/library/functions.html?highlight=int#int)

# String manipulation

- `str`
  - Return a string version of object.
  - If object is not provided, returns the empty string. Otherwise, the behavior of `str()` depends on whether encoding or errors is given, as follows.
  - [Official Doc](https://docs.python.org/3/library/stdtypes.html#str)
- `split`
  - Return a list of the words in the string, using sep as the delimiter string.
  - [Official Doc](https://docs.python.org/3/library/stdtypes.html#str.split)
