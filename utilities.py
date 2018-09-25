from src.tasks import *
from src.accounts import add_account


def prompts():
    """
    Function logs in  a user to their account and grants them access to other
    resources.
    """
    print('************ Select what you wish to do ************')
    print('1. Add a task')
    print('2. Delete a task')
    print('3. Delete all tasks')
    print('4. Mark a task as finished')


def login_func():
    """
    Function logs in  a user to their account and grants them access to other
    resources.
    """
    prompts()

    selection = input('Your selection: ')
    if selection not in ['1', '2', '3', '4']:
        print('Please a selection from the listed options')
    if selection == '1':
        task = input('Please enter your task here:')
        create_task(task)
    if selection == '2':
        print(todo_list)
        task = input('Please enter the task you want to delete here: ')
        delete_task(task)
    if selection == '3':
        delete_all_tasks()
    if selection == '4':
        print(todo_list)
        task = input('Please enter the task you want to finish: ')
        mark_as_finished(task)


def register_func(name, password):
    """
    Function registers a user using their name and password.

    :param name:
    Holds the name of the user from their input.

    :param password:
    Holds the password from their input
    """
    add_account(name, password)
    prompts()

    selection = input('Your selection: ')
    if selection not in ['1', '2', '3', '4']:
        print('Please enter a selection from the listed options')
    if selection == '1':
        task = input('Please enter the task here: ')
        create_task(task)
    if selection == '2':
        print(todo_list)
        task = input('Please enter the task you want to delete here: ')
        delete_task(task)
    if selection == '3':
        delete_all_tasks()
    if selection == '4':
        print(todo_list)
        task = input('Please enter the task you want to finish: ')
        mark_as_finished(task)
