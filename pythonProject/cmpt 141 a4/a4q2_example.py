# Will Bushell, abc123, 12345678, Jeffrey Long
# this is designed to help with question 2 of A4

import random as r

def rolldice(dice):
    sum = 0
    for i in range(dice):
        roll = r.randint(1,6)
        sum += roll
    return sum

def playgame(dice1, dice2):
    p1power = rolldice(dice1)
    p2power = rolldice(dice2)
    return p1power > p2power

simulations = 1000000
p1wins = 0
p1dice = int(input("How many dice does Player 1 have? "))
p2dice = int(input("How many dice does Player 2 have? "))

for i in range(simulations):
    if playgame(p1dice, p2dice):
        p1wins = p1wins + 1

print("With Player 1 having", p1dice, "dice against Player 2 with", p2dice, "dice,")
print("Player1 won", p1wins, "out of", simulations,
      "games (", p1wins/simulations*100.0, "%)" )

