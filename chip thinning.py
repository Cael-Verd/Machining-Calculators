import math

tool_dia = float(input("Tool Diameter: "))
ipt = float(input("ipt: "))
adoc = float(input("ADOC: "))
rdoc = float(input("RDOC: "))
sfm = float(input("SFM: "))
flute_num = int(input("Number of flutes: "))
unit_power = float(input("Unit Power: "))

ipt_adj = round((ipt*(tool_dia/2))/math.sqrt((tool_dia*rdoc) - pow(rdoc, 2)), 4)

rpm = (sfm*3.82)/tool_dia
ipm = rpm*ipt_adj*flute_num
mrr = rdoc*adoc*ipm
hp = mrr*unit_power


print(f"IPT = {ipt_adj}\nRPM = {rpm}\nIPM = {ipm}\nMRR = {mrr}\nHP = {hp}")