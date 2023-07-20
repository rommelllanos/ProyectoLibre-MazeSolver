import matplotlib.pyplot as plt
import numpy as np

#Given a maze and a path, plots a graphical representation
def plot_maze_with_path(maze, path):

    maze_array = np.array(maze)
    
    plot_maze = np.zeros(maze_array.shape, dtype=int)
    
    plot_maze[maze_array == '-'] = 1

    for cell in path:
        plot_maze[cell] = 2
    
    cmap = plt.cm.colors.ListedColormap(['white', 'black', 'gainsboro'])
    
    # Create a plot
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.imshow(plot_maze, cmap=cmap)
    for i in range(maze_array.shape[0]):
        for j in range(maze_array.shape[1]):
            if maze_array[i, j] != '-':
                text = ax.text(j, i, maze_array[i, j],
                               ha="center", va="center", color="grey")
    
    ax.set_xticks([])
    ax.set_yticks([])
    plt.show()


