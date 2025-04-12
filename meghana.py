arr = [1, 2, 2, 3, 4, 3, 5]
unique_arr = []
for num in arr:
    if num not in unique_arr:
        unique_arr.append(num)

print(unique_arr)

