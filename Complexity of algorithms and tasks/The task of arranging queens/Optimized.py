def n_queens_optimized(n):
    def backtrack(row, cols, diag1, diag2, n):
        if row == n:
            return 1
        
        count = 0
        available_positions = (~(cols | diag1 | diag2)) & ((1 << n) - 1)
        
        while available_positions:
            position = available_positions & -available_positions
            available_positions -= position
            
            count += backtrack(row + 1, 
                             cols | position,
                             (diag1 | position) << 1,
                             (diag2 | position) >> 1,
                             n)
        
        return count
    
    return backtrack(0, 0, 0, 0, n)

n = int(input("Enter board size N: "))
result = n_queens_optimized(n)
print(result)
