def fibonacci(num):
    fibonacci = 1
    old = 1
    temp = 0
    while fibonacci <= num:
        if fibonacci == num:
            return True
        fibonacci = temp + old
        temp = old
        old = fibonacci
    return False

num = input('What number do you wanna know wether it\'s a fibonacci number?')

while num.isdigit() == False:
            num = input(f'Plear enter an integer value: ')

isit = fibonacci(int(num))

if isit == True:
    print(f'The number {num} is indeed a fibonacci number!')
else:
    print(f'The number {num} is not a fibonacci number!')