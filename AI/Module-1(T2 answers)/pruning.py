# Constants
X = "X"
O = "O"
EMPTY = " "
INFINITY = float("inf")
NEG_INFINITY = -float("inf")

# Initial state
initial_state = [[EMPTY, EMPTY, EMPTY],
                 [EMPTY, EMPTY, EMPTY],
                 [EMPTY, EMPTY, EMPTY]]

# Heuristic evaluation function
def evaluate_state(state):
    if has_won(state, X):
        return 1
    elif has_won(state, O):
        return -1
    else:
        return 0

# Check if a player has won
def has_won(state, player):
    for i in range(3):
        if all(state[i][j] == player for j in range(3)):
            return True
        if all(state[j][i] == player for j in range(3)):
            return True
    if all(state[i][i] == player for i in range(3)):
        return True
    if all(state[i][2 - i] == player for i in range(3)):
        return True
    return False

# Alpha-Beta Pruning algorithm
def minimax_alpha_beta(state, depth, maximizing_player, alpha, beta):
    if terminal_state(state):
        return evaluate_state(state)

    if maximizing_player:
        max_eval = NEG_INFINITY
        for action in possible_actions(state):
            new_state = apply_action(state, action, X)
            eval = minimax_alpha_beta(new_state, depth + 1, False, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = INFINITY
        for action in possible_actions(state):
            new_state = apply_action(state, action, O)
            eval = minimax_alpha_beta(new_state, depth + 1, True, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# Check if the game is over
def terminal_state(state):
    return has_won(state, X) or has_won(state, O) or all(all(cell != EMPTY for cell in row) for row in state)

# Generate possible actions
def possible_actions(state):
    actions = []
    for row in range(3):
        for col in range(3):
            if state[row][col] == EMPTY:
                actions.append((row, col))
    return actions

# Apply an action to the state
def apply_action(state, action, player):
    new_state = [row[:] for row in state]
    row, col = action
    new_state[row][col] = player
    return new_state

# Main function
def main():
    state = initial_state
    while not terminal_state(state):
        print_board(state)
        if len(possible_actions(state)) == 0:
            print("It's a draw!")
            break
        if len(possible_actions(state)) == 1:
            print("Only one move left!")
        row = int(input("Player X: Enter row (0-2): "))
        col = int(input("Player X: Enter column (0-2): "))
        while not (0 <= row <= 2 and 0 <= col <= 2 and state[row][col] == EMPTY):
            print("Invalid move. Try again.")
            row = int(input("Player X: Enter row (0-2): "))
            col = int(input("Player X: Enter column (0-2): "))
        state = apply_action(state, (row, col), X)

        if not terminal_state(state):
            print_board(state)
            if len(possible_actions(state)) == 0:
                print("It's a draw!")
                break
            if len(possible_actions(state)) == 1:
                print("Only one move left!")
            row = int(input("Player O: Enter row (0-2): "))
            col = int(input("Player O: Enter column (0-2): "))
            while not (0 <= row <= 2 and 0 <= col <= 2 and state[row][col] == EMPTY):
                print("Invalid move. Try again.")
                row = int(input("Player O: Enter row (0-2): "))
                col = int(input("Player O: Enter column (0-2): "))
            state = apply_action(state, (row, col), O)

    print_board(state)
    winner = "Player X" if evaluate_state(state) == 1 else "Player O" if evaluate_state(state) == -1 else "No one"
    print(f"{winner} wins!")

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

if __name__ == "__main__":
    main()
