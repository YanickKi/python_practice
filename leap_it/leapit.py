leap = False

INPUT = input('What year do you wanna know wether it\'s a leap year?')
while INPUT.isdigit() == False:
            INPUT = input(f'Plear enter an integer value as a year: ')

INPUT = int(INPUT)

if INPUT % 4 == 0 and INPUT % 100 != 0 or INPUT % 400 == 0:
    leap = True

if leap == True:
    print(f'The year {INPUT} is indeed a leap year!')
else:
    print(f'The year {INPUT} is not a leap year.')