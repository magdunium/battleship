__author__ = 'Magdum'

from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!\n"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)


ship_row = random_row(board)
ship_col = random_col(board)


# The Game code
def theGame():
    for turn in range(5):
        gameResult = 0

        guess_row = int(raw_input("Guess Row:")) - 1
        guess_col = int(raw_input("Guess Col:")) - 1

        if guess_row == ship_row and guess_col == ship_col:
            print "Congratulations! You sunk my battleship!\n"
            break
        else:
            if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                print "Oops, that's not even in the ocean.\n"
            elif (board[guess_row][guess_col] == "X"):
                print "You guessed that one already.\n"
            else:
                print "You missed my battleship!\n"
                board[guess_row][guess_col] = "X"
            print_board(board)

        print "Turn", turn + 1
    gameResult += turn
    print "Your total result is: ", gameResult + 1, ", Congratulations!\n"

def player1(theGame):
    print "\nPlayer-1 turn: "
    theGame()

def player2(theGame):
    print "\nPlayer-2 turn: "
    theGame()

def whoWon(player1result, player2result):
    if player1result > player2result:
        print "Player 2 WON!"
    elif player1result == player1result:
        print "It's a TIE!"
    else:
        print "Player 1 WON!"


if __name__ == '__main__':
    whoWon(player1(theGame), player2(theGame))
