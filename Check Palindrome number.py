A = int(input("Enter A: "))
temp = A
rev = 0
while A > 0:
    rev = rev * 10 + (A % 10)
    A //= 10
if rev == temp:
    print("Yes")
else:
    print("No")
