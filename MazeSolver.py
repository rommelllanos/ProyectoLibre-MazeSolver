from RandomMazeGenerator import randomMaze
from MazeSolverWithAStarSearch import MazeSolverWithAStarSearch
from MazeSolverWithBFS import MazeSolverWithBFS
from MazeSolverWithDFS import MazeSolverWithDFS
from MazeSolverWithUniformCostSearch import MazeSolverWithUniformCost

def menu():
    print("Welcome to the Maze Solver!")
    print("Lets generate a random NxN maze")
    N = input("Enter your N : ")

    maze = randomMaze(int(N))
    print("Your random maze generated is ")
    print(maze)

    print("Choose the start cell:")
    X1 = int(input("X: "))
    Y1 = int(input("Y: "))

    print("Choose the end cell:")
    X2 = int(input("X: "))
    Y2 = int(input("Y: "))

    print("Choose a method: ")
    print("1. A*")
    print("2. BFS")
    print("3. DFS")
    print("4. Uniform Cost Search")
    print("5. Exit program")

    option = input("Enter your option: ")

    if option == "1":
        print("You selected A*.")
        mazeSolver = MazeSolverWithAStarSearch(maze,(X1,Y1),(X2,Y2))
        mazeSolver.astarSearch()

    elif option == "2":
        print("You selected BFS.")
        mazeSolver = MazeSolverWithBFS(maze,(X1,Y1),(X2,Y2))
        mazeSolver.breathFirstSearchAlgorithm()

    elif option == "3":
        print("You selected DFS.")
        mazeSolver = MazeSolverWithDFS(maze,(X1,Y1),(X2,Y2))
        mazeSolver.depthFirstSearchAlgorithm()

    elif option == "4":
        print("You selected Uniform Cost Search")
        mazeSolver = MazeSolverWithUniformCost(maze,(X1,Y1),(X2,Y2))
        mazeSolver.uniformCost()

    elif option == "5":
        exit(0)
    else:
        print("Invalid option. Please try again.")
        menu()
    

# Call the menu function
menu()
