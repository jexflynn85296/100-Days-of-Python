#volume of a sphere in feet
import math
radius = int(input("What is your radius?"))
volume = round((4/3) * math.pi * radius**3, 2)
print(f"The volume of the sphere is: {volume}ft3")
