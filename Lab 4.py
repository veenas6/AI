# Implement Adversarial Search using Alpha-Beta Pruning

def alpha_beta(node, alpha, beta, maximizing_player):
    # Check whether node is a terminal node
    if not isinstance(node, list):
        return node

    # MAX player's turn
    if maximizing_player:
        value = float('-inf')

        for child in node:
            value = max(value, alpha_beta(child, alpha, beta, False))
            alpha = max(alpha, value)

            if alpha >= beta:
                print("Pruning at MAX node")
                break

        return value

    # MIN player's turn
    else:
        value = float('inf')

        for child in node:
            value = min(value, alpha_beta(child, alpha, beta, True))
            beta = min(beta, value)

            if alpha >= beta:
                print("Pruning at MIN node")
                break

        return value


# ---------------- Main Program ----------------

print("Enter the game tree in Python list format.")
print("Example: [[[3,5],[6,9]],[[1,2],[0,-1]]]")

game_tree = eval(input("Enter game tree: "))

alpha = float('-inf')
beta = float('inf')

optimal_value = alpha_beta(game_tree, alpha, beta, True)

print("\nOptimal Game Value =", optimal_value)
