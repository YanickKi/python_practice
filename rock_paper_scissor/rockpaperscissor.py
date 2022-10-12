import random

moves = {'rock': 0, 'paper': 1, 'scissors': 2}
score = 0
play = 0

print('Welcome to rock, paper, scissors!')

while play >= 0:
    if play == 0:
        play = input('How many rounds do you want to play? ')
        while play.isdigit() == False:
            play = input(f'Input must be an integer \n Please, enter the number rounds you want to play: ')
    play = int(play)
    if play == 0:
        print(f'Thanks for playing! Your final score is {score} points.')
        break
    move = input('Your move: ')
    while move not in moves: 
        move = input('Typo? Your move: ')
    rand = random.randint(0,2)
    if moves[move] == rand:
        print('draw')
    elif moves[move] == 0 and rand == 1 or moves[move] == 1 and rand == 2 or moves[move] == 2 and rand == 0:
        print('lose')
        score = score - 1
    else:
        print('win')
        score = score + 1

    print(f'Your score: {score}')

    play = play - 1