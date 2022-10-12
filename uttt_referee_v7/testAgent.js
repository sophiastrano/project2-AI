var fs = require('fs');
var os = require('os');

// CONSTANTS
const MOVEMULTIPLIER = [1.4, 1, 1.4, 1, 1.75, 1, 1.4, 1, 1.4];
const WINNUM = 5000;
const SCORINGSYSTEM = [0.2, 0.17, 0.2, 0.17, 0.22, 0.17, 0.2, 0.17, 0.2];

// TO BE UPDATED
var Running = true;
var firstFourMoves = false;
var mRM = 0;
var globalBoard = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]];
var mainBoard = [0, 0, 0, 0, 0, 0, 0, 0, 0];
var player = 1;
var computerVal = -1;
var MOVES = 0;

/**
 * @summary Updates the stored board with a new move
 * @param {object} currentBoard the current global board
 * @param {number} localBoard the local board for the new move
 * @param {number} newMove the number space for the new move (0-8)
 * @param {boolean} whoMoved which player made this move
 * @returns {object} the updated board
 */
function updateBoard(currentBoard, localBoard, newMove, whoMoved) {
    // add move to board from move file
    var val = 0;
    if (whoMoved == false) {
        val = -1;
    }
    if (whoMoved == true) {
        val = 1;
    }
    // whoMoved is a boolean, opponent is false and we are true, always false then true
    // assigns -1 for their moves and 1 for ours, already checks if board is full
    currentBoard[localBoard][newMove] = val;
    return currentBoard;
}

/**
 * @summary Checks if the file exists
 * @param {object} file the file to be checked
 * @returns {boolean} whether the file exists
 */
function checkFileExists(file) {
    return fs.promises.access(file, fs.constants.F_OK)
        .then(() => true)
        .catch(() => false)
}

/**
 * @summary Writes to move_file
 * @param {string} result the string to write to move_file
 */
async function writeFile(result) {
    fs.writeFile('move_file', result, (err) => {
        // In case of a error throw err.
        if (err) throw err;
    })
}

/**
 * @summary Checks if it is the end of the game
 * @returns {boolean} whether the game has ended
 */
async function checkIfEndGameExists() {
    var endFileExists = await checkFileExists("end_game");
    if (endFileExists) {
        Running = false;
    }
}

/**
 * @summary Plays the game - manages the helper functions - communicates with the referee
 */
async function play() {
    while (Running) {
        checkIfEndGameExists();

        var currentLocalBoard = "";
        var mostRecentMove = "";

        if (!firstFourMoves && await checkFileExists('first_four_moves')) {
            var ffm = fs.readFileSync('first_four_moves', { encoding: 'utf8', flag: 'r' });
            var lineArray = ffm.split(os.EOL);
            for (var x = 0; x < 4; x++) {
                var player = true;
                var opponentMove = lineArray[x].split(" ");
                if (process.argv[2] !== opponentMove[0]) {
                    player = false;
                }
                var currentLocalBoard = opponentMove[1];
                var mostRecentMove = opponentMove[2];
                globalBoard = updateBoard(globalBoard, parseInt(currentLocalBoard), parseInt(mostRecentMove), !player);
            }
            firstFourMoves = true;
            mRM = parseInt(mostRecentMove);
        }
        else if (firstFourMoves && await checkFileExists(process.argv[2] + ".go")) {
            var moveFile = fs.readFileSync('./move_file', {
                encoding: 'utf8', flag: 'r'
            });
            if (moveFile !== "") {
                var opponentMove = moveFile.split(" ");
                var currentLocalBoard = opponentMove[opponentMove.length - 2];
                var mostRecentMove = opponentMove[opponentMove.length - 1];
                if (!isNaN(parseInt(currentLocalBoard))) {
                    globalBoard = updateBoard(globalBoard, parseInt(currentLocalBoard), parseInt(mostRecentMove), true);
                }
            } else {
                mostRecentMove = mRM;
            }
            var boardToPlay = mostRecentMove;
            var result = algorithm(process.argv[2], globalBoard, boardToPlay);
            var ourLocalBoard = result.substring(result.length - 3, result.length - 2);
            var ourRecentMove = result.substring(result.length - 1, result.length);
            globalBoard = updateBoard(globalBoard, ourLocalBoard, ourRecentMove, false);
            writeFile(result);
            await new Promise(resolve => setTimeout(resolve, 900));
        }
    }
}

