from src.accounts import accounts
from utilities import login_func, register_func

name = input('Please enter your name here: ')
password = input('Please enter your password: ')


def authenticate():
    """
    Function authenticates a user by checking if they are already registered
    which then runs login functionality, else it registration functionality.
    """
    if password not in accounts:
        register_func(name, password)
    else:
        login_func()


if __name__ == '__main__':
    while True:
        authenticate()
