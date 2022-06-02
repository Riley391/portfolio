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
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
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
    # quitOrNot(space)
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
        customQuit()
    printBoard(board, "default")
    if printMines:
        printBoard(board, "mine")
    if printNumbers:
        printBoard(board, "number")
    yourTurn(board)

def yourTurn(board):
    flagOrNot = input("Would you like to uncover a tile or mark a mine? ('tile' or 'mine'): ")
    quitOrNot(flagOrNot)
    if flagOrNot.lower() != 'tile' and flagOrNot.lower() != 'mine':
        yourTurn(board)
    space = input("Which space would you like to check? (use 'A1' as your template): ")
    parsedSpace = parseSpace(space)
    if flagOrNot.lower() == 'tile':
        if board[parsedSpace[1]][parsedSpace[0]]["mine"] == "x":
            board[parsedSpace[1]][parsedSpace[0]]["default"] = "x"
            printBoard(board, "default")
            print("You lose!")
            customQuit()
        elif board[parsedSpace[1]][parsedSpace[0]]["mine"] == "~":
            board[parsedSpace[1]][parsedSpace[0]]["default"] = board[parsedSpace[1]][parsedSpace[0]]["number"]
            board[parsedSpace[1]][parsedSpace[0]]["uncovered"] = True
            gameLoop(board)
    elif flagOrNot.lower() == 'mine':
        board[parsedSpace[1]][parsedSpace[0]]["default"] = "|"
        board[parsedSpace[1]][parsedSpace[0]]["uncovered"] = True
        gameLoop(board)


def gameStart(printMines=False, printNumbers=False):
    clearConsole()
    dimensions = input("How large would you like the game board to be?: ")
    if not dimensions.isnumeric():
        gameStart()
    quitOrNot(dimensions)
    board = buildBoard(int(dimensions))
    board = plantMines(board)
    board = buildNumberBoard(board)
    gameLoop(board, printMines, printNumbers)

gameStart()