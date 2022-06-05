# TODO: fix parseSpace such that parsedSpace[0] is the x coord and parsedSpace[1] is the y coord

import tkinter as tk
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

class Board:
    def __init__(self, dimensions):
        self.board = []
        for x in range(dimensions):
            boardList = []
            self.board.append(boardList)
            for y in range(dimensions):
                tile = Tile()
                self.board[x].append(tile)
    def buildNumberBoard(self):
        mineCheckMin = -1
        mineCheckMax = 1
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                # check the 3x3 around this tile for mines
                for z in range(mineCheckMin, mineCheckMax + 1):
                    for zz in range(mineCheckMin, mineCheckMax + 1):
                        # make sure we're not checking tiles out of bounds
                        if len(self.board) > x + z >= 0 and len(self.board) > y + zz >= 0:
                            # make sure we're not checking the center tile of the 3x3
                            if self.board[x + z][y + zz] != self.board[x][y]:
                                if self.board[x + z][y + zz].mine == "x":
                                    self.board[x][y].number += 1
    def printBoard(self):
        boardLength = len(self.board)
        firstLine = "  "
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in range(boardLength):
            mutableI = i
            while mutableI >= len(alphabet):
                mutableI -= len(alphabet)
            firstLine += alphabet[mutableI]
        print(firstLine)
        for x in range(len(self.board)):
            line = str(x + 1) + " "
            for y in range(len(self.board[x])):
                line += str(self.board[x][y].default)
            print(line)
        print("\n")
    def didIWin(self):
        # check for win condition (all tiles correctly identified)
        changedCheck = len(self.board) * len(self.board)
        checkAgainst = 0
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                if self.board[x][y].revealed:
                    checkAgainst += 1
        if changedCheck == checkAgainst:
            gameOver(True)
    def revealAdjacentZeros(self, parsedSpace):
        zeroCheckMin = -1
        zeroCheckMax = 1
        x = parsedSpace[1]
        y = parsedSpace[0]
        # check the 3x3 around this tile for zeros
        for z in range(zeroCheckMin, zeroCheckMax + 1):
            for zz in range(zeroCheckMin, zeroCheckMax + 1):
                # make sure we're not checking tiles out of bounds
                if len(self.board) > x + z >= 0 and len(self.board) > y + zz >= 0:
                    # make sure we're not checking the center tile of the 3x3
                    if self.board[x + z][y + zz] != self.board[x][y]:
                        if self.board[x + z][y + zz].number == 0 and self.board[x + z][y + zz].revealed == False:
                            self.board[x + z][y + zz].reveal()
                            self.revealAdjacentZeros([y + zz, x + z])

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

def gameLoop(board):
    board.printBoard()
    yourTurn(board)

def yourTurn(board):
    board.didIWin()
    flagOrNot = input("Would you like to uncover a tile or mark a mine? ('tile' or 'mine'): ")
    quitOrNot(flagOrNot)
    if flagOrNot.lower() != 'tile' and flagOrNot.lower() != 'mine':
        yourTurn(board)
    space = input("Which space would you like to check? (use 'A1' as your template): ")
    parsedSpace = parseSpace(space)
    chosenTile = board.board[parsedSpace[1]][parsedSpace[0]]
    if flagOrNot.lower() == 'tile':
        chosenTile.reveal()
        if chosenTile.exploded:
            board.printBoard()
            gameOver(False)
        else:
            if chosenTile.number == 0:
                board.revealAdjacentZeros(parsedSpace)
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
    board = Board(dimensions=int(dimensions))
    board.buildNumberBoard()
    gameLoop(board)

# gameStart()

window = tk.Tk()
window.title("Minesweeper")

""" e = tk.Entry(window, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

e.insert(0, "How large would you like the game board to be?: ") """

def button_click(button, tile):
    tile.reveal()
    button['text'] = tile.default

# button_1 = tk.Button(window, text="1", padx=40, pady=20, command=button_add)

testBoard = Board(3)
testBoard.buildNumberBoard()

button1 = tk.Button(window, text=testBoard.board[0][0].default, padx=50, pady=50, command=lambda: button_click(button1, testBoard.board[0][0]))
button2 = tk.Button(window, text=testBoard.board[0][1].default, padx=50, pady=50, command=lambda: button_click(button2, testBoard.board[0][1]))
button3 = tk.Button(window, text=testBoard.board[0][2].default, padx=50, pady=50, command=lambda: button_click(button3, testBoard.board[0][2]))
button4 = tk.Button(window, text=testBoard.board[1][0].default, padx=50, pady=50, command=lambda: button_click(button4, testBoard.board[1][0]))
button5 = tk.Button(window, text=testBoard.board[1][1].default, padx=50, pady=50, command=lambda: button_click(button5, testBoard.board[1][1]))
button6 = tk.Button(window, text=testBoard.board[1][2].default, padx=50, pady=50, command=lambda: button_click(button6, testBoard.board[1][2]))
button7 = tk.Button(window, text=testBoard.board[2][0].default, padx=50, pady=50, command=lambda: button_click(button7, testBoard.board[2][0]))
button8 = tk.Button(window, text=testBoard.board[2][1].default, padx=50, pady=50, command=lambda: button_click(button8, testBoard.board[2][1]))
button9 = tk.Button(window, text=testBoard.board[2][2].default, padx=50, pady=50, command=lambda: button_click(button9, testBoard.board[2][2]))

button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=0, column=2)
button4.grid(row=1, column=0)
button5.grid(row=1, column=1)
button6.grid(row=1, column=2)
button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)

""" buttonList = []
for x in range(len(testBoard.board)):
    tempList = []
    buttonList.append(tempList)
    for y in range(len(testBoard.board[x])):
        buttonList[x].append(tk.Button(window, text=testBoard.board[x][y].default, padx=10, pady=10, command=lambda: button_click(buttonList[x][y], testBoard.board[x][y])))
        buttonList[x][y].grid(row=x + 1, column=y) """


window.mainloop()