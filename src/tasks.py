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
