def extended_euclidean(a, b):
    if b == 0:
        return a, 1, 0
    
    gcd, x1, y1 = extended_euclidean(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

try:
    a = int(input("Enter the first number (a): "))
    b = int(input("Enter the second number (b): "))
    
    if a == 0 and b == 0:
        print("Both numbers cannot be zero.")
    else:
        gcd, x, y = extended_euclidean(abs(a), abs(b))
        
        if a < 0:
            x = -x
        if b < 0:
            y = -y
        
        print(f"GCD({a}, {b}) = {gcd}")
        print(f"Coefficients: x = {x}, y = {y}")
        print(f"Verification: {a}*{x} + {b}*{y} = {a*x + b*y}")
        
except ValueError:
    print("Invalid input. Please enter integers only.")
except RecursionError:
    print("Input too large. Recursion depth exceeded.")