/**
 * @summary Checks a 3x3 Tic-Tac-Toe board
 * @param {object} localBoard the array of length 9 representing the board
 * @returns {number} 1 or -1 if a specific player has won, returns 0 if no one has won
 */
function computeWinOrLoss(localBoard) {
    var winVal = 1;
    if (localBoard[0] + localBoard[1] + localBoard[2] === winVal * 3 || localBoard[3] + localBoard[4] + localBoard[5] === winVal * 3 || localBoard[6] + localBoard[7] + localBoard[8] === winVal * 3 || localBoard[0] + localBoard[3] + localBoard[6] === winVal * 3 || localBoard[1] + localBoard[4] + localBoard[7] === winVal * 3 ||
        localBoard[2] + localBoard[5] + localBoard[8] === winVal * 3 || localBoard[0] + localBoard[4] + localBoard[8] === winVal * 3 || localBoard[2] + localBoard[4] + localBoard[6] === winVal * 3) {
        return winVal;
    }
    winVal = -1;
    if (localBoard[0] + localBoard[1] + localBoard[2] === winVal * 3 || localBoard[3] + localBoard[4] + localBoard[5] === winVal * 3 || localBoard[6] + localBoard[7] + localBoard[8] === winVal * 3 || localBoard[0] + localBoard[3] + localBoard[6] === winVal * 3 || localBoard[1] + localBoard[4] + localBoard[7] === winVal * 3 ||
        localBoard[2] + localBoard[5] + localBoard[8] === winVal * 3 || localBoard[0] + localBoard[4] + localBoard[8] === winVal * 3 || localBoard[2] + localBoard[4] + localBoard[6] === winVal * 3) {
        return winVal;
    }
    return 0;
}

/**
 * @summary Performs a numerical evaluation of the whole game in it's current state
 * @param {object} tryPos the possible state of the board to be evaluated
 * @param {number} localBoardNum the index of the local board being tested
 * @returns {number} Integer depending on whether someone has won or drawn (1, 0 , -1)
 */
function gameAnalysis(tryPos, localBoardNum) {
    var numEval = 0;
    var globalBoard = [];
    for (let count = 0; count < 9; count++) {
        numEval += realEvaluateSquare(tryPos[count]) * 1.5 * MOVEMULTIPLIER[count];
        if (count === localBoardNum) {
            numEval += realEvaluateSquare(tryPos[count]) * MOVEMULTIPLIER[count];
        }
        var tmpEv = computeWinOrLoss(tryPos[count]);
        numEval -= tmpEv * MOVEMULTIPLIER[count];
        globalBoard.push(tmpEv);
    }
    numEval -= computeWinOrLoss(globalBoard) * WINNUM;
    numEval += realEvaluateSquare(globalBoard) * 150;
    return numEval;
}

/**
 * @summary the Minimax Algorithm
 * @param {object} potenGlobalBoard the possible state of the board to be evaluated
 * @param {number} boardNum the number of the board that will be played on (0-8)
 * @param {number} depth the depth limit
 * @param {number} a αlpha value - for αβ pruning
 * @param {number} b βeta value - for αβ pruning
 * @param {boolean} minMaxBool whether you are evaluating max on minimax algorithm
 * @returns {number} Integer depending on whether someone has won or drawn (1, 0 , -1)
 */
