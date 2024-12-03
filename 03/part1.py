import re

file_name = "sample.txt"
file_name = "data.txt"

safe_count = 0
with open(file_name, "r") as file:
    input = file.read()

valid_mul_re = r"mul\(\d{1,3}\,\d{1,3}\)"
valid_input = re.findall(valid_mul_re, input)

mul_sum = 0

for mul in valid_input:
    mul = mul[4:-1]
    mul_vals = mul.split(",")
    mul_sum += int(mul_vals[0]) * int(mul_vals[1])

print(mul_sum)
