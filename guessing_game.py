import random

print('Game starting...')
print('HOW TO PLAY: Try to guess the computers number, it will tell you if is high or low.')


computer_number = random.randint(1, 100)
print(computer_number)
user_guess = 0

guesses = 0
max_guesses = 5

while guesses < max_guesses:
    user_guess = int(input('Guess a number (1,100): '))
    guesses +=1

    if user_guess < computer_number:
        print('Higher')
    elif user_guess > computer_number:
        print('Lower')
    else:
        print(f'Correct! It took you {guesses} guesses')
        break
if user_guess != computer_number:
    print('You lost! The number was', computer_number)