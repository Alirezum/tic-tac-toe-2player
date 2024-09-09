import os
import time

board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
player = 1

# Win Flag
win = 1
draw = -1
running = 0
stop = 1

game = running
mark = "X"


def drawBoard():
    print(" %c | %c | %c " % (board[1], board[2], board[3]))
    print("---|---|---|")
    print(" %c | %c | %c " % (board[4], board[5], board[6]))
    print("---|---|---|")
    print(" %c | %c | %c " % (board[7], board[8], board[9]))
    print("---|---|---|")


def checkPosition(x):
    if board[x] == " ":
        return True
    else:
        return False


def checkWin():
    global game

    if board[1] == board[2] and board[2] == board[3] and board[1] != " ":
        game = win
    elif board[4] == board[5] and board[5] == board[6] and board[4] != " ":
        game = win
    elif board[7] == board[8] and board[8] == board[9] and board[7] != " ":
        game = win
    elif board[1] == board[4] and board[4] == board[7] and board[1] != " ":
        game = win
    elif board[2] == board[5] and board[5] == board[8] and board[2] != " ":
        game = win
    elif board[3] == board[6] and board[6] == board[9] and board[3] != " ":
        game = win
    elif board[1] == board[5] and board[5] == board[9] and board[5] != " ":
        game = win
    elif board[3] == board[5] and board[5] == board[7] and board[5] != " ":
        game = win
    elif (
        board[1] != " "
        and board[2] != " "
        and board[3] != " "
        and board[4] != " "
        and board[5] != " "
        and board[6] != " "
        and board[7] != " "
        and board[8] != " "
        and board[9] != " "
    ):
        game = draw
    else:
        game = running


print("Welcome Tic-Tac_Toe ")
print("Player 1 [X] --- Player 2 [O]\n")
print()
print()
print("Please wait...")
time.sleep(3)

while game == running:
    os.system("clear")
    drawBoard()

    if player % 2 != 0:
        print("Player 1's chance")
        mark = "X"
    else:
        print("Player 2's chance")
        mark = "O"

    choice = int(input("Enter your position between [1-9] where you want to mark: "))
    if checkPosition(choice):
        board[choice] = mark
        player += 1
        checkWin()

    os.system("clear")
    drawBoard()

    if game == draw:
        print("game draw")
    elif game == win:
        player = -1
        if player % 2 != 0:
            print("player 1 Won")
        else:
            print("player 2 Won")
