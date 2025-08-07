# Write your solution here
def row_correct(sudoku: list, row_num: int):
    numbers = []
    for num in sudoku[row_num]:
        if num > 0 and num in numbers:
            return False
        numbers.append(num)

    return True

def column_correct(sudoku: list, col_num: int):
    numbers = []
    for row in sudoku:
        num = row[col_num]
        if num > 0 and num in numbers:
            return False
        numbers.append(num)

    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers = []
    for r in range(row_no, row_no+3):
        for s in range(column_no, column_no+3):
            number = sudoku[r][s]
            if number > 0 and number in numbers:
                return False
            numbers.append(number)
 
    return True

def sudoku_grid_correct(sudoku: list):
    for row in range(0,9):
        if not row_correct(sudoku, row):
            return False
    
    for col in range(0,9):
        if not column_correct(sudoku, col):
            return False
    
    for row in range(0,9,3):
        for col in range(0,9,3):
            if not block_correct(sudoku, row, col):
                return False

    return True


if __name__ == "__main__":
    

    sudoku2 = [
        [ 6, 4, 9, 2, 8, 3, 1, 5, 7 ],
        [ 0, 5, 0, 6, 4, 9, 2, 3, 8 ],
        [ 2, 3, 8, 1, 5, 7, 6, 4, 9 ],
        [ 9, 2, 3, 8, 1, 5, 0, 6, 4 ],
        [ 7, 6, 4, 9, 2, 3, 8, 1, 5 ],
        [ 8, 1, 5, 7, 0, 4, 9, 2, 0 ],
        [ 5, 7, 6, 4, 9, 2, 3, 2, 1 ],
        [ 4, 0, 2, 3, 8, 1, 5, 0, 6 ],
        [ 3, 0, 1, 5, 0, 6, 4, 9, 0 ]
        ]
    print(sudoku_grid_correct(sudoku2))