# Constants
X = "X"
O = "O"
EMPTY = " "

# Initial state
initial_state = [[EMPTY, EMPTY, EMPTY],
                 [EMPTY, EMPTY, EMPTY],
                 [EMPTY, EMPTY, EMPTY]]

# Evaluation function
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
        if all(state[i][j] == player for j in range(3)):  #row check
            return True
        if all(state[j][i] == player for j in range(3)): #col check
            return True
    if all(state[i][i] == player for i in range(3)): #\ check
        return True
    if all(state[i][2 - i] == player for i in range(3)): #/check
        return True
    return False

# Minimax algorithm
def minimax(state, depth, maximizing_player):
    if terminal_state(state):
        return evaluate_state(state)

    if maximizing_player:
        max_eval = -float("inf")
        for action in possible_actions(state):
            new_state = apply_action(state, action, X)
            eval = minimax(new_state, depth + 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for action in possible_actions(state):
            new_state = apply_action(state, action, O)
            eval = minimax(new_state, depth + 1, True)
            min_eval = min(min_eval, eval)
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
    print_board(state)
    while not terminal_state(state):
        if len(possible_actions(state)) == 0:
            print("It's a draw!")
            break
        row = int(input("Player X: Enter row (0-2): "))
        col = int(input("Player X: Enter column (0-2): "))
        while not (0 <= row <= 2 and 0 <= col <= 2 and state[row][col] == EMPTY):
            print("Invalid move. Try again.")
            row = int(input("Player X: Enter row (0-2): "))
            col = int(input("Player X: Enter column (0-2): "))
        state = apply_action(state, (row, col), X)
        print_board(state)
        if terminal_state(state):
            winner = "Player X" if evaluate_state(state) == 1 else "Player O" if evaluate_state(state) == -1 else "No one"
            print(f"{winner} wins!")

        if not terminal_state(state):
            row = int(input("Player O: Enter row (0-2): "))
            col = int(input("Player O: Enter column (0-2): "))
            while not (0 <= row <= 2 and 0 <= col <= 2 and state[row][col] == EMPTY):
                print("Invalid move. Try again.")
                row = int(input("Player O: Enter row (0-2): "))
                col = int(input("Player O: Enter column (0-2): "))
            state = apply_action(state, (row, col), O)
            print_board(state)

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

if __name__ == "__main__":
    main()
