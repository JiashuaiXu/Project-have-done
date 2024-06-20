# main.py
from maze import Maze
from dfs_solver import DFSSolver
from bfs_solver import BFSSolver
from aco_solver import AntColony

maze_grid = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
             [1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
             [1,0,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,0,0,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,0,1],
             [1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,1],
             [1,0,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,0,1,1,1,1,1,0,1,0,0,1],
             [1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,1],
             [1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1],
             [1,0,1,0,1,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1],
             [1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1],
             [3,0,1,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,1,0,1,0,9],
             [1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,0,1,1,1,1,1,0,0,1,0,1,0,1,0,1,0,1],
             [1,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,1,0,0,0,0,1,0,1],
             [1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,1,1,1,1,1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,1,1,1,0,1],
             [1,0,0,0,1,0,1,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,0,1,0,1],
             [1,1,1,1,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,1,0,1],
             [1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,0,1,0,1],
             [1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,0,0,1,0,1],
             [1,0,0,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,0,0,1,1,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,0,1,0,1],
             [1,1,1,1,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,1,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,0,1],
             [1,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,1],
             [1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1],
             [1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1],
             [1,0,0,0,1,1,1,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1],
             [1,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,0,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1],
             [1,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,0,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1],
             [1,1,1,1,1,0,1,1,1,0,1,0,0,0,1,1,1,1,1,0,0,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,0,1,1],
             [1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,1],
             [1,0,1,0,1,0,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,1],
             [1,0,1,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,1,0,1,1],
             [1,0,1,0,1,0,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1,0,1,1],
             [1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0,1,1],
             [1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1,0,1,1],
             [1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0,1,1],
             [1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,0,1,0,1,0,1,1],
             [1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1],
             [1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,0,0,1,1,0,0,0,0,1,1],
             [1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,1],
             [1,0,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1],
             [1,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]

maze = Maze(maze_grid)

dfs_solver = DFSSolver(maze)
dfs_path = dfs_solver.solve()
print("DFS Path:", dfs_path)

bfs_solver = BFSSolver(maze)
bfs_path = bfs_solver.solve()
print("BFS Path:", bfs_path)

ant_colony = AntColony(maze, n_ants=10, n_iterations=100, decay=0.1, alpha=1, beta=1)
aco_path, length = ant_colony.run()
print("ACO Path:", aco_path)
print("ACO Path Length:", length)
