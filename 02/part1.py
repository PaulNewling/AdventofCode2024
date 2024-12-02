import itertools

# file_name = "sample.txt"
file_name = "data.txt"

safe_count = 0
with open(file_name, "r") as file:
    for report in file:
        level = report.split(" ")
        increasing = True if int(level[0]) < int(level[1]) else False

        for a, b in itertools.pairwise(level):
            a = int(a)
            b = int(b)
            if a - b > 3 or b - a > 3 or a - b == 0:
                break
            if (increasing and a > b) or (not increasing and b > a):
                break

        else:
            safe_count += 1

print(safe_count)
