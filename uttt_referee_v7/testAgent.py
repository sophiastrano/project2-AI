import os
import sys
import js2py
import re
import time
from functools import partial
from os import listdir
from os.path import isfile, join

# program must use Urinetown in communication
# call js game -> pass in team name, pass in boards, pass in current board to play
# find go file -> see if game is over -> see that board is empty -> become first player
eval_res, testAgent = js2py.run_file("getMove.js")

js2py.translate_file("getMove.js", "translation.py")
from translation import *

# thing1, thing2 = js2py.run_file("getMove.js")
# toPrint = thing2.hello()
# print(toPrint)

# To do: update boards value on return from game call and from text file input
globalBoard = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]

# if .go is detected, then begin updating our total board with recent move

# make a forever loop -> do all this while game running is true, detect end_game file to set false

def updateBoard(currentBoard, localBoard, newMove, whoMoved):
    # add move to board from move file
    val = 0
    if whoMoved == False:
        val = -1
    if whoMoved == True:
        val = 1
        # whoMoved is a boolean, opponent is false and we are true, always false then true
        # assigns -1 for their moves and 1 for ours, already checks if board is full
    currentBoard[localBoard][newMove] = val
    return currentBoard
    # update currBoard with localBoard value and newMove value that are in move file

    # localBoard = should be defined by readMoves into currentLocalBoard
    # newMove = read something out of text file in pos 2

    # Checks for go file, starts doing stuff


Running = True

while Running:
    if os.path.exists("end_game"):
        Running = False
    while not os.path.exists("first_four_moves"):
        time.sleep(1)

    currentLocalBoard = ""
    mostRecentMove = ""

        # read text, search line for space and assign based on position
        # set mostRecentMove = read something out of text file in pos 2
        # set currentLocalBoard = read something out of text file in pos 1

        # board updating function to be used to add the most recent move to our global board
        # sep function to read in from move_file for opponent

    if os.path.exists(sys.argv[1] + ".go"):
        # Adds opponent move to our board
        with open('move_file', "r") as f:
            if os.path.getsize("move_file") == 0:
                with open('first_four_moves', "r") as ffm:
                    # Read contents of first_four_moves
                    lineArray = ffm.readlines()
                    # Add to updateBoard
                    for moveLine in lineArray:
                        print(moveLine)
                        opponentMove = moveLine.split(" ")
                        currentLocalBoard = opponentMove[1]
                        mostRecentMove = opponentMove[2]
                        globalBoard = updateBoard(globalBoard, int(currentLocalBoard), int(mostRecentMove), False)
            else:
                line = f.readline()
                opponentMove = line.split(" ")
                currentLocalBoard = opponentMove[1]
                mostRecentMove = opponentMove[2]
        globalBoard = updateBoard(globalBoard, int(currentLocalBoard), int(mostRecentMove), False)

        # Calls JS function to use our AI
        boardToPlay = currentLocalBoard
        result = translation.game(sys.argv[1], globalBoard, boardToPlay, False)
        print(result)
        ourMove = result.split(" ")
        ourLocalBoard = ourMove[1]
        ourRecentMove = ourMove[2]

        # send result to the move_file myself (have it just return numbers)
        globalBoard = updateBoard(globalBoard, ourLocalBoard, ourRecentMove, True)

        # Write our move to the Urinetown .go file

        file = open('move_file', "r")
        file.seek(0)
        file.write(result)  # whatever your move is...
        file.truncate()
        file.close()
