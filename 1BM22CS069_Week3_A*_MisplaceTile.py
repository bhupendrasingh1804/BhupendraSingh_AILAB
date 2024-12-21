class Puzzle:
    def __init__(self, initial_state, goal_state):
        self.board = initial_state
        self.goal = goal_state
        self.n = len(initial_state)
   
    def find_blank(self, board):
        for i in range(self.n):
            for j in range(self.n):
                if board[i][j] == 0:
                    return (i, j)

    def misplaced_tiles(self, board):
        misplaced = 0
        for i in range(self.n):
            for j in range(self.n):
                if board[i][j] != 0 and board[i][j] != self.goal[i][j]:
                    misplaced += 1
        return misplaced
   
    def get_neighbors(self, board):
        neighbors = []
        blank_pos = self.find_blank(board)
        x, y = blank_pos
        
        moves = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        for move in moves:
            new_x, new_y = move
            if 0 <= new_x < self.n and 0 <= new_y < self.n:
                new_board = [row[:] for row in board]  
                
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
            
            open_list.sort(key=lambda x: x[1] + self.misplaced_tiles(x[0]))  
            current_board, g = open_list.pop(0)  
           
            iteration += 1
            print(f"\nIteration {iteration}:")
            self.print_board(current_board)
            print(f"g(n): {g}, h(n): {self.misplaced_tiles(current_board)}, f(n): {g + self.misplaced_tiles(current_board)}")
           
            
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

# Main
if __name__ == "__main__":
    initial_state, goal_state = take_input()
   
    puzzle = Puzzle(initial_state, goal_state)
    moves = puzzle.a_star()

    if moves != -1:
        print(f"\nNumber of moves to solve: {moves}")
    else:
        print("\nNo solution found.")
