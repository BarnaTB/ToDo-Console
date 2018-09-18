todo_list = []


def create_task(task):
    if not task or task.isspace():
        print('Please enter a task')
    if not task.isalnum():
        print('A task should be a string')
    todo_list.append(task)
    print('Your list: {0}'.format(todo_list))
    return todo_list


def delete_task(task):
    for a_task in todo_list:
        if a_task == task:
            todo_list.remove(task)
            print(todo_list)
            return todo_list
        print('That task does not exist in this list.')
