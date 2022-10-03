def who_win(player):
    if player == "rock":
        print("player 1 is winner")
    elif player == "paper":
        print("player 2 is winner")
    else:
        print("you give wrong information")

name = input()
who_win(name)
