import random

def initial_state(n):
    """
    Generates a random initial state with n queens placed on the board.
    Each queen is represented by its column index in a row.
    
    Arguments:
    n -- The number of queens (and the size of the board).
    
    Returns:
    A list representing the initial state.
    """
    return [random.randint(0, n - 1) for _ in range(n)]

def successors(state):
    """
    Generates all possible successors by moving each queen to a different column.
    
    Arguments:
    state -- The current state of the board.
    
    Returns:
    A list of new states (neighbors).
    """
    neighbors = []
    n = len(state)
    
    for row in range(n):
        for col in range(n):
            if col != state[row]:  
                new_state = state[:]  
                new_state[row] = col  
                neighbors.append(new_state) 
    
    return neighbors

def value(state):
    """
    Calculates the number of attacking pairs of queens in the current state.
    
    Arguments:
    state -- The current state of the board.
    
    Returns:
    The number of attacking pairs.
    """
    conflicts = 0
    n = len(state)
    
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                
                conflicts += 1
    
    return conflicts

def best_successor(state):
    """
    Finds the neighbor with the lowest number of conflicts.
    
    Arguments:
    state -- The current state of the board.
    
    Returns:
    The best neighboring state.
    """
    neighbors = successors(state)
    best_neighbor = state  
    lowest_value = value(state) 
    
    for neighbor in neighbors:
        neighbor_value = value(neighbor)
        if neighbor_value < lowest_value:
            lowest_value = neighbor_value
            best_neighbor = neighbor  
    
    return best_neighbor

def print_board(state):
    """
    Prints the board state with queens and empty spaces.
    
    Arguments:
    state -- The current state of the board.
    """
    n = len(state)
    board = []
    for row in range(n):
        line = ['.'] * n  
        line[state[row]] = 'Q'  
        board.append(' '.join(line))  
    
    print("\n".join(board))  

def hill_climbing_n_queens(n):
    """
    Solves the N-Queens problem using the Hill Climbing algorithm.
    
    Arguments:
    n -- The number of queens (and the size of the board).
    
    Returns:
    A state that is a local maximum (ideally a solution).
    """
    current_state = initial_state(n)  
    iterations = 0  
    
    while True:
        iterations += 1
        neighbor = best_successor(current_state)  
        
        print(f"Iteration {iterations}:")
        print_board(current_state)  
        print(f"Attacking pairs: {value(current_state)}\n")
        
        if value(neighbor) >= value(current_state):  
            print(f"Final state after {iterations} iterations:")
            print_board(current_state)  
            print(f"Attacking pairs: {value(current_state)}")
            return current_state  
        
        current_state = neighbor  

if __name__ == "__main__":
    
    n = int(input("Enter the number of queens (N): "))
    
    
    solution = hill_climbing_n_queens(n)
    
    
    print("Solution state (column positions of queens):", solution)
    print("Number of attacking pairs:", value(solution))
    
    
    if value(solution) == 0:
        print("Found a valid solution!")
    else:
        print("No valid solution found. This is a local maximum.")
