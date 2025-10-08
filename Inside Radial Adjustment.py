import math

circle_dia = float(input("Circle Diameter"))
tool_dia = float(input("Tool Diameter: "))
ipt = float(input("ipt: "))

radial_adjustment = ((circle_dia-tool_dia)*ipt)/circle_dia

print(f"Radial Adjustment = {radial_adjustment}")