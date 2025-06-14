#stone to top of HDPE conversion; needs math update
import math
pipe_od = float(input("What is the OD of the pipe?"))
half_pipe_od = pipe_od / 2
bedding = float(input("What is the depth of bedding stone in feet?"))
total_depth = pipe_od * bedding
width_of_trench = float(input("What is the width of the trench?"))
volume_per_lf = total_depth * width_of_trench * 1 / 27
pipe_volume = math.pi * half_pipe_od**2 * 1 / 27
bedding_backfill = volume_per_lf - pipe_volume
ton_per_lf = bedding_backfill * 1.65
length_of_pipe = float(input("What is the length of the pipe?"))
tons_of_stone = round(ton_per_lf * length_of_pipe, 2)
print(f"Your tonnage is: {tons_of_stone} tons")
