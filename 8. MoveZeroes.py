list = [0, 1, 0, 3, 12]
last_non_zero_found_at = 0
for i in range(len(list)):
    if list[i] != 0:
        list[last_non_zero_found_at] = list[i]
        last_non_zero_found_at += 1
for i in range(last_non_zero_found_at, len(list)):
    list[i] = 0
print(list)
        