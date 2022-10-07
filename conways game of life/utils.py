# useful functions and constants


### CONSTS
PIXEL_SIZE = 5


### FUNCTIONS
def get_neighbours(row,col,grid,shape):
    """
        returns the sum of the neghbours in a grid given the cell position
    """
    sum = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if not (i ==0 and j ==0):
                sum += grid[((row + i) % shape[0])][((col + j) % shape[1])]
    return sum

def next_gen(grid,shape):
    """
        gets the previous grid and returns the updated gird 
    """
    new_grid = []
    for i in range(shape[0]):
        row = []
        for j in range(shape[1]):
            neighbours =  get_neighbours(i,j,grid,shape)
            
            if neighbours > 3 or neighbours < 2:
                row.append(0)
            elif neighbours == 3 and grid[i][j] == 0:
                row.append(1)
            else:
                row.append(grid[i][j])
        new_grid.append(row)
    return new_grid
