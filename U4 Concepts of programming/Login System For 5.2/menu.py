from app import App

GRADES = {
    'required': {
        'maths': 4,
        'english': 4,
        'computer science': 4
    },
    'users': {
        'maths': None,
        'english': None,
        'computer science': None
    }
}


def required_grades():
    required = True

    if GRADES['users']['maths'] < GRADES['required']['maths']:
        required = False

    if GRADES['users']['english'] < GRADES['required']['english']:
        required = False

    if GRADES['users']['computer science'] < GRADES['required']['computer science']:
        required = False

    return required


def teacher_gone():
    choice = None

    while choice != 'y' or choice != 'n':
        choice = input('\nIs the teacher gone (Y/N): ').strip().lower()

        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print('Enter \'y\' or \'n\'.')


def check_interest():
    choice = None

    while choice != 'y' or choice != 'n':
        choice = input('Are you interested in computer science (Y/N): ').strip().lower()

        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print('Enter \'y\' or \'n\'.')


def get_grades():
    GRADES['users']['maths'] = int(input('\nMaths grade: '))
    GRADES['users']['english'] = int(input('English grade: '))
    GRADES['users']['computer science'] = int(input('Computer Science grade: '))


def menu():
    running = True

    while running:
        print('1. Login')
        print('2. Register')
        
        opt = input('\n--> ')

        username = input('\nUsername: ')
        password = input('Password: ')

        if opt == '1':
            if App.login(username, password):
                print('Logged in.')

                if teacher_gone():
                    print('Go on your phone for abit.')
                else:
                    print('You can still go on your phone for abit.')
        elif opt == '2':
            if check_interest():
                get_grades()

                if required_grades():
                    print('\n' + App.register(username, password) + '\n')
                else:
                    print('\nYou grades are to low.\n')
            else:
                print('\nYour not even interested.\n')


if __name__ == '__main__':
    menu()