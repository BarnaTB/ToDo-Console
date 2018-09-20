from src.accounts import *
from utilities import login_func, register_func


if __name__ == '__main__':
    while True:
        name = input('Please enter your name here: ')
        password = input('Please enter your password ')
        if password not in accounts:
            register_func(name, password)
        else:
            login_func()
