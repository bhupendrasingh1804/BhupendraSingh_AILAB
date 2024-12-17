import math
import sys

def alpha_beta_pruning(depth, node_index, is_max, values, alpha, beta, max_depth):
    if depth == max_depth:
        return values[node_index]

    if is_max:
        best = -sys.maxsize
        for i in range(2):
            child = node_index * 2 + i
            val = alpha_beta_pruning(depth + 1, child, False, values, alpha, beta, max_depth)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                print(f"Pruned subtree at node: {child} (alpha={alpha}, beta={beta})")
                break
        return best
    else:
        best = sys.maxsize
        for i in range(2):
            child = node_index * 2 + i
            val = alpha_beta_pruning(depth + 1, child, True, values, alpha, beta, max_depth)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                print(f"Pruned subtree at node: {child} (alpha={alpha}, beta={beta})")
                break
        return best

if __name__ == "__main__":
    values = [3, 5, 6, 9, 1, 2, 0, 4]
    max_depth = int(math.log2(len(values)))
    alpha = -sys.maxsize
    beta = sys.maxsize
    print("Starting Alpha-Beta Pruning...\n")
    optimal_value = alpha_beta_pruning(0, 0, True, values, alpha, beta, max_depth)
    print("\nThe optimal value for the root MAX node is:", optimal_value)
