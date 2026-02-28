def extended_euclidean(a, b):
    """
    Extended Euclidean algorithm.
    
    Returns (gcd, x, y) such that:
    a * x + b * y = gcd(a, b)
    """
    if b == 0:
        # Base case: when b is 0, gcd is a, and coefficients are 1 and 0
        return a, 1, 0
    
    # Recursively compute gcd and coefficients for smaller problem
    gcd, prev_x, prev_y = extended_euclidean(b, a % b)
    
    # Update coefficients using the recurrence relation:
    # x = previous_y
    # y = previous_x - (a // b) * previous_y
    current_x = prev_y
    current_y = prev_x - (a // b) * prev_y
    
    return gcd, current_x, current_y


def adjust_coefficients_for_negative_inputs(a, b, x, y):
    """
    Adjust Bezout coefficients when original inputs were negative.
    
    If a < 0, we need to flip the sign of x coefficient.
    If b < 0, we need to flip the sign of y coefficient.
    This ensures the equation a*x + b*y = gcd holds for negative inputs.
    """
    if a < 0:
        x = -x
    if b < 0:
        y = -y
    return x, y


def main():
    """
    Main function to execute extended Euclidean algorithm with user input.
    """
    try:
        # Get user input for the two numbers
        a = int(input("Enter the first number (a): "))
        b = int(input("Enter the second number (b): "))
        
        # Handle special case where both numbers are zero
        if a == 0 and b == 0:
            print("Both numbers cannot be zero.")
            return
        
        # Compute GCD and Bezout coefficients using absolute values
        # The algorithm works with positive numbers, we'll adjust signs later
        gcd, x_coeff, y_coeff = extended_euclidean(abs(a), abs(b))
        
        # Adjust coefficients based on original signs of inputs
        x_coeff, y_coeff = adjust_coefficients_for_negative_inputs(a, b, x_coeff, y_coeff)
        
        # Display results
        print(f"GCD({a}, {b}) = {gcd}")
        print(f"Bezout coefficients: x = {x_coeff}, y = {y_coeff}")
        
        # Verify the result by checking Bezout's identity
        verification = a * x_coeff + b * y_coeff
        print(f"Verification of Bezout's identity: {a}*{x_coeff} + {b}*{y_coeff} = {verification}")
        
        if verification != gcd:
            print("Warning: Verification failed! Something went wrong.")
        
    except ValueError:
        print("Invalid input. Please enter integers only.")
    except RecursionError:
        print("Input too large. Recursion depth exceeded.")


if __name__ == "__main__":
    main()
