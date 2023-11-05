# we set the default value of the filepath as it is the same file.
# however this would be overriden by the parameters during the call if any
def get_todos(filepath="todos.txt") -> object:
    '''
    Return the lines of a file as a list
    :param filepath: picks up the file in this path
    :return: returns the lines in the file as a list
    '''
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todo_arg, filepath="todos.txt"):
    '''
    Writes todos to a file
    :param todo_arg: picks up the todo list
    :param filepath: picks up the file in this path
    '''
    with open(filepath, 'w') as file:
        file.writelines(todo_arg)


# the below lines would work when we try to execute locally
# these function would not work when other modules calls this function
if __name__ == "__main__":
    print("Hello!")
