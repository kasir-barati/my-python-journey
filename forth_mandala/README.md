# Working with file system

-   If you just pass the file name and do not specify the file path, it will save the file inside the current directory that `python3` command gets executed.
    ```py
    my_file = open("new-file.md", "w", encoding="utf8")
    message = "This is Kasir, talking to you from his own VSCode."
    my_file.write(message)
    ```
    -   The first parameter is:
        -   file name: `open("new-file.md", "w", encoding="utf8")`
        -   full path to file: `open("/tmp/new-file.md", "w", encoding="utf8")`
    -   The second parameter is the mode, python wanna know how do you wanna work with the file?
        -   `w`: Write into it and if file exists override it
        -   `r`: Just read file
        -   `a`: to append to file
        -   There are other flags too but I do not have time to go through all of them

# Installing pip

-   Follow the [specified instruction in the official doc](https://pip.pypa.io/en/stable/installation/)
-   I used `get-pip.py`
    ```cmd
    $ wget https://bootstrap.pypa.io/get-pip.py
    $ python3 get-pip.py
    Defaulting to user installation because normal site-packages is not writeable
    Collecting pip
      Downloading pip-22.1.2-py3-none-any.whl (2.1 MB)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 506.5 kB/s eta 0:00:00
    Collecting wheel
      Downloading wheel-0.37.1-py2.py3-none-any.whl (35 kB)
    Installing collected packages: wheel, pip
    Successfully installed pip-22.1.2 wheel-0.37.1
    $ python3 -m pip install --upgrade pip setuptools wheel
    ```
    -   What is wheel?
        -   It is how pip installs Python modules from the Python Package Index (PyPI) splits to two branches:
            -   Source Distributions (sdist)
            -   Wheels (whl).
        -   According to the Python Packaging Authority (PyPA), **wheels are the preferred way** because they’re
            -   smaller to install.
            -   faster to install.
            -   More efficient than building the package from the source code.
            -   Easier for newcomers to install packages.
    -   Last command to make sure we have latests. In my own experience it also installed `setuptools`.
        -   What is setuptools?
            -   A group of improvements to the Python distutils that allow us to easily build and share Python distributions.
-   Seeing an output like this after running ` python3 -m pip -V` or `pip3 --version` would be a good validation that everything is installed correctly.
    ```cmd
    pip 22.1.2 from /home/kasir/.local/lib/python3.10/site-packages/pip (python 3.10)
    ```
-   Publishing your own modules
    -   `pip install my_library`
    -   PyPI does not support publishing private packages.

# Install new packages with pip

-   The package installer for Python. I guess the successor of npm
-   Many Python projects use `requirements.txt` files, to specify the list of packages that need to be installed for the project to run.
-   A bundle of software to be installed
-   Install packages from the [Python Package Index](https://pypi.org/) and other indexes.
    -   What is index?
        -   A repository of softwares for the Python programming language.
        -   You can find and install softwares developed and shared by the Python community.
        -   There are more than 200,000 package in it.
-   A list of well accepted 3rd party packages
    -   NumPy: Scientific computing in Python.
    -   Requests: sends HTTP requests
    -   Pytest: unit test or a more complex functional test
    -   Python Imaging Library: Pillow, or PIL works with images
    -   Pendulum: Makes our life easier to work with datetime, especially that it handles timezone which makes it IMO a great Sweetzer knife since dealing with timezone is a painful task.
    -   urllib3: user-friendly HTTP client
    -   Matplotlib: Data exploration and visualization library
    -   pandas
    -   MoviePy: Working with video files
    -   PyQt: building GUIs
    -   NLTK: natural language processing
-   "package" used in this context serves as a synonym for a distribution. A distribution is a collection of packaged software that includes all of the modules and other resources needed to install and run a Python package.
-   With PIP, we can use either:
    -   A virtual environment to test out programs
        -   Usually we stick to this option
        -   Do not pollute your dev python env
    -   Use it in a global setting on a server.

# Create a virtual environment

-   **Note:** They are just meant to be and environment for my project's packages and dependencies. Not for my project. I mean nobody wanna build their app inside these virtual envs.
-   venv
    -   `python3 -m venv forth_mandala`
    -   Packages installed in an isolated location for `forth_mandala` application, rather than being installed globally.
    -   I just gave up from this option for now
-   [Virtualenv](https://virtualenv.pypa.io/en/stable/index.html)
    -   A way to separate different project envs from each other
    -   Create isolated Python environments
    -   It has been integrated into the standard library
    -   `pip3 install virtualenv`
    -   `virtualenv project_name`
    -   `source project_name/bin/activate` to activate the isolated env.
        -   `which python3` should show you a path to your local env
    -   `pip3 freeze --local > requirements.txt` to generate requirements.txt which based on my observation is the equivalent of `package.json`
    -   To get out of your virtual env you can issue `deactivate` in the terminal
    -   Create a env with a specific python version `pip3 -p /usr/bin/python2.6 app_name`
    -   To install packages using `requirements.txt` we can do this: `pip3 install -r requirements.txt`
