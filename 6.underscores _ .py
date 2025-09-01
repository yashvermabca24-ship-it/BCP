
n = int(input("Enter number of underscores in first row: "))
for i in range(n, 0, -1):
    if i == 1:   
        print("*_*")
    else:
        underscores = "_ " * (i - 1)   
        print("* " + underscores + "*")