function minimax(potenGlobalBoard, boardNum, depth, a, b, minMaxBool) {
    var beginMove = -1;
    var gameEvaluation = gameAnalysis(potenGlobalBoard, boardNum);
    if (Math.abs(gameEvaluation) > WINNUM || depth <= 0) {
        return { "game_eval": gameEvaluation, "move": beginMove };
    }
    if (boardNum !== -1 && computeWinOrLoss(potenGlobalBoard[boardNum]) !== 0) {
        boardNum = -1;
    } else if (boardNum !== -1 && !potenGlobalBoard[boardNum].includes(0)) {
        boardNum = -1;
    }
    if (minMaxBool) {
        var maxEval = -Infinity;
        for (let minimaxCount = 0; minimaxCount < 9; minimaxCount++) {
            var minimaxEval = -Infinity;
            if (boardNum === -1) {
                for (var boardLoc = 0; boardLoc < 9; boardLoc++) {
                    if (computeWinOrLoss(potenGlobalBoard[minimaxCount]) === 0) {
                        if (potenGlobalBoard[minimaxCount][boardLoc] === 0) {
                            potenGlobalBoard[minimaxCount][boardLoc] = computerVal;
                            minimaxEval = minimax(potenGlobalBoard, boardLoc, depth - 1, a, b, false).game_eval;
                            potenGlobalBoard[minimaxCount][boardLoc] = 0;
                        }
                        if (minimaxEval > maxEval) {
                            maxEval = minimaxEval;
                            beginMove = minimaxCount;
                        }
                        a = Math.max(a, minimaxEval);
                    }
                }
                if (b <= a) { break; }
            } else {
                if (potenGlobalBoard[boardNum][minimaxCount] === 0) {
                    potenGlobalBoard[boardNum][minimaxCount] = computerVal;
                    minimaxEval = minimax(potenGlobalBoard, minimaxCount, depth - 1, a, b, false);
                    potenGlobalBoard[boardNum][minimaxCount] = 0;
                }
                var mMEGE = minimaxEval.game_eval;
                if (mMEGE > maxEval) {
                    maxEval = mMEGE;
                    beginMove = minimaxEval.move;
                }
                a = Math.max(a, mMEGE);
                if (b <= a) { break; }
            }
        }
        return { "game_eval": maxEval, "move": beginMove };
    } else {
        var minEval = Infinity;
        for (var minimaxCount = 0; minimaxCount < 9; minimaxCount++) {
            var minimaxEval = Infinity;
            if (boardNum === -1) {
                for (var boardLoc = 0; boardLoc < 9; boardLoc++) {
                    if (computeWinOrLoss(potenGlobalBoard[minimaxCount]) === 0) {
                        if (potenGlobalBoard[minimaxCount][boardLoc] === 0) {
                            potenGlobalBoard[minimaxCount][boardLoc] = player;
                            minimaxEval = minimax(potenGlobalBoard, boardLoc, depth - 1, a, b, true).game_eval;
                            potenGlobalBoard[minimaxCount][boardLoc] = 0;
                        }
                        if (minimaxEval < minEval) {
                            minEval = minimaxEval;
                            beginMove = minimaxCount;
                        }
                        b = Math.min(b, minimaxEval);
                    }
                }
                if (b <= a) { break; }
            } else {
                if (potenGlobalBoard[boardNum][minimaxCount] === 0) {
                    potenGlobalBoard[boardNum][minimaxCount] = player;
                    minimaxEval = minimax(potenGlobalBoard, minimaxCount, depth - 1, a, b, true);
                    potenGlobalBoard[boardNum][minimaxCount] = 0;
                }
                var mMEGE = minimaxEval.game_eval;
                if (mMEGE < minEval) {
                    minEval = mMEGE;
                    beginMove = minimaxEval.move;
                }
                b = Math.min(b, mMEGE);
                if (b <= a) { break; }
            }
        }
        return { "game_eval": minEval, "move": beginMove };
    }
}

/**
 * @summary Performs a numerical evaluation of a local board in it's current state
 * @param {object} localBoard an array of length 9 of the local board
 * @param {number} boardNum the number of the local board that is being evaluated on
 * @returns {number} an evaluation of placing the game peice in the square (0.0-1.0)
 */
