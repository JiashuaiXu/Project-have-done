# aco_solver.py
import numpy as np
from maze import Maze

class AntColony:
    def __init__(self, maze, n_ants, n_iterations, decay, alpha=1, beta=1):
        self.maze = maze
        self.start = self.maze.get_start_position()
        self.end = self.maze.get_end_position()
        self.n_ants = n_ants
        self.n_iterations = n_iterations
        self.decay = decay
        self.alpha = alpha
        self.beta = beta
        self.pheromone = np.ones((len(maze.grid), len(maze.grid[0]))) * 0.1
        for i in range(len(maze.grid)):
            for j in range(len(maze.grid[0])):
                if maze.grid[i][j] == 1:
                    self.pheromone[i][j] = 0

    def run(self):
        shortest_path = None
        best_length = float('inf')
        for iteration in range(self.n_iterations):
            paths = []
            path_lengths = []
            for ant in range(self.n_ants):
                path, length = self.construct_path()
                paths.append(path)
                path_lengths.append(length)
                if length < best_length:
                    best_length = length
                    shortest_path = path
            self.update_pheromone(paths, path_lengths)
        return shortest_path, best_length

    def construct_path(self):
        path = [self.start]
        visited = set(path)
        current = self.start
        while current != self.end:
            next_moves = self.possible_moves(current, visited)
            if not next_moves:
                break
            next_move = self.choose_next_move(next_moves)
            path.append(next_move)
            visited.add(next_move)
            current = next_move
        return path, len(path)

    def possible_moves(self, current, visited):
        moves = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in directions:
            nx, ny = current[0] + dx, current[1] + dy
            if (nx, ny) not in visited and self.maze.is_within_bounds(nx, ny) and not self.maze.is_wall(nx, ny):
                moves.append((nx, ny))
        return moves

    def choose_next_move(self, moves):
        probabilities = [self.pheromone[move] ** self.alpha * ((1.0 / (1 + self.maze.grid[move[0]][move[1]])) ** self.beta) for move in moves]
        probabilities_sum = sum(probabilities)
        probabilities = [p / probabilities_sum for p in probabilities]
        return moves[np.argmax(probabilities)]

    def update_pheromone(self, paths, path_lengths):
        self.pheromone *= (1 - self.decay)
        for path, length in zip(paths, path_lengths):
            for step in path:
                self.pheromone[step[0]][step[1]] += (1.0 / length)
