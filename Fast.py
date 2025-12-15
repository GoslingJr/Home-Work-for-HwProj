try:
    base = int(input("Enter base (integer): "))
    exponent = int(input("Enter exponent (non-negative integer): "))
    
    if exponent < 0:
        print("Error: Exponent must be non-negative!")
    else:
        result = 1
        current_base = base
        current_exp = exponent
        
        while current_exp > 0:
            if current_exp % 2 == 1:
                result *= current_base
            current_base *= current_base
            current_exp //= 2
        
        print(f"\nResult: {base}^{exponent} = {result}")
        
        expected = base ** exponent
        if result == expected:
            print(f" Correct: matches built-in calculation")
        else:
            print(f" Error: mismatch with built-in calculation")
            
except ValueError:
    print("Error: Please enter valid integers!")