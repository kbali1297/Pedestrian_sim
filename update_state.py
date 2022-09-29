import numpy as np
from utility_functions import *

def update(Grid, pedestrians, target):
    '''
    Grid : List of Cells row X col
    pedestrian : x, y coordinate values of the pedestrian
    '''

    neighbour_locs = np.array([[1, 1], [1, 0], [1, -1], [0, -1], [0, 1], [-1, 1], [-1, 0], [-1, -1]])

    target_loc = np.array([target[0], target[1]])
    pedestrians = np.array(pedestrians)

    row_size = len(Grid)
    col_size = len(Grid[0])

    for p in range(len(pedestrians)):

        pedestrian_loc = np.array([pedestrians[p][0], pedestrians[p][1]])
        max_loc = pedestrian_loc
        present_utility = utility(pedestrian_loc, target_loc, Grid)
        max_utility = present_utility
        for loc in neighbour_locs:
            neighbour_loc = pedestrian_loc + loc
            if check_grid_bound(neighbour_loc, col_size, row_size):
                if Grid[neighbour_loc[1] - 1][neighbour_loc[0] - 1].state == 'target':
                    max_loc = pedestrian_loc
                    break
                elif Grid[neighbour_loc[1] - 1][neighbour_loc[0] - 1].state == 'pedestrian':
                    continue
                neighbour_utility = utility(neighbour_loc, target_loc, Grid)
                if neighbour_utility > max_utility:
                    max_utility = neighbour_utility
                    max_loc = neighbour_loc
        Grid[pedestrian_loc[1] - 1][pedestrian_loc[0] - 1].state = 'empty'
        Grid[max_loc[1] - 1][max_loc[0] - 1].state = 'pedestrian'
        pedestrians[p] = max_loc

    return Grid, pedestrians
