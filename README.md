# CS 4341 Project 2: Game Playing
## Ultimate Tic-Tac-Toe
Project 2 for Sophia Strano, Luke Foley, &amp; Ilana Whittaker

## Initial Project Submission
woohoo yeh

### To run and compile our program: 

Our "Urinetown" agent uses a javaScript file, "getMoves.js" to calculate its next move. To have our Agent play against itself, please call:
   - node testAgent.js Urinetown1
   
in one terminal, 
   - node testAgent.js Urinetown2
   
in another terminal (though other names should work),

and in the third and final terminal: 
   - python referee.py Urinetown1 Urinetown2
### Designing our Agent

- Contributions to Development
   - The team worked both synchronously and asynchronously to complete the UTTT project in its entirety while communicating with TA to develop initial psuedocode as a group. Luke focused a lot of effort into developing minimax inside of the getMoves.js file. Sophie began implementing python within html to develop the functions our agent would use to maintain track of the global board, as well as read and write to and from the move_file after the algorithm is accessed. The team faced huge setbacks due to a massive struggle to merge the work that had been done in python with the work that had been done in JavaScript with the work that had been done in python- multiple libraries like js2py and bond were explored in an attempt to resolve this, but despite thorough review of documentation and a variety of scrapped interfacing the team eventually decided to move forward by translating all of the python code we had written to make use of our agent into javaScript so that it would more seamlessly. 

- Our Utility Function
   - The utility function that our program uses
- Our Evaluation Function
   - The evaluation function that our program uses
- The heuristics and/or strategies that you employed to decide how to expand nodes of the minimax tree without exceeding your time limit.
   - The heuristic functions are computeWinOrLoss, gameAnalysis, calculateLocalPosition, and realEvaluateSquare.
      - computeWinOrLoss takes in the local board as its only parameter and returns a number. This function returns a 1 or a -1 if a specific player has won, or returns 0 if there is no winner yet.
      - gameAnalysis takes in tryPos, which is an object that represents the possible state of the board. It also takes in the localBoardNum, which is the cell number of the current board in play.  It returns an integer (-1, 0, or 1) to represent if someone has lost, tied, or won.
      - calculateLocalPosition takes in 2 parameters, those being localBoard, and boardNum.  This is an array of the board in play and the number cell of that board.  The function uses a scoring system to decide how "good" a move is.  This is scored on a scale of 0.0 to 1.0.  This number is returned.
      - realEvaluateSquare evaluates the small board in its current state.  It takes in 1 parameter, that being possLocalBoard, which is an array of the possible board positions.  This function again returns a number on a scale from 0.0 to 1.0, ranked on how good a possible move is.
### Results and Testing
- Testing our Agent
   - To test our Agent, we attempted to have the Agent play against itself and human players, but we consistently ran into a series of errors causing our agent to choose an invalid move. Our program successfully begins to evaluate these moves, but sometimes struggled with the format moves were read in and out of the program with.
-  Strengths and the weaknesses of your program.
   -  they are
- A discussion of why the evaluation function and the heuristic(s) you picked are good choices.
   - The heuristics picked are good choices because they allow the possible moves to be ranked on a numberical scale. This eliminates ambiguity when the program is trying to decide which move to proceed with. Using heuristics allowed us to determine how good a move was.  Therefore, a brute force search of all possible moves does not have to be used.  One of our heuristic functions returns a number, -1, 0, or 1, to determine if a player has lost, tied, or won. This can be used to evaluate winning and losing positions.  Our heuristics are able to assign different temporary point values depending on what the possible move is, whether this be a small board win, winning center board, etc.

### Code.  
- The source code for your program
- Ancillary files, if any, that your program requires (e.g., such as a script to run a language interpreter).
Feel free to access our UTTT agent through our github repository: https://github.com/sophiastrano/project2-AI

