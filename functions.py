FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):  # default parameter, we can still use this function to open different files
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

# print(help(get_todos))


def write_todos(todos_arg, filepath=FILEPATH):  # non-default parameter should be placed before default parameters
    """ Write the to-do items list in the text file """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__": # it appears only when we run functions code
    print("hello from functions")

# if __name__ == "__current_file__", it executes only if we run current file
