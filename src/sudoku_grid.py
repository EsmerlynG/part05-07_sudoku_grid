# Write your solution here
def sudoku_grid_correct(sudoku: list):
    block = []
    row_cord = 0
    col_cord = 0
    
    while row_cord < len(sudoku):
        for r in range(row_cord, row_cord+3):
            for c in range(col_cord, col_cord + 3):
                number = sudoku [r][c]
                if number > 0 and number in block:
                    return False
                block.append(number)
                
        
        if col_cord+3 == 9:
            row_cord+=3
            col_cord = 0
        else:
            col_cord += 3
        
        block = []
    
    while row_cord < len(sudoku):
        block = []
        for num in sudoku[row_cord]:
            if num > 0 and num in block:
                return False
            block.append(num)
        row_cord += 1
        
    
    while col_cord < len(sudoku):
        block = []
        for row in sudoku:
            if row[col_cord] > 0 and row[col_cord] in block:
                return False
            block.append(row[col_cord])
        col_cord += 1       

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