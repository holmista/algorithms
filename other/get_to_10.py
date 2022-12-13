from random import randint

def roll_dice():
    return randint(1, 6)

def get_to_10():
    total = 0
    rolled_amount = 0
    while True:
        current_roll = roll_dice()
        rolled_amount+=1
        total += current_roll
        if total == 10:
            return rolled_amount
        elif total > 10:
            total -= current_roll


def average_rolls(tries):
    roll_amounts = []
    for i in range(0, tries):
        roll_amounts.append(get_to_10())
    return sum(roll_amounts)/tries

print(average_rolls(10_000))





