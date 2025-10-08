import math
tool_dia = float(input("Tool Diameter :"))
rad = tool_dia/2
adoc = float(input("ADOC: "))
sfm = float(input("SFM: "))

effective_dia = 2*math.sqrt(pow(rad, 2) - pow(rad-adoc, 2))
rpm = (sfm*3.82)/effective_dia

print(f"Effective Diameter = {effective_dia}\nRPM = {rpm}")