import copy


def spread_fire(grid):
    """Update the forest grid based on fire spreading rules."""
    grid_size = len(grid)  # Get grid size dynamically
    update_grid = copy.deepcopy(grid)
    
    for i in range(grid_size):  # Update loop range to include the last row/column
        for j in range(grid_size):  # Update loop range to include the last row/column
            if grid[i][j] == 1:
                neighbors = []
                
                # Check the neighbors safely by ensuring indices are within bounds
                if i > 0:  # Up
                    neighbors.append(grid[i-1][j])
                if i < grid_size - 1:  # Down
                    neighbors.append(grid[i+1][j])
                if j > 0:  # Left
                    neighbors.append(grid[i][j-1])
                if j < grid_size - 1:  # Right
                    neighbors.append(grid[i][j+1])

                # If any neighbor is on fire, spread the fire to the tree
                if 2 in neighbors:
                    update_grid[i][j] = 2

    return update_grid




