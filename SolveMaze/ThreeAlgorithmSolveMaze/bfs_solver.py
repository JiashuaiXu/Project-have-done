# bfs_solver.py
from collections import deque
from maze import Maze

class BFSSolver:
    def __init__(self, maze):
        self.maze = maze

    def solve(self):
        start = self.maze.get_start_position()
        if not start:
            return None
        return self.bfs(start[0], start[1])

    def bfs(self, start_x, start_y):
        queue = deque([(start_x, start_y, [(start_x, start_y)])])
        visited = [[False] * len(self.maze.grid[0]) for _ in range(len(self.maze.grid))]
        visited[start_x][start_y] = True
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            x, y, path = queue.popleft()

            if self.maze.is_end(x, y):
                return path

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if self.maze.is_within_bounds(nx, ny) and not visited[nx][ny] and not self.maze.is_wall(nx, ny):
                    visited[nx][ny] = True
                    queue.append((nx, ny, path + [(nx, ny)]))
        return None
