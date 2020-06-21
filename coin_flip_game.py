
from random import randint  # import randint from random

# define counts of heads, tails and games played
heads = 0
tails = 0
count = 0

# flip a coin, win if result == guess, else lose
def filp(guess):

    # if a random int between 0 and 1 is 0, res = heads
    # else res = tails
    res = 'heads' if randint(0, 1) == 0 else 'tails'

    # access heads, tails and count from globle scope
    global heads, tails, count

    # add 1 to heads count if res is head
    # else add 1 to tails count
    if res == 'heads':
        heads += 1
    else:
        tails += 1

    # add 1 to games count
    count += 1

    # print the result and win/lose
    print(f'Flipped: {res}. ', end='')
    print('You win!' if guess == res else 'You lose.')

# print out 'game over' and the counts of heads, tails and games played
# then quit the program
def end_game():
    print('\nGame over.')
    print(f'Heads: {heads}\nTails: {tails}\nGames played: {count}')
    quit()


# run the game
def play_game():
    print('Type x to exit.')

    while True:  # keeps running

        # get input from player
        guess = input('\nType heads or tails: ')

        # if guess is heads or tails, flip the coin and show the result
        if guess in ('heads', 'tails'):
            filp(guess)
        elif guess == 'x':  # end the game if guess is 'x'
            end_game()
        else:
            print('Type heads/tails/x only.')

play_game()  # start the game