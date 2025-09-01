A = int(input("Enter A: "))
B = int(input("Enter B: "))
C = int(input("Enter C: "))

if A <= B and A <= C:
    print("Minimum is:", A)
elif B <= A and B <= C:
    print("Minimum is:", B)
else:
    print("Minimum is:", C)
