memory = []

print("Type 'm' to see memory.")

while True:
    calc = input('\n--> ')

    if calc.lower().strip() == 'm':
        for e in memory:
            print('\nEquation:', e[0])
            print('Answer:  ', str(e[1]) + '\n')
    else:
        answer = eval(calc)
        print(answer)
        memory.append((calc, answer))
