import re

file_name = "sample2.txt"
file_name = "data.txt"

safe_count = 0
with open(file_name, "r") as file:
    input = file.read()

do_locs = [m.start() for m in re.finditer(r"do\(\)", input)]
dont_locs = [m.start() for m in re.finditer(r"don't\(\)", input)]

working_string = ""

working = 0
while do_locs and dont_locs:
    dn_loc = dont_locs.pop(0)
    working_string += input[working:dn_loc]
    while do_locs and working < dn_loc:
        working = do_locs.pop(0) + 4

if not dont_locs:
    working_string += input[working:]

valid_mul_re = r"mul\(\d{1,3}\,\d{1,3}\)"
valid_input = re.findall(valid_mul_re, working_string)

mul_sum = 0

for mul in valid_input:
    mul = mul[4:-1]
    mul_vals = mul.split(",")
    mul_sum += int(mul_vals[0]) * int(mul_vals[1])

print(mul_sum)