function calculateLocalPosition(localBoard, boardNum) {
    localBoard[boardNum] = computerVal;
    var evaluation = 0;
    var a = 2;
    evaluation += SCORINGSYSTEM[boardNum];
    a = -2;
    if (localBoard[0] + localBoard[1] + localBoard[2] === a || localBoard[3] + localBoard[4] + localBoard[5] === a || localBoard[6] + localBoard[7] + localBoard[8] === a || localBoard[0] + localBoard[3] + localBoard[6] === a || localBoard[1] + localBoard[4] + localBoard[7] === a ||
        localBoard[2] + localBoard[5] + localBoard[8] === a || localBoard[0] + localBoard[4] + localBoard[8] === a || localBoard[2] + localBoard[4] + localBoard[6] === a) {
        evaluation += 1;
    }
    a = -3;
    if (localBoard[0] + localBoard[1] + localBoard[2] === a || localBoard[3] + localBoard[4] + localBoard[5] === a || localBoard[6] + localBoard[7] + localBoard[8] === a || localBoard[0] + localBoard[3] + localBoard[6] === a || localBoard[1] + localBoard[4] + localBoard[7] === a ||
        localBoard[2] + localBoard[5] + localBoard[8] === a || localBoard[0] + localBoard[4] + localBoard[8] === a || localBoard[2] + localBoard[4] + localBoard[6] === a) {
        evaluation += 5;
    }
    localBoard[boardNum] = player;
    a = 3;
    if (localBoard[0] + localBoard[1] + localBoard[2] === a || localBoard[3] + localBoard[4] + localBoard[5] === a || localBoard[6] + localBoard[7] + localBoard[8] === a || localBoard[0] + localBoard[3] + localBoard[6] === a || localBoard[1] + localBoard[4] + localBoard[7] === a ||
        localBoard[2] + localBoard[5] + localBoard[8] === a || localBoard[0] + localBoard[4] + localBoard[8] === a || localBoard[2] + localBoard[4] + localBoard[6] === a) {
        evaluation += 2;
    }
    localBoard[boardNum] = computerVal;
    evaluation -= computeWinOrLoss(localBoard) * 15;
    localBoard[boardNum] = 0;
    return evaluation;
}

/**
 * @summary Performs a detailed numerical evaluation of a small board in it's current state
 * @param {object} possLocalBoard an array of length 9 of possible board positions
 * @returns {number} an evaluation of placing the game peice in the square (0.0-1.0)
 */
