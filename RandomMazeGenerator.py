import random


def randomMaze(n):
    # Initialize an empty maze
    mazeN = []

    # Loop to create rows
    for i in range(n):
        # Initialize an empty row
        row = []

        # Loop to create columns
        for j in range(n):
            # Randomly assign a value to the cell
            cell = random.choice(["-", 0, 1, 2, 3])

            # Append the cell to the row
            row.append(cell)

        # Append the row to the maze
        mazeN.append(row)

    return mazeN
