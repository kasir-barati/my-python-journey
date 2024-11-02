# Installing Python Interpreter

You might wanna ask what is interpreter, in the layman's terms (tell me like i am 5), it is a software that:

1. Takes your python code.
2. Read the first line.
3. Translate it to what computers understand.
4. Execute the translated result.
5. Computer act upon it.
6. It goes to the next line.
7. If there is more code, it repeats steps 3 to 6 until it finishes executing your python code.

![Interpreter as translator](./assets/interpreter-translator.png)

> [!NOTE]
>
> Number systems: binary, octal, decimal, hexadecimal
>
> ![Number systems](./assets/number-systems.png)

## Windows

![Downloading Python for Windows](./assets/win-download-process.png)

After it finished downloading, open the downloaded file.

![Opening file](./assets/open-python-file.png)

Then you must check the option to add python to your path:

![First page of python installer](./assets/first-page-of-python.png)

Allow python installer make changes on your device:

![allow installer to install python](./assets/allow-installer-to-install-python.png)

Confirm python installation:

![Open run](./assets/open-run.png)

Open CMD:

![Open CMD](./assets/open-cmd.png)

Type `python --version` and hit enter:

![Printed python version in terminal](./assets/python-version-in-terminal.png)

# IDE -- VSCode

There might be others who use things like [PyCharm](https://www.jetbrains.com/pycharm/), [Intellij IDEA](https://www.jetbrains.com/idea/).

> [!NOTE]
>
> IDE stands for **I**ntegrated **D**evelopment **E**nvironment.

## Download & installation

1. Download it from [here](https://code.visualstudio.com/).
2. Open it and accept terms of service:

   ![accepting terms of service](./assets/install-vscode-terms-of-service.png)

3. Pick a location on your hard drive if you like, but like I've already suggested in the folowing screenshot, do not change if you do not have any reason to do so and just click on "Next":

   ![VSCode install location](./assets/vscode-install-location.png)

4. ![Click next](./assets/start-menu-vscode.png).
5. Create its icon on desktop if you like, but those two other options will make your life much much easier:

   ![Add some actions to your right click](./assets/add-vscode-to-desktop.png)

6. ![CLick on Install](./assets/install-vscode-page.png)
7. ![alt text](./assets/finished-vscode-installation-page.png)

## Configurations

1.  Choose a theme:

    ![Choose a theme](./assets/vscode-initial-page-choose-theme.png)

2.  Install ["Python"](https://marketplace.visualstudio.com/items?itemName=ms-python.python) extension for VSCode. This will give you stuff like:
    - IntelliSense (Through Pylance extension).
    - Debugging (Through Python Debugger extension).
    - Formatting, linting, code navigation, refactoring, variable explorer, test explorer, and other convenience you might need while coding.

## Create a new python project

1. Create a new directory/folder on your desktop and call it "projects":

   ![alt text](./assets/create-new-folder.png)

2. Open it and inside it create a new directory called "HelloWorld".

   BTW this is a naming convention ![naming conventions](./assets/naming-conventions.png)

3. Open "HelloWorld" with VSCode.

   You can do it inside file explorer:

   ![alt text](./assets/open-with-vscode.png)

   Or through VSCode:

   ![alt text](./assets/open-folder.png)

## Creating a virtual environment

- For your Python projects we need to create what is called virtual environment which is necessary.
- You can have multiple Python project which use different version of Python, thus you cannot every time for every project just reinstall it, right?
- We also might install 3rd party libraries, in which we do not wanna pollute our global environment.

1. Open Command Palette and type "Python create Environment": ![Create venv](./assets/create-venv.png)
2. Press enter.
3. Wait until it is done creating your virtual environment: ![Create venv in process](./assets/create-venv-in-process.png)
4. You can see that now your virtual env is dictating which Python version should be used in that project: ![alt text](./assets/venv-python-version.png)

## VScode shortcut keys

- Press `ctrl + z` to undo your changes. ![ctrl + z](./assets/ctrl-plus-z.png)
- Press `ctrl + y` to redo. ![ctrl + y](./assets/ctrl-plus-y.png)
- Press `ctrl + d` to kill a REPL. ![CTRL+D](./assets/ctrl-plus-d.png)
- Press <code>ctrl + `</code> to open terminal (it is called command prompt in windows): ![ctrl + backtick](./assets/ctrl-plus-backtick.png)
- Press `ctrl + shift + p` to open "command palette". ![ctrl + shift + p](./assets/ctrl-plus-shift-plus-p.png).

  - Here we can do things like opening a REPL: ![repl](./assets/repl.png)

# Final words

Do not be afraid of reading docs. I wanna show you how you could accomplish same results by just reading VSCode's official documentations:

1. Install VSCode on windows: search in google "Install VSCode on Windows".
2. How to configure newly installed VSCode for Python in Windows: Search in Google: "VSCode + windows + python".
3. How to know which short cut does what in VSCode. Google "VSCode shortcuts" or "VSCode shortcuts cheat sheet".
