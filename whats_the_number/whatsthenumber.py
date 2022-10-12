import random

mistake = 0 #COUNTING FAILED GUESSES ON CURRENT RANDOM NUMBER
tries   = 2 #NUMBER OF TRIES PER RANDOM NUMBER
MAX     = 10 #MAXIMUM NUMBER TO GUESS

print('Welcome to What\'s the number?')

num = random.randint(0,MAX)

while True:
    INPUT = input('What\'s the number?:')
    if INPUT.isdigit() == False or int(INPUT) > MAX:
        print(f'Input must be an integer and smaller than {MAX+1}')
    elif int(INPUT) == num:
        print('HURRA')
        mistake = 0
        num = random.randint(0,MAX)
    else:
        print(f'The number is off by {abs(int(INPUT) - num)}')
        mistake = mistake + 1
        if mistake == tries:
            print('Loose! Next random number')
            mistake = 0
            num = random.randint(0,MAX)