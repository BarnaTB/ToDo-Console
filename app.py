from src.tasks import *
from src.accounts import *
from utilities import login_func


if __name__ == '__main__':
    while True:
            name = raw_input('Please enter your name here: ')
            password = raw_input('Please enter your password ')

            if password not in accounts:
                add_account(name, password)
                print('A new account was created for you!')
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
                    print('Please enter a selection from the listed options')
            else:
                login_func()
