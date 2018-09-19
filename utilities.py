from src.tasks import *
from src.accounts import *


def login_func():
    print('Please select what you want to do!')
    print('1. Add a task')
    print('2. Delete a task')
    print('3. Delete all tasks')
    print('4. Mark a task as finished')

    selection = raw_input('Your selection: ')
    if selection == '1':
        task = raw_input('Please enter your task here:')
        create_task(task)
    elif selection == '2':
        print(todo_list)
        task = raw_input('Please enter the task you want to delete here: ')
        delete_task(task)
    elif selection == '3':
        delete_all_tasks()
    elif selection == '4':
        print(todo_list)
        task = raw_input('Please enter the task you want to finish: ')
        mark_as_finished(task)
    else:
        print('Please a selection from the listed options')
