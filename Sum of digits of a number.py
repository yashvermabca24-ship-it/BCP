N = int(input("Enter N: "))
total = 0
while N > 0:
    digit = N % 10
    total += digit
    N //= 10
print("Sum of digits =", total)
