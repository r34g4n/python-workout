import random

number = random.randint(0, 100)


def guessing_game():
    guess = input('Guess the number (Clue: it\'s between 0 and 100 inclusive): ')
    try:
        guess = int(guess)
    except ValueError:
        print('You either typed a string or typed nothing.Try again!')
        return guessing_game()
    if guess > number:
        print('Too high')
        return guessing_game()
    elif guess < number:
        print('Too low')
        return guessing_game()
    else:
        print('Just right')


guessing_game()
