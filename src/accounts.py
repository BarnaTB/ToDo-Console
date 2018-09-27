accounts = {}


def add_account(name, password):
    """
    Function enables user to create an account on the application using their
    name and password after which they are logged in.

    :param name:
    name takes the value of the user's name.

    :param password:
    password takes the value of the user's password

    :returns:
    A dictionary of registered users.
    """
    if not name.isalpha():
        print('A name should only contain alphabetical characters!')
    else:
        accounts[password] = name
        print(
            ':::::::::::: {} was registered successfully ::::::::::::'.format(name)
            )
        return accounts
