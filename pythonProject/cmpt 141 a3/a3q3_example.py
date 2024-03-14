# Will Bushell, abc123, 12345678, Jeffrey Long
# this is designed to help with question 3 of A3

def rock_paper_scissors(p1, p2):
    if p1 == p2:
        return 2    # 2 = tie
    if p1 == 'r' and p2 == 's':
        return 1    # 1 == player 1 win
    if p1 == 'p' and p2 == 'r':
        return 1
    if p1 == 's' and p2 == 'p':
        return 1
    else:
        return 3    # if player 1 doesnt win, and they are not equal, then player 2 must have won
    
player1 = input("(Player 1) Enter Rock, Paper, or Scissors [r/p/s] ")
player2 = input("(Playert 2) Enter Rock, Paper, or Scissors [r/p/s] ")

if rock_paper_scissors(player1, player2) == 1:
    print("Player 1 wins! hurrah!")
elif rock_paper_scissors(player1, player2) == 2:
    print("It was a tie.")
else:
    print("Player 2 wins! yippee!")