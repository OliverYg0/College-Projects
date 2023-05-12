import sqlite3
import hashlib


def create_db():
    con = sqlite3.connect('db.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS users (usernames text, passwords text)''')
    con.commit()
    con.close()


def show_all():
    con = sqlite3.connect('db.db')
    cur = con.cursor()

    for user in list(cur.execute('''SELECT * FROM users''')):
        print(user)
        
    con.close()


class App:
    logged_in = False
    user = None
    salt = 'g1FqplkXVk4BOVWcc3zbJHph5ZiAhhzz9SuTou6DPzeQRYoU2HvAUWkue1v9ox9cF'
    hash_amount = 1072415
    add_salt_at = 57
    db_file = 'db.db'
    table_name = 'users'

    @classmethod
    def login(cls, username, password):
        create_db()

        con = sqlite3.connect(cls.db_file)
        cur = con.cursor()

        if (username, cls.encrypt_password(password)) in list(cur.execute('SELECT * FROM users')):
            return 'Logged in.'
        else:
            return 'User does not exist or password is incorrect.'

    @classmethod
    def encrypt_password(cls, password):
        for i in range(cls.hash_amount):
            
            if i == cls.add_salt_at:
                password += cls.salt

            password = hashlib.sha512(password.encode()).hexdigest()

        return password

    @classmethod
    def check_for_user(cls, username):
        create_db()

        con = sqlite3.connect(cls.db_file)
        cur = con.cursor()

        if (username,) in list(cur.execute(f'SELECT usernames FROM {cls.table_name}')):
            con.close()

            return True
        else:
            con.close()

            return False

    @classmethod
    def register(cls, username, password):
        create_db()

        if not cls.check_for_user(username):
            con = sqlite3.connect(cls.db_file)
            cur = con.cursor()

            # cur.execute(f'''INSERT INTO {cls.table_name} VALUES ({username}, {cls.encrypt_password(password)})''')
            cur.execute('INSERT INTO users (usernames, passwords) VALUES (?, ?)', (username, cls.encrypt_password(password)))
            con.commit()  

            con.close()

            return '[ADDED] User added to the db.'
        else:
            return '[DENIED] User already exists.'


def main():
    # create_db()
    show_all()


if __name__ == '__main__':
    main()
