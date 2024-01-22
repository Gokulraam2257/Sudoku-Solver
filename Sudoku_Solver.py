N=9

def print_a (arr):
    for i in range(N):
        for j in range(N):
            print(arr[i][j],end=" ")
        print()

def safe(grid,row,col,num):
    
    for x in range(9):
        if grid[row][x] == num:
            return False
    
    for x in range(9):
        if grid[x][col] == num:
            return False
        
    s_row = row -row % 3
    s_col = col -col % 3

    for i in range(3):
        for j in range(3):
            if grid[i + s_row][j+s_col] == num:
                return False
    return True

def solver(grid,row,col):
    if row == N-1 and col == N:
        return True

    if col == N:
        row +=1
        col =0
    if grid[row][col] > 0:
        return solver(grid, row, col + 1)
    for num in range(1, N + 1, 1):
        if safe(grid, row, col, num):
            grid[row][col] = num
            if solver(grid,row,col+1):
                return True
        grid[row][col] = 0
    return False

grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]
print('*'*10+"GIVEN SUDOKU"+'*'*10)
print_a(grid)

if solver(grid,0,0):
    
    print('*'*10+"SOLUTION FOUND"+'*'*10)
    print_a(grid)
else :
    print('*'*10+"NO SOLUTION FOUND"+'*'*10)