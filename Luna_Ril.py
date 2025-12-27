number = input("Enter number: ").strip()

if not number.isdigit():
    print("Error: Input must contain only digits")
else:
    total = 0
    reverse_digits = list(map(int, number))[::-1]
    
    for i, digit in enumerate(reverse_digits):
        if i % 2 == 1:
            doubled = digit * 2
            total += doubled if doubled < 10 else doubled - 9
        else:
            total += digit
    
    is_valid = total % 10 == 0
    print("Valid" if is_valid else "Invalid")