# maze.py

class Maze:
    def __init__(self, grid):
        self.grid = grid

    def get_start_position(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == 3:
                    return (i, j)
        return None

    def get_end_position(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == 9:
                    return (i, j)
        return None

    def is_within_bounds(self, x, y):
        return 0 <= x < len(self.grid) and 0 <= y < len(self.grid[0])

    def is_wall(self, x, y):
        return self.grid[x][y] == 1

    def is_end(self, x, y):
        return self.grid[x][y] == 9
