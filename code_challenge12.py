n = 6   
for i in range(1, n+1):
    print("  " * (n - i), end="")  
    for j in range(i, 1, -1):
        print(j, end=" ")
    print("1", end=" ")
    for j in range(2, i+1):
        print(j, end=" ")
    print()
