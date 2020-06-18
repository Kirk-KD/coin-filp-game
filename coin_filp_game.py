from random import randrange

heads = 0
tails = 0
count = 0

while count < 2:
    coin = randrange(2)

    if coin == 0: heads += 1
    else: tails += 1

    count += 1


print(f'Heads: {heads}\nTails: {tails}\n')
input('Enter to exit')
