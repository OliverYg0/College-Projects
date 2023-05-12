import random
from calculator2 import Calculator
import os


class Program:
    def __init__():
        # Week 1, assignment 1.8, Task 6,
        A = 33
        B = 200

        if b > a:
            print('B is greater than A')
        elif a > b:
            print('A is greater than B')
            
    # Week 1, assignment 1.8, Task 2, Create variables
    NAME = "Bob"
    NUMBER = 2

    # Week 1, assignment 1.8, Task 5 & 7, Create and store items in a list
    THIS_LIST = ['car', 'boat', 'squirrel']

    running = True

    # Week 2, assignment 2.2 Task 1
    @classmethod
    def run_calculator(cls):
        calculator = Calculator()
        calculator.start()

    @classmethod
    def tea_flow_chart(cls):
        os.system('start tea.jfif')

    @classmethod
    def clear_screen_only_works_in_console(cls):
        os.system('cls')
        cls.menu()

    @classmethod
    def generalisation_and_abstaction(cls):
        print('Once we have recognised patterns in our problems, we use abstraction to gather the general characteristics and to filter out of the details we do not need in order to solve our problem and justfy it.')

    @classmethod
    def sources(cls):
        print('BBC Bitesize.')

    @classmethod
    def pattern_recognition(cls):
        print('Once we have decomposed a complex problem, it helps to examine the small problems for similarities or ‘patterns. These patterns can help us to solve complex problems more efficiently.')

    @classmethod
    def show_variables(cls):
        print('Name:', cls.NAME)
        print('Number:', cls.NUMBER)

    @classmethod
    def decomposition(cls):
        print('''1.	what kind of app you want to create?
2.	what your app will look like
3.	who the target audience for your app is?
4.	what your graphics will look like
5.	what audio you will include
6.	what software you will use to build your app
7.	how the user will navigate your app
8.	how you will test your app
9.	where you will sell your app
''')

    @classmethod
    def show_list(cls):
        for item in cls.THIS_LIST:
            print(item)

    # Week 1, assignment 1.8, Task 4, Calculate equation
    @classmethod
    def calculate_task(cls):
        print(f'(2,452,1230 * 1,291,201) + (252,1230,920.291,239 / 9) = {eval("(2,452,1230*1,291,201)+(252,1230,920.291,239/9)")}')
    
    # Week 1, assignment 1.8, Task 1, Hello world program
    @classmethod
    def hello_world(cls):
        print('Hello world!')

    # Exit the program
    @classmethod
    def exit(cls):
        cls.running = False

    # Method for dynamic automatic updating menu
    @classmethod
    def get_attributes(cls):
        return [attribute for attribute in dir(Program) if callable(getattr(Program, attribute)) and attribute.startswith('__') is False and attribute != 'menu' and attribute != 'get_attributes']
    
    @classmethod
    def menu(cls):
        print('My Colloge Projects')
        print('-------------------\n')

        c = 1

        # Display class functions in a menu
        for method in cls.get_attributes():
            print(c, method.replace('_', ' ').title())

            c += 1

        while cls.running:
            
            # Week 1, assignment 1.8, Task 3, Get user input
            opt = int(input('\n--> '))

            if opt > 0 and opt <= len(cls.get_attributes()):
                func = getattr(Program, cls.get_attributes()[opt - 1])
                func()
                

def main():
    Program.menu()
    

if __name__ == '__main__':
    os.system('color a')
    main()
