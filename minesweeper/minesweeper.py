import random
import sys
import os

def clearConsole():
    if sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        os.system('clear')
    elif sys.platform.startswith('win'):
        os.system('cls')

def quitOrNot(string):
    if string == 'quit':
        quit()

def buildBoard(dimensions):
    board = []
    for x in range(dimensions):
        boardList = []
        board.append(boardList)
        for y in range(dimensions):
            boardDictionary = { "mine": "", "number": 0, "default": "~", "uncovered": False }
            board[x].append(boardDictionary)
    return board

def plantMines(board):
    for x in range(len(board)):
        for y in range(len(board[x])):
            mineOrNot = random.randint(1, 3)
            if mineOrNot == 3:
                board[x][y]["mine"] = 'x'
            else:
                board[x][y]["mine"] = '~'
    return board

def buildNumberBoard(board):
    for x in range(len(board)):
        for y in range(len(board[x])):
            for z in range(-1, 2):
                for za in range(-1, 2):
                    if len(board) > x + z >= 0 and len(board) > y + za >= 0:
                        if board[x + z][y + za] != board[x][y]:
                            if board[x + z][y + za]["mine"] == "x":
                                board[x][y]["number"] += 1
    return board

def printBoard(board, mineOrNumber="mine"):
    boardLength = len(board)
    firstLine = "  "
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    for i in range(boardLength):
        newI = i
        while newI >= len(alphabet):
            newI -= len(alphabet)
        firstLine += alphabet[newI]
    print(firstLine)
    for x in range(len(board)):
        line = str(x + 1) + " "
        for y in range(len(board[x])):
            line += str(board[x][y][mineOrNumber])
        print(line)
    print("\n")

def parseSpace(space):
    quitOrNot(space)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    letter = alphabet.index(space[0])
    number = space[slice(1, len(space))]
    spaceList = [letter, int(number) - 1]
    return spaceList

def gameLoop(board, printMines=False, printNumbers=False):
    changedCheck = len(board) * len(board)
    checkAgainst = 0
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y]["uncovered"]:
                checkAgainst += 1
    if changedCheck == checkAgainst:
        printBoard(board)
        print("You win!")
        quit()
    printBoard(board, "default")
    if printMines:
        printBoard(board, "mine")
    if printNumbers:
        printBoard(board, "number")
    yourTurn(board)

def yourTurn(board):
    flagOrNot = input("Would you like to uncover a tile or mark a mine? ('tile' or 'mine'): ")
    quitOrNot(flagOrNot)
    space = input("Which space would you like to check? (use 'A1' as your template): ")
    parsedSpace = parseSpace(space)
    if flagOrNot == 'tile':
        if board[parsedSpace[1]][parsedSpace[0]]["mine"] == "x":
            board[parsedSpace[1]][parsedSpace[0]]["default"] = "x"
            printBoard(board, "default")
            print("You lose!")
            quit()
        elif board[parsedSpace[1]][parsedSpace[0]]["mine"] == "~":
            board[parsedSpace[1]][parsedSpace[0]]["default"] = board[parsedSpace[1]][parsedSpace[0]]["number"]
            board[parsedSpace[1]][parsedSpace[0]]["uncovered"] = True
            gameLoop(board)
    elif flagOrNot == 'mine':
        board[parsedSpace[1]][parsedSpace[0]]["default"] = "|"
        board[parsedSpace[1]][parsedSpace[0]]["uncovered"] = True
        gameLoop(board)


def gameStart(printMines=False, printNumbers=False):
    clearConsole()
    dimensions = input("How large would you like the game board to be?: ")
    quitOrNot(dimensions)
    board = buildBoard(int(dimensions))
    board = plantMines(board)
    board = buildNumberBoard(board)
    gameLoop(board, printMines, printNumbers)

gameStart()

# TODO: handle user input that generates errors