import itertools

# file_name = "sample.txt"
file_name = "extra.txt"
file_name = "data.txt"

def is_asc(level):
    for i in range(len(level)-1):
        if level[i] > level[i+1]:
            return False
    return True

def is_des(level):
    for i in range(len(level)-1):
        if level[i] < level[i+1]:
            return False
    return True

def is_safe(level):
    if is_asc(level) == is_des(level):
        return False
    
    for i in range(len(level)-1):
        if (abs(level[i] - level[i+1]) > 3 or level[i] == level[i+1]):
            return False
    return True

safe_count = 0
with open(file_name, "r") as file:
    for report in file:
        org_level = [int(x) for x in report.split()]
        
        for idx in range(len(org_level)):
            level = org_level[:idx] + org_level[idx+1:]
            if is_safe(level) and (is_asc(level) != is_des(level)):
                safe_count += 1
                break
      
print(safe_count)


