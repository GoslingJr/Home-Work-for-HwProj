def reverse_lexicographic_compare(s1, s2):
    return s1[::-1] < s2[::-1]

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

result = reverse_lexicographic_compare(s1, s2)
print(f"'{s1}' < '{s2}'" if result else f"'{s1}' >= '{s2}'")
