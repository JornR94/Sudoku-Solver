# Sudoku-Solver
Sudoku solver written in Python with a simple UI to input the values.

It works for most sudokus, only with difficult sudokus it might become stuck in a recursive loop. This is probably because at that point, you will have to guess a value for a box with, for example, two options. This has not been done and will be possible for further development. 
The procedure would be as follows:
1) Guess a value for a box with two possibilities
2) Store the sudoku as it was before the guess and store the guessed value
3) If an error occurs later on in the sudoku, apparently the guess was wrong and we reset the sudoku to that of step 2. Also, we now set the correct value (the other value in step 1) and go on with solving
