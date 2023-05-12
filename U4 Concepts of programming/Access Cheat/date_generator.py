import random
import string


def postcodes(amount):
    postcodes = []

    for _ in range(amount):
        postcodes.append(''.join(random.choice(string.ascii_uppercase) for _ in range(3)) + str(random.randint(000, 999)))

    return postcodes


def phone_numbers(amount):
    numbers = []

    for _ in range(amount):
        numbers.append('07' + str(random.randint(000000000, 999999999)))

    return numbers


def dates(amount):
    dates = []

    for _ in range(amount):
        month = str(random.randint(1, 12))

        if len(month) == 1:
            month = '0' + month
        
        dates.append(str(random.randint(1, 30)) + '/' + month + '/' + str(random.randint(2000, 2021)))
 
    return dates

def datetimes(amount):
    dates = []

    for _ in range(amount):
        dates.append(str(random.randint(1, 30)) + '/' + str(random.randint(1, 12)) + '/2021 ' + str(random.choice([0, 30])) + ':' + str(random.randint(1, 24)) + ':0')
 
    return dates


def addresses(amount):
    with open('words.txt', 'r') as words:
        words = list(words)
        addresses = []

        for _ in range(amount):
            address = f'{str(random.randint(1, 300))} {random.choice(words)}'
            address = address.title()
            addresses.append(address.strip().replace('\n', ''))

        return addresses

def activities(amount):
    return [random.choice(['Swimming', 'Basketball', 'Gym Session', 'MMA', 'Boxing', 'Kick Boxing', 'Judo']) for _ in range(amount)]


def prices(amount):
    prices = []

    for _ in range(amount):
        prices.append('£' + str(random.randint(20, 50)) + '.' + str(random.randint(0, 99)))

    return prices


def menu():
    print('1. Generate postcodes')
    print('2. Generate phone numbers')
    print('3. Generate dates')
    print('4. Generate addresses')
    print('5. Generate prices')
    print('6. Generate datetimes')
    print('7. Activities')
    print('8. Exit')

    opt = 0

    while opt != '5':
        opt = input('\n--> ').strip()
        amount = int(input('Amount: '))

        if opt == '1':
            for postcode in postcodes(amount):
                print(postcode)
        elif opt == '2':
            for number in phone_numbers(amount):
                print(number)
        elif opt == '3':
            for date in dates(amount):
                print(date)
        elif opt == '4':
            for addr in addresses(amount):
                print(addr)
        elif opt == '5':
            for price in prices(amount):
                print(price)
        elif opt == '6':
            for datetime in datetimes(amount):
                print(datetime)
        elif opt == '7':
            for activity in activities(amount):
                print(activity)
        elif opt == '8':
            exit()
        else:
            print('Invalid')
            
menu()
