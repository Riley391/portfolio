# TODO: fix parseSpace such that parsedSpace[0] is the x coord and parsedSpace[1] is the y coord
# TODO: fix recursion bug in reveal zeros function by making a board class

import random
import sys
import os

class Tile:
    def __init__(self):
        mineOrNot = random.randint(1, 5)
        if mineOrNot == 3:
            self.mine = "x"
        else:
            self.mine = "~"
        self.number = 0
        self.default = "~"
        self.revealed = False
        self.exploded = False
    def flag(self):
        if self.default == "|":
            self.default = "~"
        else:
            self.default = "|"
        if self.mine == "x":
            self.revealed = True
    def reveal(self):
        if self.mine == "x":
            self.default = self.mine
            self.exploded = True
        else:
            self.default = self.number
            self.revealed = True

def clearConsole():
    if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        os.system('clear')
    elif sys.platform.startswith('win'):
        os.system('cls')

def quitOrNot(string):
    if string == 'quit':
        quit()

def customQuit():
    playAgain = input("Would you like to play again? (y/n): ")
    if playAgain == 'y':
        gameStart()
    elif playAgain == 'n':
        quit()
    else:
        customQuit()

def buildBoard(dimensions):
    board = []
    for x in range(dimensions):
        boardList = []
        board.append(boardList)
        for y in range(dimensions):
            tile = Tile()
            board[x].append(tile)
    return board

def buildNumberBoard(board):
    mineCheckMin = -1
    mineCheckMax = 1
    for x in range(len(board)):
        for y in range(len(board[x])):
            # check the 3x3 around this tile for mines
            for z in range(mineCheckMin, mineCheckMax + 1):
                for zz in range(mineCheckMin, mineCheckMax + 1):
                    # make sure we're not checking tiles out of bounds
                    if len(board) > x + z >= 0 and len(board) > y + zz >= 0:
                        # make sure we're not checking the center tile of the 3x3
                        if board[x + z][y + zz] != board[x][y]:
                            if board[x + z][y + zz].mine == "x":
                                board[x][y].number += 1
    return board

def printBoard(board):
    boardLength = len(board)
    firstLine = "  "
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(boardLength):
        mutableI = i
        while mutableI >= len(alphabet):
            mutableI -= len(alphabet)
        firstLine += alphabet[mutableI]
    print(firstLine)
    # create numbered lines
    for x in range(len(board)):
        line = str(x + 1) + " "
        for y in range(len(board[x])):
            line += str(board[x][y].default)
        print(line)
    print("\n")

def didIWin(board):
    # check for win condition (all tiles correctly identified)
    changedCheck = len(board) * len(board)
    checkAgainst = 0
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y].revealed:
                checkAgainst += 1
    if changedCheck == checkAgainst:
        printBoard(board)
        gameOver(True)

def gameOver(winOrLose):
    print("You win!") if winOrLose else print("You lose!")
    customQuit()

def parseSpace(space):
    quitOrNot(space)
    realSpace = ""
    spaceList = []
    for character in space:
        if character.isalpha():
            realSpace += character
    for character2 in space:
        if not character2.isalpha():
            realSpace += character2
    realSpace = realSpace.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    try:
        letter = alphabet.index(realSpace[0])
        number = realSpace[slice(1, len(realSpace))]
        spaceList = [letter, int(number) - 1]
    except:
        space = input("Which space would you like to check? (use 'A1' as your template): ")
        spaceList = parseSpace(space)
    return spaceList

def revealAdjacentZeros(board, parsedSpace):
    zeroCheckMin = -1
    zeroCheckMax = 1
    x = parsedSpace[1]
    y = parsedSpace[0]
    # check the 3x3 around this tile for zeros
    for z in range(zeroCheckMin, zeroCheckMax + 1):
        for zz in range(zeroCheckMin, zeroCheckMax + 1):
            # make sure we're not checking tiles out of bounds
            if len(board) > x + z >= 0 and len(board) > y + zz >= 0:
                # make sure we're not checking the center tile of the 3x3
                if board[x + z][y + zz] != board[x][y]:
                    if board[x + z][y + zz].number == 0:
                        board[x + z][y + zz].reveal
                        revealAdjacentZeros(board, [y + zz, x + z])

def gameLoop(board):
    printBoard(board)
    yourTurn(board)

def yourTurn(board):
    flagOrNot = input("Would you like to uncover a tile or mark a mine? ('tile' or 'mine'): ")
    quitOrNot(flagOrNot)
    if flagOrNot.lower() != 'tile' and flagOrNot.lower() != 'mine':
        yourTurn(board)
    space = input("Which space would you like to check? (use 'A1' as your template): ")
    parsedSpace = parseSpace(space)
    chosenTile = board[parsedSpace[1]][parsedSpace[0]]
    if flagOrNot.lower() == 'tile':
        chosenTile.reveal()
        if chosenTile.exploded:
            printBoard(board)
            gameOver(False)
        else:
            # revealAdjacentZeros(board, parsedSpace)
            gameLoop(board)
    elif flagOrNot.lower() == 'mine':
        chosenTile.flag()
        gameLoop(board)


def gameStart():
    clearConsole()
    dimensions = input("How large would you like the game board to be?: ")
    if not dimensions.isnumeric():
        gameStart()
    quitOrNot(dimensions)
    board = buildBoard(int(dimensions))
    board = buildNumberBoard(board)
    gameLoop(board)

gameStart()