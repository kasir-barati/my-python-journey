# Whetting Your Appetite

- There are some tasks that you'd like to automate. E.g.:

  - Rename and rearrange a bunch of photo files in a complicated/simple way.

    ![Renaming files](./assets/renaming-files.png)

  - Or search and replace over a large number of text files.

    ![Replace functionality in microsoft office word](./assets/office-word-replace.png)

- Do not like write/compile/test/re-compile cycle.

  ![Code, compile, run, test cycle](./assets/code-compile-run-test-cycle.png)

  This can save us the precious little time we've got ;).

We can do all of these things with Python.

> [!TIP]
>
> Wanna learn coding in Python. You can go and read their standard modules. It can give you a very good sense of direction and how you should think when you develop an app.

> [!TIP]
>
> Whenever you got stuck somewhere go and chat with Generative AI tools. E.g. [ChatGPT](https://chatgpt.com/).

## Python REPL

Use it:

- To experiment with features of the language.
- To write throw-away programs.
- To test functions during bottom-up program development.
- As a handy desk calculator :|.

![Learn by doing](./assets/doing-learning.png)

## The road ahead us

1. Simple expressions.
2. Statements and data types.
3. Functions and modules.
4. Exceptions and user-defined classes.

## Ref

- [https://docs.python.org/3/tutorial/appetite.html#whetting-your-appetite](https://docs.python.org/3/tutorial/appetite.html#whetting-your-appetite).

## YouTube/Aparat

- [https://aparat.com/v/xlw508e](https://aparat.com/v/xlw508e).
- [https://youtu.be/oQrnW7QbZNE](https://youtu.be/oQrnW7QbZNE).

## Invoking the Interpreter

- We talked about how to install Python [here](../01-intro/README.md#installing-python-interpreter).
- And we know how to run it thanks to our [first exposure to VSCode](../01-intro/README.md#ide----vscode).
- Exit from interpreter using end-of-file character:
  - `Ctrl + d` on Unix, `ctrl + z` on Windows.
  - Or just type `quit()`.
- In REPL we have:

  - Code completion.

    - On Windows you need to install `pyreadline3`: `python -m pip install pyreadline3` ([ref](https://stackoverflow.com/a/71186211/8784518)).

    ![Code completion](./assets/code-completion.gif)

  - history substitution.

    ![history substitution](./assets/history-substitution.gif)

- Operates somewhat like the Unix shell:

  - Called with standard input connected to a tty device? It reads and executes commands interactively.

    ![Python hello in REPL](./assets/python-hello-in-repl.gif)

  - Called with a file name argument or with a file as standard input, it reads and executes a script from that file.

    ![Python executes a script](./assets/python-executes-a-script.gif)

  - Use `-c` flag to tell python interpreter that it needs to run the specified code:

    ![python interpreter -c flag](./assets/pytho-interpreter--c.png)

- Commands are read from a [tty](./glossary.md#teletypewritersDefinition).
- Primary prompt: `>>>`.
- Secondary prompt/Continuation lines: `...`.

![Continuation lines and primary prompt](./assets/continuation-line-primary-prompt.png)

- Python source files are treated as encoded in UTF-8 ([learn more about encoding](https://github.com/kasir-barati/html-css/blob/main/01-html/README.md#charset)).

  ```py
  # -*- coding: encoding -*-
  ```

  You can see a list of them [here](https://docs.python.org/3/library/codecs.html#standard-encodings).

## YouTube/Aparat

- [https://youtu.be/ltUwClOB60o](https://youtu.be/ltUwClOB60o).
- [https://aparat.com/v/oqzh038](https://aparat.com/v/oqzh038).

## Ref

- [https://docs.python.org/3/tutorial/interpreter.html](https://docs.python.org/3/tutorial/interpreter.html).

## How computer memory works

- Our memory defines us.
  - You're past exps.
  - Know-hows.
  - etc.
- Computers are the same in that regard.
- In computers everything takes the form of what is commonly referred to as **bits**.

### Bit

- Stands for **b**inary dig**it**.
  ![Binary digit](./assets/bit-stands-for-binary-digit.png)
- Can switch between 0 and 1.
- Every file/software consist of millions of these bits.
- Each one of them is stored in a [memory cell](./glossary.md#memoryCellDefinition).

### CPU -- Central Process Unit

- Computer's brain.
- Process bits.

  ![CPU processes bits from memory](./assets/cpu-processing-bits.png)

- The amount of bits needs to be processed grows. Thus the need to always even in the modern era to optimize your software.

### Short-term memories

- Needs to be fast, thus we can access any place of the memory in any order.
- When we run a program CPU allocates memory to that program in short-term memory to run that program.
- E.g. When you open a movie it needs to process bits of data and tell your monitor what to do. In order to do that it needs to put your video's info somewhere withing reach and that somewhere is short-term memories.
- Used to store data just for a short period of time.
- Cut of the power supply (electricity) and your data is gone.
- Categories:
  - DRAM -- Dynamic Random Access Memory.
  - Cache -- Internal cache inside CPU made up from SRAM (Static RAM).

### Long term memories

- Most well know ones:

  - Optical base storages:
    - DVD -- Digital Versatile Disc.
    - CD -- Compact Disc.
  - HDD -- Hard Disk Driver.

    - Magnetic storage.

      ![Magnetic storage](./assets/magnetic-storage.png)

  - SSD -- Solid State Drive.
    - USB hard disk driver.

- Used to store data permanently.
- Turn off the computer and turn it back on the next day it still has the data.

### Memory latency

- The time it takes for the bits to be transferred from memory to CPU.

  ![Data from memory to CPU and vice versa](./assets/memory-latency.png)

### Digital storage terminology

![Byte is 8 bits put together](./assets/byte.png)

- Byte is 8 bits put together.
- The space necessary to store 1 character (letter/number/symbol).

![Kilobyte is 1000 bytes put together](./assets/kilobyte.png)

- Kilobyte is 1000 bytes put together.
- Enough to store one third of a page.

> [!NOTE]
>
> Digital storage uses the binary system, thus everything needs to be in powers of two.

![Megabyte](./assets/megabyte.png)

- 1000 Kilobytes.
- Roughly enough to store one book, one photo, or 1 minute of music.

![Gigabyte](./assets/gigabyte.png)

- 1000 Megabyte.
- Enough for 1000 books.

## Ref

- [How computer memory works - Kanawat Senanan](https://youtu.be/p3q5zWCw8J4?si=th34ctRMV0u3Yrob).
- [Computer Skills Course: Bits, Bytes, Kilobytes, Megabytes, Gigabytes, Terabytes (UPDATED VERSION)](https://youtu.be/u4P0LOofEFs?si=bnNIyTUaRmWWvZQn).
