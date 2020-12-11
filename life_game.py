import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

line = 200
column = 200
dead = 0
alive = 1
iterations = 300

grid = np.zeros((line, column), dtype=int)
grid[:,99:101] = 1

colors = ["white", "black"]
cmap = ListedColormap(colors)

# initialise la fenêtre d'affichage de la figure
fig = plt.gcf()
fig.show()
fig.canvas.draw()


def choose_event(grid: np.ndarray, x: int, y: int) -> int:
    cell = grid[x, y]
    nb_neighbor = number_neighbor(grid, x, y)
    is_dead = cell == dead
    is_alive = cell == alive
    if is_dead and nb_neighbor == 3:
        return alive
    elif is_alive and (nb_neighbor == 2 or nb_neighbor == 3):
        return alive
    else:
        return dead


def number_neighbor(grid: np.ndarray, x: int, y: int) -> int:
    return sum([valid(grid, x - 1, y - 1), valid(grid, x - 1, y), valid(grid, x - 1, y + 1),
                valid(grid, x, y - 1), valid(grid, x, y + 1),
                valid(grid, x + 1, y - 1), valid(grid, x + 1, y), valid(grid, x + 1, y + 1)])


def valid(grid, x, y) -> int:
    try:
        return grid[x, y]
    except IndexError:
        return 0


for _ in range(iterations):
    fig.clear()
    plt.imshow(grid, cmap=cmap)
    plt.axis('off')
    # plt.show()
    fig.canvas.draw()
    plt.pause(0.1)
    temp_grid = np.zeros((line, column), dtype=int)
    for i in range(line):
        for j in range(column):
            temp_grid[i, j] = choose_event(grid, i, j)
    grid = temp_grid[:,:]

plt.show()
