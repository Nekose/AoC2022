def import_data(datafile:str) -> list:
    grid = []
    with open(datafile) as file:
        for line in file:
            line = line.rstrip("\r\n")
            row = []
            for char in line:
                row.append(int(char))
            grid.append(row)
    return grid

def create_visited_map(grid):
    map = []
    for row in grid:
        line = []
        for _ in row:
            line.append(None)
        map.append(line)
    return map

def check_suroundings(grid,row,col,visited):
    height = grid[row][col]
    if row == 0 or row == len(grid)-1:
        visited[row][col] = True
        return
    elif col == 0 or col == len(grid[0])-1:
        visited[row][col] = True
        return
    north,south,east,west = True,True,True,True
    #west
    for value in grid[row][:col]:
        if value >= height:
            west = False
    #east
    for value in grid[row][col+1:]:
        if value >= height:
            east = False
    #north
    northsouthlist = [x[col] for x in grid]
    for value in northsouthlist[:row]:
        if value >= height:
            north = False
    #south
    for value in northsouthlist[row+1:]:
        if value >= height:
            south = False
    visited[row][col] = any((north,south,east,west))

def score_surroundings(grid,row,col,score_grid):
    height = grid[row][col]
    if row == 0 or row == len(grid)-1:
        score_grid[row][col] = 0
        return
    elif col == 0 or col == len(grid[0])-1:
        score_grid[row][col] = 0
        return
    #look east
    eastview = 0
    eastlist = grid[row][col+1:]
    for value in eastlist:
        if value >= height:
            eastview += 1
            break
        else:
            eastview += 1
    westview = 0
    westlist = grid[row][:col]
    westlist.reverse()
    for value in westlist:
        if value >= height:
            westview += 1
            break
        else:
            westview += 1
    northsouthlist = [x[col] for x in grid]
    northview = 0
    northlist = northsouthlist[:row]
    northlist.reverse()
    for value in northlist:
        if value >= height:
            northview += 1
            break
        else:
            northview += 1
    southview = 0
    southlist = northsouthlist[row+1:]
    for value in southlist:
        if value >= height:
            southview += 1
            break
        else:
            southview += 1
    score_grid[row][col] = northview * southview * eastview * westview

def visit_dem_trees(grid):
    visitedmap = create_visited_map(grid)
    for row,val in enumerate(grid):
        for col,tree in enumerate(val):
            check_suroundings(grid,row,col,visitedmap)
    return visitedmap

def score_dem_trees(grid):
    scoredmap = create_visited_map(grid)
    for row,val in enumerate(grid):
        for col,tree in enumerate(val):
            score_surroundings(grid,row,col,scoredmap)
    return scoredmap

def count_dem_trees(visitedmap):
    trees = 0
    for row in visitedmap:
        for tree in row:
            if tree == True:
                trees += 1
    return trees

def max_score_trees(scored_map):
    return max(max(x for x in row) for row in scored_map)