function realEvaluateSquare(possLocalBoard) {
    var evaluation = 0;
    for (var index in possLocalBoard) {
        evaluation -= possLocalBoard[index] * SCORINGSYSTEM[index];
    }
    var comparison = 2;
    if (possLocalBoard[0] + possLocalBoard[1] + possLocalBoard[2] === comparison || possLocalBoard[3] + possLocalBoard[4] + possLocalBoard[5] === comparison || possLocalBoard[6] + possLocalBoard[7] + possLocalBoard[8] === comparison) {
        evaluation -= 6;
    }
    if (possLocalBoard[0] + possLocalBoard[3] + possLocalBoard[6] === comparison || possLocalBoard[1] + possLocalBoard[4] + possLocalBoard[7] === comparison || possLocalBoard[2] + possLocalBoard[5] + possLocalBoard[8] === comparison) {
        evaluation -= 6;
    }
    if (possLocalBoard[0] + possLocalBoard[4] + possLocalBoard[8] === comparison || possLocalBoard[2] + possLocalBoard[4] + possLocalBoard[6] === comparison) {
        evaluation -= 7;
    }
    comparison = -1;
    if ((possLocalBoard[0] + possLocalBoard[1] === 2 * comparison && possLocalBoard[2] === -comparison) || (possLocalBoard[1] + possLocalBoard[2] === 2 * comparison && possLocalBoard[0] === -comparison) || (possLocalBoard[0] + possLocalBoard[2] === 2 * comparison && possLocalBoard[1] === -comparison)
        || (possLocalBoard[3] + possLocalBoard[4] === 2 * comparison && possLocalBoard[5] === -comparison) || (possLocalBoard[3] + possLocalBoard[5] === 2 * comparison && possLocalBoard[4] === -comparison) || (possLocalBoard[5] + possLocalBoard[4] === 2 * comparison && possLocalBoard[3] === -comparison)
        || (possLocalBoard[6] + possLocalBoard[7] === 2 * comparison && possLocalBoard[8] === -comparison) || (possLocalBoard[6] + possLocalBoard[8] === 2 * comparison && possLocalBoard[7] === -comparison) || (possLocalBoard[7] + possLocalBoard[8] === 2 * comparison && possLocalBoard[6] === -comparison)
        || (possLocalBoard[0] + possLocalBoard[3] === 2 * comparison && possLocalBoard[6] === -comparison) || (possLocalBoard[0] + possLocalBoard[6] === 2 * comparison && possLocalBoard[3] === -comparison) || (possLocalBoard[3] + possLocalBoard[6] === 2 * comparison && possLocalBoard[0] === -comparison)
        || (possLocalBoard[1] + possLocalBoard[4] === 2 * comparison && possLocalBoard[7] === -comparison) || (possLocalBoard[1] + possLocalBoard[7] === 2 * comparison && possLocalBoard[4] === -comparison) || (possLocalBoard[4] + possLocalBoard[7] === 2 * comparison && possLocalBoard[1] === -comparison)
        || (possLocalBoard[2] + possLocalBoard[5] === 2 * comparison && possLocalBoard[8] === -comparison) || (possLocalBoard[2] + possLocalBoard[8] === 2 * comparison && possLocalBoard[5] === -comparison) || (possLocalBoard[5] + possLocalBoard[8] === 2 * comparison && possLocalBoard[2] === -comparison)
        || (possLocalBoard[0] + possLocalBoard[4] === 2 * comparison && possLocalBoard[8] === -comparison) || (possLocalBoard[0] + possLocalBoard[8] === 2 * comparison && possLocalBoard[4] === -comparison) || (possLocalBoard[4] + possLocalBoard[8] === 2 * comparison && possLocalBoard[0] === -comparison)
        || (possLocalBoard[2] + possLocalBoard[4] === 2 * comparison && possLocalBoard[6] === -comparison) || (possLocalBoard[2] + possLocalBoard[6] === 2 * comparison && possLocalBoard[4] === -comparison) || (possLocalBoard[4] + possLocalBoard[6] === 2 * comparison && possLocalBoard[2] === -comparison)) {
        evaluation -= 9;
    }
    comparison = -2;
    if (possLocalBoard[0] + possLocalBoard[1] + possLocalBoard[2] === comparison || possLocalBoard[3] + possLocalBoard[4] + possLocalBoard[5] === comparison || possLocalBoard[6] + possLocalBoard[7] + possLocalBoard[8] === comparison) {
        evaluation += 6;
    }
    if (possLocalBoard[0] + possLocalBoard[3] + possLocalBoard[6] === comparison || possLocalBoard[1] + possLocalBoard[4] + possLocalBoard[7] === comparison || possLocalBoard[2] + possLocalBoard[5] + possLocalBoard[8] === comparison) {
        evaluation += 6;
    }
    if (possLocalBoard[0] + possLocalBoard[4] + possLocalBoard[8] === comparison || possLocalBoard[2] + possLocalBoard[4] + possLocalBoard[6] === comparison) {
        evaluation += 7;
    }
    comparison = 1;
    if ((possLocalBoard[0] + possLocalBoard[1] === 2 * comparison && possLocalBoard[2] === -comparison) || (possLocalBoard[1] + possLocalBoard[2] === 2 * comparison && possLocalBoard[0] === -comparison) || (possLocalBoard[0] + possLocalBoard[2] === 2 * comparison && possLocalBoard[1] === -comparison)
        || (possLocalBoard[3] + possLocalBoard[4] === 2 * comparison && possLocalBoard[5] === -comparison) || (possLocalBoard[3] + possLocalBoard[5] === 2 * comparison && possLocalBoard[4] === -comparison) || (possLocalBoard[5] + possLocalBoard[4] === 2 * comparison && possLocalBoard[3] === -comparison)
        || (possLocalBoard[6] + possLocalBoard[7] === 2 * comparison && possLocalBoard[8] === -comparison) || (possLocalBoard[6] + possLocalBoard[8] === 2 * comparison && possLocalBoard[7] === -comparison) || (possLocalBoard[7] + possLocalBoard[8] === 2 * comparison && possLocalBoard[6] === -comparison)
        || (possLocalBoard[0] + possLocalBoard[3] === 2 * comparison && possLocalBoard[6] === -comparison) || (possLocalBoard[0] + possLocalBoard[6] === 2 * comparison && possLocalBoard[3] === -comparison) || (possLocalBoard[3] + possLocalBoard[6] === 2 * comparison && possLocalBoard[0] === -comparison)
        || (possLocalBoard[1] + possLocalBoard[4] === 2 * comparison && possLocalBoard[7] === -comparison) || (possLocalBoard[1] + possLocalBoard[7] === 2 * comparison && possLocalBoard[4] === -comparison) || (possLocalBoard[4] + possLocalBoard[7] === 2 * comparison && possLocalBoard[1] === -comparison)
        || (possLocalBoard[2] + possLocalBoard[5] === 2 * comparison && possLocalBoard[8] === -comparison) || (possLocalBoard[2] + possLocalBoard[8] === 2 * comparison && possLocalBoard[5] === -comparison) || (possLocalBoard[5] + possLocalBoard[8] === 2 * comparison && possLocalBoard[2] === -comparison)
        || (possLocalBoard[0] + possLocalBoard[4] === 2 * comparison && possLocalBoard[8] === -comparison) || (possLocalBoard[0] + possLocalBoard[8] === 2 * comparison && possLocalBoard[4] === -comparison) || (possLocalBoard[4] + possLocalBoard[8] === 2 * comparison && possLocalBoard[0] === -comparison)
        || (possLocalBoard[2] + possLocalBoard[4] === 2 * comparison && possLocalBoard[6] === -comparison) || (possLocalBoard[2] + possLocalBoard[6] === 2 * comparison && possLocalBoard[4] === -comparison) || (possLocalBoard[4] + possLocalBoard[6] === 2 * comparison && possLocalBoard[2] === -comparison)) {
        evaluation += 9;
    }
    evaluation -= computeWinOrLoss(possLocalBoard) * 12;
    return evaluation;
}

