def draw(sudoku):
    """Pretty print for sudoku.

    Args:
        sudoku (Individual): Sudoku 9x9 array.

    Prints:
        Sudoku with line-split into 9 boxes and empty (zero) values represented as dots.
    """
    for i,row in enumerate(sudoku):
        for j,e in enumerate(row):
            if e > 0:
                print(e, end=" ")
            else:
                print("·", end=" ")
            if j==8:
                print("")
            elif (j==2) | (j==5):
                print("│", end=" ")
        if (i==2) | (i==5):
            print("──────┼───────┼───────")

   
if __name__ == '__main__':
    
    sudoku = [[9, 4, 8, 4, 8, 8, 0, 5, 1],
              [0, 7, 0, 3, 0, 5, 6, 9, 1],
              [0, 8, 5, 2, 8, 6, 3, 7, 0],
              [9, 3, 0, 4, 9, 2, 0, 1, 0],
              [0, 7, 0, 0, 5, 2, 0, 0, 4],
              [0, 7, 2, 0, 7, 8, 2, 6, 0],
              [4, 6, 0, 5, 2, 5, 0, 0, 1],
              [2, 4, 8, 0, 0, 9, 0, 0, 0],
              [7, 0, 0, 1, 0, 7, 0, 8, 3]]

    draw(sudoku)