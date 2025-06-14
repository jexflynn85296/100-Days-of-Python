#tons for rock in feet
area = float(input("What is you area?"))
depth = float(input("What is your depth in feet?"))
cubic_conversion = 27
ton_conversion = 1.5
volume = round(area * depth / cubic_conversion * ton_conversion, 2)
print(f"The amount of tons you would need is: {volume} tons")


