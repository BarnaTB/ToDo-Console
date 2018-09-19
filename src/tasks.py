todo_list = []


def create_task(task):
    """Function enables user to add a task to a to-do list"""
    if not task or task.isspace():
        print('Please enter a task')
    if not task.isalnum():
        print('A task should be a string')
    todo_list.append(task)
    print('Your list: {0}'.format(todo_list))
    return todo_list


def delete_task(task):
    """Function enables a user to delete a specific task from a to-do list"""
    for a_task in todo_list:
        if a_task == task:
            todo_list.remove(task)
            print(todo_list)
            return todo_list
        print('That task does not exist in this list.')


def mark_as_finished(task):
    """Function enables user to mark a task as finished"""
    for a_task in todo_list:
        if a_task == task:
            finished_task = "{0} -finished".format(a_task)
            todo_list.remove(a_task)
            todo_list.append(finished_task)
            print(todo_list)
            return todo_list
        print('This task does not exist in your list')


def delete_all_tasks():
    """Function to delete all tasks from a to-do list"""
    todo_list.clear()
    print(todo_list)
    return todo_list
