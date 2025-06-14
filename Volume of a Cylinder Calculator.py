#volume of a cylinder in feet
import math
radius = int(input("What is the radius?"))
height = int(input("What is the height?"))
volume = round(math.pi * radius**2 * height, 2)
print(f"The volume of your cylinder is: {volume}ft3")

