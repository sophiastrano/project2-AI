
// program must use Urinetown in communication
// call js game -> pass in team name, pass in boards, pass in current board to play
// find go file -> see if game is over -> see that board is empty -> become first player


// thing1, thing2 = js2py.run_file("getMove.js")
// toPrint = thing2.hello()
// print(toPrint)

// To do: update boards value on return from game call and from text file input
var globalBoard = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]];

// if .go is detected, then begin updating our total board with recent move

// make a forever loop -> do all this while game running is true, detect end_game file to set false

function updateBoard(currentBoard, localBoard, newMove, whoMoved) {
    // add move to board from move file
    var val = 0;
    if (whoMoved == False) {
        val = -1;
    }
    if (whoMoved == True) {
        val = 1;
    }
    // whoMoved is a boolean, opponent is false and we are true, always false then true
    // assigns -1 for their moves and 1 for ours, already checks if board is full
    currentBoard[localBoard][newMove] = val;
    return currentBoard;
}
// update currBoard with localBoard value and newMove value that are in move file

// localBoard = should be defined by readMoves into currentLocalBoard
// newMove = read something out of text file in pos 2

// Checks for go file, starts doing stuff


var Running = True;

while (Running) {
    var endFile = new File("end_game");
    if (endFile.exists()) {
        Running = False;
    }
    while (!endFile.exists()) {
        time.sleep(1)
    }

    var currentLocalBoard = "";
    var mostRecentMove = "";

    // read text, search line for space and assign based on position
    // set mostRecentMove = read something out of text file in pos 2
    // set currentLocalBoard = read something out of text file in pos 1

    // board updating function to be used to add the most recent move to our global board
    // sep function to read in from move_file for opponent

    if (os.path.exists(sys.argv[1] + ".go")) {
        // Adds opponent move to our board
        with (open('move_file', "r") as f) {
            if (os.path.getsize("move_file") == 0) {
                with (open('first_four_moves', "r") as ffm) {
                    // Read contents of first_four_moves
                    var lineArray = ffm.readlines();
                    // Add to updateBoard
                    for (moveLine in lineArray) {
                        console.log(moveLine);
                        var opponentMove = moveLine.split(" ");
                        var currentLocalBoard = opponentMove[1];
                        var mostRecentMove = opponentMove[2];
                        globalBoard = updateBoard(globalBoard, int(currentLocalBoard), int(mostRecentMove), false);
                    }
                }
            } else {
                var line = f.readline();
                var opponentMove = line.split(" ");
                var currentLocalBoard = opponentMove[1];
                var mostRecentMove = opponentMove[2];
                globalBoard = updateBoard(globalBoard, int(currentLocalBoard), int(mostRecentMove), false);
            }
        }

        // Calls JS function to use our AI
        var boardToPlay = currentLocalBoard;
        var result = translation.game(sys.argv[1], globalBoard, boardToPlay, false);
        console.log(result);
        var ourMove = result.split(" ");
        var ourLocalBoard = ourMove[1];
        var ourRecentMove = ourMove[2];

        // send result to the move_file myself (have it just return numbers)
        globalBoard = updateBoard(globalBoard, ourLocalBoard, ourRecentMove, true);

        // Write our move to the Urinetown .go file

        var file = open('move_file', "r");
        file.seek(0);
        file.write(result);  // whatever your move is...
        file.truncate();
        file.close();
    }
}