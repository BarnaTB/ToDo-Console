todo_list = []


def create_task(task):
    """
    Function adds a task to a to-do list using user input as
    the task.

    :param task:
    Holds the task from user input which is then added to the to-do list.

    :returns:
    Returns the to-do list with the added task
    """
    if task == '':
        print('You cannot enter an empty task!')
    if task in todo_list:
        print('This task already exists!')
    todo_list.append(task)
    print(todo_list)


def delete_task(task):
    """
    Function deletes a specific task from the to-do list.

    :param task:
    Holds the task entered by the user which is to be deleted.

    :returns:
    A new list without the deleted task.
    """
    for a_task in todo_list:
        if a_task == task:
            task_position = todo_list.index(task)
            del todo_list[task_position]
            print(todo_list)
        else:
            print('That task does not exist in this list.')


def mark_as_finished(task):
    """
    Function marks a task as finished.

    :param task:
    Holds the task to entered by the user to be marked as finished.

    :returns:
    Returns to-do list with finished task.
    """
    for a_task in todo_list:
        if a_task == task:
            finished_task = "{0} -finished".format(a_task)
            todo_list.remove(a_task)
            todo_list.append(finished_task)
            print(todo_list)
        print('This task does not exist in your list')


def delete_all_tasks():
    """
    Function to delete all tasks from a to-do list
    
    :returns:
    Empty to-do list
    """
    del todo_list[:]
    print(todo_list)
