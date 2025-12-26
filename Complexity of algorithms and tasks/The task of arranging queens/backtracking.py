def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or \
           abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_n_queens(board, row, n, count):
    if row == n:
        return count + 1
    
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            count = solve_n_queens(board, row + 1, n, count)
    
    return count

def n_queens_recursive(n):
    board = [-1] * n
    return solve_n_queens(board, 0, n, 0)

if __name__ == "__main__":
    n = int(input("Enter board size N: "))
    result = n_queens_recursive(n)
    print(result)
