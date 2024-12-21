class Puzzle:
    def __init__(self, initial_state, goal_state, heuristic='manhattan'):
        self.board = initial_state
        self.goal = goal_state
        self.n = len(initial_state)
        self.heuristic = heuristic  # heuristic method chosen by user

    def find_blank(self, board):
        for i in range(self.n):
            for j in range(self.n):
                if board[i][j] == 0:
                    return (i, j)

    def manhattan_distance(self, board):
        distance = 0
        for i in range(self.n):
            for j in range(self.n):
                if board[i][j] != 0:
                    goal_x, goal_y = self.find_position(self.goal, board[i][j])
                    distance += abs(i - goal_x) + abs(j - goal_y)
        return distance

    def misplaced_tiles(self, board):
        misplaced = 0
        for i in range(self.n):
            for j in range(self.n):
                if board[i][j] != 0 and board[i][j] != self.goal[i][j]:
                    misplaced += 1
        return misplaced

    def find_position(self, board, value):
        for i in range(self.n):
            for j in range(self.n):
                if board[i][j] == value:
                    return (i, j)

    def get_neighbors(self, board):
        neighbors = []
        blank_pos = self.find_blank(board)
        x, y = blank_pos

        moves = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        for move in moves:
            new_x, new_y = move
            if 0 <= new_x < self.n and 0 <= new_y < self.n:
                new_board = [row[:] for row in board]  # Create a copy of the current board
                new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
                neighbors.append(new_board)
        return neighbors

    def a_star(self):
        start = self.board
        goal = self.goal
        open_list = [(start, 0)]  
        closed_list = set()
        iteration = 0

        while open_list:
            # Choose the heuristic based on user input
            if self.heuristic == 'manhattan':
                open_list.sort(key=lambda x: x[1] + self.manhattan_distance(x[0]))  # Using Manhattan Distance
            elif self.heuristic == 'misplaced':
                open_list.sort(key=lambda x: x[1] + self.misplaced_tiles(x[0]))  # Using Misplaced Tiles

            current_board, g = open_list.pop(0)

            iteration += 1
            print(f"\nIteration {iteration}:")
            self.print_board(current_board)
            print(f"g(n): {g}, h(n): {self.manhattan_distance(current_board) if self.heuristic == 'manhattan' else self.misplaced_tiles(current_board)}, f(n): {g + (self.manhattan_distance(current_board) if self.heuristic == 'manhattan' else self.misplaced_tiles(current_board))}")

            if current_board == goal:
                print("\nGoal reached!")
                return g

            closed_list.add(tuple(map(tuple, current_board)))

            for neighbor in self.get_neighbors(current_board):
                if tuple(map(tuple, neighbor)) in closed_list:
                    continue

                g_new = g + 1
                open_list.append((neighbor, g_new))

        return -1  

    def print_board(self, board):
        for row in board:
            print(" ".join(str(tile) if tile != 0 else "_" for tile in row))

def take_input():
    print("Enter the initial state (3x3 grid) row by row, use '0' for the blank tile:")
    initial_state = []
    for _ in range(3):
        row = list(map(int, input().split()))
        initial_state.append(row)

    print("Enter the goal state (3x3 grid) row by row, use '0' for the blank tile:")
    goal_state = []
    for _ in range(3):
        row = list(map(int, input().split()))
        goal_state.append(row)

    return initial_state, goal_state

def take_heuristic_input():
    print("Choose the heuristic:")
    print("1. Manhattan Distance")
    print("2. Misplaced Tiles")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        return 'manhattan'
    elif choice == '2':
        return 'misplaced'
    else:
        print("Invalid choice, defaulting to Manhattan Distance.")
        return 'manhattan'

# Main
if __name__ == "__main__":
    initial_state, goal_state = take_input()
    heuristic = take_heuristic_input()

    puzzle = Puzzle(initial_state, goal_state, heuristic)
    moves = puzzle.a_star()

    if moves != -1:
        print(f"\nNumber of moves to solve: {moves}")
    else:
        print("\nNo solution found.")
