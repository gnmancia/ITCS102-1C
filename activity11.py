temp = eval(input("Enter Temperature outside --> "))
#input 33
if temp >= 1 and temp <= 20:
    print("Temperature is Considered as Freezing Temperature")
elif temp <= 21 and temp <= 30:
    print("Temperature is Considered as Extremely Cold")
elif temp <= 31 and temp <= 37:
    print("Temperature is Considered as Moderately Cold")
elif temp <= 38 and temp <= 45:
    print("Temperature is Considered as Lukewarm")
elif temp >= 45 and temp <= 50:
    print("Temperature is Considered as Boiling Hot")
elif temp >= 51 and temp <= 1000:
    print("Temperature is Considered as Dangerous Temperature")
else:
    print("Invalid Temperature")