/**
 * @summary Runs the Minimax algorithm + ancillary functions
 * @param {string} playerName the name of the player
 * @param {object} smallBoards the 2d array of all the small boards (the Global Board)
 * @param {number} currBoard the number of the current board to play on (0-8)
 * @returns {string} the message to write to the text file, in format "{PlayerName} {LocalBoardNumber} {SpaceNumber}"
 */
function algorithm(playerName, smallBoards, currBoard) {
    var currentBoard = currBoard;
    topMove = -1;
    topScore = [-Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity, -Infinity];
    var count = 0;
    for (let index = 0; index < smallBoards.length; index++) {
        if (computeWinOrLoss(smallBoards[index]) === 0) {
            smallBoards[index].forEach(function (param) { param === 0 && count++ });
        }
    }
    if (mainBoard[currentBoard] !== 0 || !smallBoards[currentBoard].includes(0)) {
        currentBoard = -1;
    }
    if (currentBoard === -1 || computeWinOrLoss(smallBoards[currentBoard]) !== 0) {
        var cachedMiniMax;
        if (MOVES < 10) {
            cachedMiniMax = minimax(smallBoards, -1, Math.min(4, count), -Infinity, Infinity, true);
        } else if (MOVES < 18) {
            cachedMiniMax = minimax(smallBoards, -1, Math.min(5, count), -Infinity, Infinity, true);
        } else {
            cachedMiniMax = minimax(smallBoards, -1, Math.min(6, count), -Infinity, Infinity, true);
        }
        currentBoard = cachedMiniMax.move;
    }
    for (let index = 0; index < 9; index++) {
        if (smallBoards[currentBoard][index] === 0) {
            topMove = index;
            break;
        }
    }
    if (topMove !== -1) {
        for (let index = 0; index < 9; index++) {
            if (smallBoards[currentBoard][index] === 0) {
                var analysis = calculateLocalPosition(smallBoards[currentBoard], index) * 45;
                topScore[index] = analysis;
            }
        }
        for (let index = 0; index < 9; index++) {
            if (computeWinOrLoss(smallBoards[currentBoard]) === 0) {
                if (smallBoards[currentBoard][index] === 0) {
                    smallBoards[currentBoard][index] = computerVal;
                    var cachedMiniMax;
                    if (MOVES < 20) {
                        cachedMiniMax = minimax(smallBoards, index, Math.min(5, count), -Infinity, Infinity, false);
                    } else if (MOVES < 32) {
                        cachedMiniMax = minimax(smallBoards, index, Math.min(6, count), -Infinity, Infinity, false);
                    } else {
                        cachedMiniMax = minimax(smallBoards, index, Math.min(7, count), -Infinity, Infinity, false);
                    }
                    var temp = cachedMiniMax.game_eval;
                    smallBoards[currentBoard][index] = 0;
                    topScore[index] += temp;
                }
            }
        }
        for (let index in topScore) {
            if (topScore[index] > topScore[topMove]) {
                topMove = index;
            }
        }
        if (smallBoards[currentBoard][topMove] === 0) {
            smallBoards[currentBoard][topMove] = computerVal;
        }
    }

    for (var index in smallBoards) {
        if (mainBoard[index] === 0) {
            if (computeWinOrLoss(smallBoards[index]) !== 0) {
                mainBoard[index] = computeWinOrLoss(smallBoards[index]);
            }
        }
    }
    return (playerName + " " + currentBoard + " " + topMove);
}

/**
 * @summary Running our AI!
 */
play();