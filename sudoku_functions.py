def is_solved(sudoku):
    for i in range(0, 9):
        for j in range(0, 9):
            if sudoku[i][j] == 0 or isinstance(sudoku[i][j], list):
                return False
    return True

# def check_for_fill(char):
#     for row in range(1, 9):
#         for column in range(1, 9):
#             print("row:")


def is_zero(character):
    return character == 0


def input_valid(input_user):
    return len(input_user) == 81


def on_line_hor(sudoku, value, value_hor):
    for i in range(0, 9):
        if sudoku[value_hor][i] == value:
            return True
    return False


def on_line_ver(sudoku, value, value_ver):
    for i in range(0, 9):
        if sudoku[i][value_ver] == value:
            return True
    return False


def in_block(sudoku, value, place_y, place_x):
    block_y = determine_block_place(place_y)
    block_x = determine_block_place(place_x)
    for i in range(0, 3):
        for j in range(0, 3):
            ii = i + block_y
            jj = j + block_x
            # print("jj is %s, ii is %s, value is %s" % (jj, ii, sudoku[ii][jj]))
            if sudoku[ii][jj] == value:
                return True
    return False


def only_possibility_in_block(sudoku, value, place_y, place_x):
    block_y = determine_block_place(place_y)
    block_x = determine_block_place(place_x)
    for i in range(0, 3):
        for j in range(0, 3):
            y = i + block_y
            x = j + block_x
            # print("jj is %s, ii is %s, value is %s" % (jj, ii, sudoku[ii][jj]))
            if sudoku[y][x] == value:
                return False
            if isinstance(sudoku[y][x], list) and value in sudoku[y][x]:
                if place_x != x or place_y != y:
                    return False
    return True


def determine_block_place(place):
    if place < 3:
        return 0
    elif place < 6:
        return 3
    else:
        return 6


