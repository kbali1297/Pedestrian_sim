import numpy as np

def utility(co_or1, co_or2, grid):
    """
    :param co_or1: list of coordinates of Cell 1
    :param co_or2: list of Coordinates of Cell 2
    :param grid: List of Cells row x col
    :return: utility value scalar indicative of how favourable Cell1(pedestrian) location is to Cell2(target)
    """
    grid_size = len(grid)
    co_or1 = np.array(co_or1)
    co_or2 = np.array(co_or2)
    r_2 = np.sum((co_or1-co_or2)**2)
    r_max2 = 2 * grid_size**2

    return np.exp(1.0/(r_2-r_max2)) if r_2<r_max2 else 0

def check_grid_bound(location, grid_size_x, grid_size_y):
    """
    :param location: tuple of coordinate values (x, y) to be checked whether it lies inside the grid or not
    :param grid_size_x: Size of Grid in x direction (Number of Columns)
    :param grid_size_y: Size of Grid in y direction (Number of Rows)
    :return: bool value indicating whether cell lies inside (true) or not (false)
    """
    if location[0] <= 0 or location[0] > grid_size_x or location[1] <= 0 or location[1] > grid_size_y:
        return False
    return True