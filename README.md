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
   - The utility function that our program uses
- Our Evaluation Function
   - The evaluation function that our program uses
- The heuristics and/or strategies that you employed to decide how to expand nodes of the minimax tree without exceeding your time limit.
### Results
- describe which tests you ran to try out your program. Did your program play against human players? Did your program play against itself? Did your program play against other programs? How did your program do during those games?
-  Strengths and the weaknesses of your program.
- A discussion of why the evaluation function and the heuristic(s) you picked are good choices.

### Code.  
- The source code for your program
- Ancillary files, if any, that your program requires (e.g., such as a script to run a language interpreter).
Feel free to access our UTTT agent through our github repository: https://github.com/sophiastrano/project2-AI

