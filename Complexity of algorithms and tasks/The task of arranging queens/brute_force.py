import itertools

def is_valid_board(board, n):
    for i in range(n):
        for j in range(i + 1, n):
            if abs(i - j) == abs(board[i] - board[j]):
                return False
    return True

def n_queens_bruteforce(n):
    if n < 1 or n > 10:
        return 0
    
    count = 0
    all_permutations = itertools.permutations(range(n))
    
    for permutation in all_permutations:
        if is_valid_board(permutation, n):
            count += 1
    
    return count

if __name__ == "__main__":
    n = int(input("Enter board size N: "))
    result = n_queens_bruteforce(n)
    print(result)8
