# CS 4341 Project 2: Game Playing
## Ultimate Tic-Tac-Toe
Project 2 for Sophia Strano, Luke Foley, &amp; Ilana Whittaker

## Initial Project Submission


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
   - The utility function(s) of our program that maintain and update the current state of the global board game while passing that information to the evaluation portion of our agent is largely contained in the testAgent.js file. The function updateBoard is used repeatedly by our agent to first read from the move_file and split the line into two strings containing the most recently used local board and move made, filling in our globalBoard array.
- Our Evaluation Function
   - The evaluation function that our program uses is largely contained within the getMove.js file, and is called by the utility functions in our testAgent file after each previous move is read in. The function "game" is the primary evaluator within getMoves.js, making use of the minimax function and huerisitc functions that are later described. The minimax function being used by our evaluation function consumes the current board as well as values for alpha beta pruning, and it returns either a 1, 0 , -1 to indicate that there was a win, draw, or loss in that scenario. 
- The heuristics and/or strategies that you employed to decide how to expand nodes of the minimax tree without exceeding your time limit.
   - The heuristic functions are computeWinOrLoss, gameAnalysis, calculateLocalPosition, and realEvaluateSquare.
      - computeWinOrLoss takes in the local board as its only parameter and returns a number. This function returns a 1 or a -1 if a specific player has won, or returns 0 if there is no winner yet.
      - gameAnalysis takes in tryPos, which is an object that represents the possible state of the board. It also takes in the localBoardNum, which is the cell number of the current board in play.  It returns an integer (-1, 0, or 1) to represent if someone has lost, tied, or won.
      - calculateLocalPosition takes in 2 parameters, those being localBoard, and boardNum.  This is an array of the board in play and the number cell of that board.  The function uses a scoring system to decide how "good" a move is.  This is scored on a scale of 0.0 to 1.0.  This number is returned.
      - realEvaluateSquare evaluates the small board in its current state.  It takes in 1 parameter, that being possLocalBoard, which is an array of the possible board positions.  This function again returns a number on a scale from 0.0 to 1.0, ranked on how good a possible move is.
### Results and Testing
- Testing our Agent
   - To test our Agent, we attempted to have the Agent play against itself and human players, but we consistently ran into a series of errors causing our agent to choose an invalid move. Our program successfully begins to evaluate these moves, but sometimes struggled with the format moves were read in and out of the program with.
-  Strengths and Weaknesses
   -  One aspect of our program that contributes positively to its functionality would be the heuristic functions used to evaluate which spaces are most advantageous based on not only availability and pure winability, but also the position of each available space as the middle and corner spaces are more highly sought after. The glaring weakness our program has is the use of javaScript making it difficult to debug errors related to our utility function and the referee. 
- A discussion of why the evaluation function and the heuristic(s) you picked are good choices.
   - they are

### Code.  
- To reiterate, this agent was constructed in python and javaScript initially, and then reconstructed into two seperate .js files. Sophie has done her best to clean up the remaining no-longer useful files or libraries, but just in case- all of our agent code can be found in getMoves.js and testAgent.js
- Please ensure you have node.js installed when running our program.
Feel free to access our UTTT agent through our github repository: https://github.com/sophiastrano/project2-AI
All of our agent code is within the uttt_referee_v7 folder, and can be played as described above. 

