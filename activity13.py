#Ask: user to input ten 10 numbers
#After get the summation of all the numbers provided

for x in range(1, 11, 1):
    sum = 0
    print(x)
    number = eval(input("Enter any number --> "))
    sum += number
print("\n\tThe sum of all the number given is ",sum)