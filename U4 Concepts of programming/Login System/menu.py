from app import App


def menu():
    running = True

    while running:
        print('1. Login')
        print('2. Register')
        
        opt = input('\n--> ')

        username = input('\nUsername: ')
        password = input('Password: ')

        if opt == '1':
            print('\n' + App.login(username, password) + '\n')
        if opt == '2':
            print('\n' + App.register(username, password) + '\n')


if __name__ == '__main__':
    menu()