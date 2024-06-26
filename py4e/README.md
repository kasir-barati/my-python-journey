# OS

This module provides a portable way of using operating system dependent functionality.

## `os.system(command)`

Execute the command (a string) in a sub-shell. If command generates any output, it will be sent to the interpreter standard output stream.

The return value of the Python function is system-dependent.

-   On Unix, the return value is the exit status of the process encoded in the format specified for wait().
-   On Windows, the return value is that returned by the system shell after running command.

# `sys.exit()`

The optional argument arg can be an integer giving the exit status (defaulting to zero),

If it is an integer, zero is considered “successful termination” and any nonzero value is considered “abnormal termination” by shells and the like.

Most systems require it to be in the range 0-127, and produce undefined results otherwise.

Cleanup actions specified by `finally` clauses of `try` statements are honored, and it is possible to intercept the exit attempt at an outer level.

Unlike `quit()` and `exit()`, `sys.exit()` is recommended for use in production code. It raises a `SystemExit` exception that can be caught and handled (Could not find any ref in the official doc :/).

# `len()`

# `try...except...else...finally` statement

The `try` statement specifies exception handlers and/or cleanup code for a group of statements

## `except` clause

The `except` clause(s) specify one or more exception handlers. Here the `Exception` is a common base class for all non-exit exceptions.

## `else` clause

The optional `else` clause is executed if the control flow leaves the `try` suite, no exception was raised, and no `return`, `continue`, or `break` statement was executed.

> [!CAUTION]
> Exceptions in the `else` clause **are not** handled by the preceding `except` clauses.

## `finally` clause

If `finally` is present, it specifies a 'cleanup' handler. When a `return`, `break` or `continue` statement is executed in the `try` suite of a _try…finally_ statement, the `finally` clause is also executed 'on the way out.'

1.  The `try` clause is executed.
2.  If an exception occurs in any of the clauses (does not matter where it was occurred; `try`, `else`, or `except`) and is not handled, the exception is temporarily saved.
3.  The `finally` clause is executed.
4.  If there is a saved exception it is re-raised at the end of the `finally` clause.
5.  If the `finally` clause raises another exception, the saved exception is set as the context of the new exception.
6.  If the `finally` clause executes a `return`, `break` or `continue` statement, the saved exception is discarded.

# `print()`

Print objects to the text stream file, separated by `sep` and followed by `end`. The `file` argument must be an object with a `write(string)` method; `sys.stdout` is the default value.

## `sys.stdin`, `sys.stdout`, `sys.stderr`

File objects used by the interpreter for standard input, output and errors:

-   `stdin` is used for all interactive input (including calls to `input()`).
-   `stdout` is used for the output of `print()` and expression statements and for the prompts of `input()`;
-   The interpreter's own prompts and its error messages go to `stderr`.

# `dict()`

Return a new dictionary initialized from an optional positional argument and a possibly empty set of keyword arguments.

-   Use a comma-separated list of key:
    -   `{'jack': 4098, 'ford': 4127}`
    -   `{4098: 'jack', 4127: 'ford'}`
-   Use a dict comprehension:

    -   `{}`
    -   `{x: x ** 2 for x in range(10)}`

    ![Create dictionary using dict comprehension](./create-dict-1.png)

-   Use the type constructor:

    -   `dict()`
    -   `dict([('foo', 100), ('bar', 200)])`
    -   `dict(foo=100, bar=200)`

    ![Create dictionary using dict constructor](./create-dict-2.png)

# `open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)`

Open file and return a corresponding file object. If the file cannot be opened, an `OSError` is raised. `file` is a path-like object giving the pathname (absolute or relative to the current working directory) of the file to be opened. `mode` is an optional string that specifies the mode in which the file is opened. It defaults to `'r'` which means open for reading in text mode (Read more in the official doc).

> [!TIP]
>
> It is good practice to use the `with` keyword when dealing with file objects. The advantage is that the file is properly closed after its suite finishes, even if an exception is raised at some point. Using with is also much shorter than writing equivalent _try-finally_ blocks:
>
> ```py
> with open('workfile', encoding="utf-8") as f:
>     read_data = f.read()
> ```

# Format String

The `str.format()` method and the `Formatter` class share the same syntax for format strings.

## `str.format(*args, **kwargs)`

Perform a string formatting operation.

-   The string on which this method is called can contain _literal text_ or _replacement fields_ delimited by braces `{}`.
-   Each replacement field contains either the numeric index of a positional argument, or the name of a keyword argument.
-   Returns a copy of the string where each replacement field is replaced with the string value of the corresponding argument.

## f-strings

A _formatted string literal_ or _f-string_ is a string literal that is prefixed with 'f' or 'F'. These strings may contain replacement fields, which are expressions delimited by curly braces `{}`.

> [!IMPORTANT]
>
> While other string literals always have a constant value, formatted strings are really expressions **evaluated at run time**.

### Examples:

```python
today = datetime(year=2017, month=1, day=27)
print(f"{today:%B %d, %Y}") # 'January 27, 2017'
# When the equal sign '=' is provided, the output will have the expression text, the '=' and the evaluated value.
print(f"{today=:%B %d, %Y}")
# We can specify the width after color
line = "The mill's closed"
print(f"{line:20}") # "The mill's closed   "
# Reusing the outer f-string quoting type inside a replacement field is permitted:
a = dict(x=2)
print(f"abc {a["x"]} def") # 'abc 2 def'
```
