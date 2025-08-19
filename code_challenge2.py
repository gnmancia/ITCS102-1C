amount = eval(input("Enter amount to deposit : "))

print("\nHere is a breakdown of your deposited amount using the PH denominations\n")

denominations = [1000, 500, 200, 100, 50, 20, 10, 5, 1]

for d in denominations:
    count = amount // d
    amount %= d
    if count > 0:
        print(f"{count} x {d} peso = {count * d}")

