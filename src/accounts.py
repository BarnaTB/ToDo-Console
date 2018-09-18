accounts = {}


def add_account(name, password):
    if not name.isalpha():
        print('A name should only contain alphabetical characters!')
    else:
        accounts[password] = name
        print(
            '{} is registered. Go ahead and login'.format(accounts[password])
            )
        return accounts


def login(name, password):
    for key in accounts:
        if key == accounts[password]:
            return True
        return False
