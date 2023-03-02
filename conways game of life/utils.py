import pygame

# cell size
PIXEL_SIZE = 5


# get near neighbors of a speciefic cell
def get_neighbours(row,col,grid,shape):
    """
        returns the sum of the neighbours in a grid given the cell position
    """
    sum = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if not (i ==0 and j ==0):
                sum += grid[((row + i) % shape[0])][((col + j) % shape[1])]
    return sum

# main game of life rules
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


# quad tree alghoritm functions
def count_points_in_bounds(bounds, points):
    count = 0
    for point in points:
        if bounds[0][0] <= point[0] <= bounds[1][0] and bounds[0][1] <= point[1] <= bounds[1][1]:
            count += 1
    print(count)
    return count

def draw_quad_lines(bounds, window, color=(255,255,255)):
    x_mid = (bounds[0][0] + bounds[1][0]) / 2
    y_mid = (bounds[0][1] + bounds[1][1]) / 2

    # Draw the two lines that split the square
    pygame.draw.line(window, color, (bounds[0][0], y_mid), (bounds[1][0], y_mid))
    pygame.draw.line(window, color, (x_mid, bounds[0][1]), (x_mid, bounds[1][1]))

def quadtree(bounds, points, window,depth=0,):
    if depth == 5 or count_points_in_bounds(bounds,points) < 1:
        return points
    
    x_mid = (bounds[0][0] + bounds[1][0]) / 2
    y_mid = (bounds[0][1] + bounds[1][1]) / 2

    top_left = []
    top_right = []
    bottom_left = []
    bottom_right = []
    
    for point in points:
        if point[0] < x_mid and point[1] < y_mid:
            top_left.append(point)
        elif point[0] < x_mid and point[1] >= y_mid:
            bottom_left.append(point)
        elif point[0] >= x_mid and point[1] < y_mid:
            top_right.append(point)
        else:
            bottom_right.append(point)
            
    draw_quad_lines(bounds,window)
    
    quadtree(bounds=[(bounds[0][0], bounds[0][1]), (x_mid, y_mid)], points=top_left, depth=depth+1,window=window)
    quadtree(bounds=[(x_mid, bounds[0][1]),( bounds[1][0], y_mid)], points=top_right, depth=depth+1,window=window)
    quadtree(bounds=[(bounds[0][0], y_mid),( x_mid, bounds[1][1])], points=bottom_left, depth=depth+1,window=window)
    quadtree(bounds=[(x_mid, y_mid), (bounds[1][0], bounds[1][1])], points=bottom_right, depth=depth+1,window=window)

