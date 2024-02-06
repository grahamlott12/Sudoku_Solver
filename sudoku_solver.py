
grid = [
    [0,4,0,6,0,8,0,0,0],
    [0,0,0,0,2,4,0,6,7],
    [3,6,0,0,0,0,4,2,0],
    [0,1,0,4,6,0,5,0,9],
    [8,0,0,0,0,9,0,4,3],
    [0,9,0,0,0,0,0,7,0],
    [0,0,0,0,9,0,0,0,0],
    [0,0,0,2,4,3,8,9,1],
    [9,0,1,0,8,0,0,0,0]
]

def display_grid(grid):

    for i in range(len(grid)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")

        for j in range(len(grid[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end = "")

            if j == 8:
                print(grid[i][j])
            
            else:
                print(str(grid[i][j]) + " ", end = "")


def find_empty_space(grid):
    #Finds the first empty cell in the grid

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return (i, j)
    
    return None

def is_valid(grid, pos, num):
    #Checks if the number is already present in the row, column, or 3x3 box it is in

    #Checks row 
    for i in range(0, len(grid)):
        if grid[pos[0]][i] == num and pos[1] != i:
            return False

    #Checks column
    for i in range(0, len(grid)):
        if grid[i][pos[1]] == num and pos[0] != i:
            return False

    
    #Checks 3x3 box
    x = pos[1] // 3
    y = pos[0] // 3

    for i in range(y*3, y*3 + 3):
        for j in range(x*3, x*3 + 3):
            if grid[i][j] == num and (i, j) != pos:
                return False

    return True


def solve(grid):
    find = find_empty_space(grid)

    #If there are no empty cells, the Sudoku is solved
    if find:
        row, col = find
    else:
        return True

    #Tries to fill empty cell with a number and places the number if it is valid
    for num in range(1, 10):
        if is_valid(grid, (row, col), num):
            grid[row][col] = num
        
            #Attempts to recursively solve the rest of the Sudoku
            if solve(grid):
                return True

            #Backtracks if the current number does not lead to a solution
            grid[row][col] = 0

    return False

print("     Starting Sudoku")
display_grid(grid)
solve(grid)
print(" ")
print("     Solved Sudoku")
display_grid(grid)