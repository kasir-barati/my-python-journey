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
