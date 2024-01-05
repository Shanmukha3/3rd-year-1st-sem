# app.py

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

def board_print(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end='')
            if j != n-1:
                print(' | ', end='')
        print()

def has_won(board, player, dict, p, q, n):
    c = 0
    for i in range(n):
        if board[p-1][i] == dict[player]:
            c = c + 1
            if c == n:
                print()
                print(dict[player], " has won")
                print()
                return 1
    c = 0
    for i in range(n):
        if board[i][q-1] == dict[player]:
            c = c + 1
            if c == n:
                print()
                print(dict[player], " has won")
                print()
                return 1
    c = 0
    for i in range(n):
        if board[i][i] == dict[player]:
            c = c + 1
            if c == n:
                print()
                print(dict[player], " has won")
                print()
                return 1
    c = 0
    for i in range(n):
        if board[i][n-1-i] == dict[player]:
            c = c + 1
            if c == n:
                print()
                print(dict[player], " has won")
                print()
                return 1
    return 0


def draw(board, n):
    for i in range(n):
        for j in range(n):
            if(board[i][j]==' '):
                return 0
    return 1

def initialize_board(n):
    board = [[' ' for _ in range(n)] for _ in range(n)]
    return board

@app.route('/')
def index():
    n = int(request.args.get('n', 3))  # Default grid size is 3x3
    board = initialize_board(n)
    return render_template('index.html', n=n, board=board)

@app.route('/make_move', methods=['POST'])
def make_move():
    move = request.json
    p, q = move['row'], move['column']
    board[p-1][q-1] = move['player']
    board_print(board, n)
    has_winning = has_won(board, move['player'], dict, p, q, n)
    is_draw = draw(board, n)
    response = {'board': board, 'has_winning': has_winning, 'is_draw': is_draw}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
