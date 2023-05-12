

class Calculator:
    def __init__(self):
        self.memory = []
        self.running = False

    def display_memory(self):
        for e in self.memory:
            print('\nEquation:', e[0])
            print('Answer:  ', str(e[1]) + '\n')

    def calculate(self, calc):
        answer = eval(calc)
        self.memory.append((calc, answer))
        print(answer)

    def process_input(self, user_input):
        if user_input.lower().strip() == 'm':
            self.display_memory()
        else:
            self.calculate(user_input)

    def start(self):
        self.running = True

        print("Type 'm' to see memory.")
        
        while self.running:
            user_input = input('\n--> ')
            self.process_input(user_input)


def main():
    calculator = Calculator()
    calculator.start()
    

if __name__ == '__main__':
    main()
