# dfs_solver.py
from maze import Maze

class DFSSolver:
    def __init__(self, maze):
        self.maze = maze
        self.path = []
        self.visited = [[False]*len(maze.grid[0]) for _ in range(len(maze.grid))]

    def solve(self):
        start = self.maze.get_start_position()
        if not start:
            return None
        if self.dfs(start[0], start[1]):
            return self.path
        return None

    def dfs(self, x, y):
        if not self.maze.is_within_bounds(x, y) or self.maze.is_wall(x, y) or self.visited[x][y]:
            return False
        if self.maze.is_end(x, y):
            self.path.append((x, y))
            return True

        self.visited[x][y] = True
        self.path.append((x, y))

        if (self.dfs(x + 1, y) or self.dfs(x - 1, y) or self.dfs(x, y + 1) or self.dfs(x, y - 1)):
            return True

        self.path.pop()
        return False
