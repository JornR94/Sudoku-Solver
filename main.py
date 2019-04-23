import sudoku_functions as helper  # helper functions
from tkinter import *  # GUI package


# container for the puzzle, initially all values are 0:
sudoku = [[0 for x in range(0, 9)] for y in range(0, 9)]
sudoku_backup = [[0 for x in range(0, 9)] for y in range(0, 9)]
# Array for storing the input:
input_user = [0 for x in range(0, 81)]
# Initialise array for input
entries = [[0 for x in range(0, 9)] for y in range(0, 9)]


# Setting up UI:
GUI = Tk()
GUI.geometry('500x500')
GUI.title("Sudoku Solvert")

for row in range(0, 9):
    for col in range(0, 9):
        entries[row][col] = Text(GUI, font=("Courier", 16), width=4, height=2)
        entries[row][col].grid(column=col, row=row)


def clicked():
    parse_input()
    solve()


def parse_input():
    count = -1
    for row in range(0, 9):
        for col in range(0, 9):
            count += 1
            input_given = 0
            try:
                input_given = int(entries[row][col].get("1.0", END))
                print("Input %s, %s" % (input_given, count))
            except ValueError:
                print("Input 0, %s" % count)
            input_user[count] = input_given


btn = Button(GUI, text="Solve!", command=clicked)
btn.grid(column=4, row=9)

# input_user = input("Input the sudoku from top left to right \nInput a zero if the value is unknown: ")
# print(" Input: " , input_user)


# Parses the input into the sudoku double array
def fill_sudoku():
    count = -1
    for i in range(0, 9):
        for j in range(0, 9):
            count += 1
            sudoku[i][j] = int(input_user[count])
            print("filled in %s in the sudoku array at place %s %s, count: %s" % (sudoku[i][j], i, j, count))


# Converts the array into a string representation for debugging
def array_to_string(arr):
    for i in range(0, 9):
        print()
        for j in range(0, 9):
            sys.stdout.write(str(arr[i][j]))
            sys.stdout.write(' ')
    print()


# Initialises the sudoku double array with arrays at places where
# the number is not known yet
def init_sudoku():
    for vert in range(0, 9):
        for hor in range(0, 9):
            if sudoku[vert][hor] == 0:
                sudoku[vert][hor] = []


# Method to solve the sudoku
def solve():
    fill_sudoku()
    print("Given sudoku:")
    array_to_string(sudoku)
    print("============= SOLVING SUDOKU NOW ===========")
    init_sudoku()
    while not helper.is_solved(sudoku):
        update_sudoku()
    print("============= SOLVED SUDOKU! ===========")
    print("Solved sudoku result:")
    array_to_string(sudoku)
    display_result()


# Updates the sudoku by checking possibilities and consequently
# checking these possibilities
def update_sudoku():
    updated = False
    for vert in range(0, 9):
        for hor in range(0, 9):
            if isinstance(sudoku[vert][hor], list):
                sudoku[vert][hor].clear()  # First clear out the array
                for value in range(1, 10):
                    if not (helper.in_block(sudoku, value, vert, hor) or helper.on_line_hor(sudoku, value, vert)
                            or helper.on_line_ver(sudoku, value, hor)):
                        print("adding %s to the array at sudoku[%s][%s]" % (value, vert, hor))
                        sudoku[vert][hor].append(value)
            if isinstance(sudoku[vert][hor], list) and len(sudoku[vert][hor]) == 1:
                sudoku[vert][hor] = sudoku[vert][hor].pop()
                print("sudoku at %s %s had one element: %s" % (vert, hor, sudoku[vert][hor]))
                print("set to element now: " + str(type(sudoku[vert][hor])))
                updated = True
    for vert in range(0, 9):
        for hor in range(0, 9):
            if isinstance(sudoku[vert][hor], list):
                for value in sudoku[vert][hor]:
                    if helper.only_possibility_in_block(sudoku, value, vert, hor):
                        print("sudoku at %s %s had one option: %s" % (vert, hor, value))
                        sudoku[vert][hor] = value
                        updated = True
    if not updated:
        create_backup()
        # TODO add method that chooses one of the two options for random array with two elements
        # if that gives errors, the other element should have been chosen (so keep old sudoku)


def create_backup():
    for y in range(0, 9):
        for x in range(0, 9):
            sudoku_backup[x][y] = sudoku[x][y]


def display_result():
    for row in range(0, 9):
        for col in range(0, 9):
            entries[row][col] = Text(GUI, font=("Courier", 16), width=4, height=2)
            entries[row][col].grid(column=col, row=row)
            entries[row][col].insert(END, str(sudoku[row][col]))


GUI.mainloop()

# solve()

# print(" ----------------- tests ---------------------- ")
# print(helper.on_line_hor(sudoku, 4, 0))
#
# init_sudoku()
# # update_sudoku()
#
# print("TEST BLOCK sudoku[0][1]: ", helper.in_block(sudoku, 4, 0, 1))
# print("TEST BLOCK sudoku[0][1]: ", helper.in_block(sudoku, 4, 0, 1))
# print("TEST BLOCK sudoku[0][1]: ", helper.in_block(sudoku, 6, 0, 1))
# print("TEST BLOCK sudoku[3][0]: ", helper.in_block(sudoku, 9, 3, 0))
# print("TEST BLOCK sudoku[3][1]: ", helper.in_block(sudoku, 5, 3, 1))
#
# print("TEST HOR line 1: ", helper.on_line_hor(sudoku, 1, 0))
# print("TEST VER line 3: ", helper.on_line_ver(sudoku, 1, 2))
# print("TEST VER line 3: ", helper.on_line_ver(sudoku, 2, 2))
# print("TEST VER line 4: ", helper.on_line_ver(sudoku, 4, 3))
#
# # print(helper.in_block(sudoku, 4, 0, 3) or helper.on_line_hor(sudoku, 4, 0)
# #                             or helper.on_line_ver(sudoku, 4, 3))
#
# # # check for place 2,2 to see if only 1 fits:
# # for i in range(0, 9):
# #     if not (helper.in_block(sudoku, i+1, 2, 2) or helper.same_on_line_hor(sudoku, i+1, 2) or helper.same_on_line_ver(sudoku, i+1, 2)):
# #         print("adding %s to the array" % (i+1))
# #         sudoku[2][2].append(i+1)
#
#
# # solve(input_user)
# # else:
# #     print("Input is invalid...")
#
# update_sudoku()
# print("==============NEW ROUND============")
# # print("TEST POSSIBILITY: " + str(helper.only_possibility_in_block(sudoku, 1, 2, 2)))
# # print("TEST POSSIBILITY: " + str(helper.only_possibility_in_block(sudoku, 1, 7, 5)))
# # print("TEST POSSIBILITY: " + str(helper.only_possibility_in_block(sudoku, 1, 8, 5)))
# # for value in sudoku[2][2]:
# #     print(str(value))
# # print("--")
# # for value in sudoku[7][5]:
# #     print(str(value))
# # print("--")
# # for value in sudoku[8][5]:
# #     print(str(value))
# update_sudoku()
# # array_to_string(sudoku)


