def find_second_largest(arr):
    if len(arr) < 2:
        return -1

    largest = second_largest = float('-inf')

    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif largest > num > second_largest:
            second_largest = num

    return second_largest if second_largest != float('-inf') else -1

# Test cases
arr1 = [12, 35, 1, 10, 34, 1]
arr2 = [10, 10, 10]
arr3 = [5]

print("Second largest in arr1:", find_second_largest(arr1))  # Output: 34
print("Second largest in arr2:", find_second_largest(arr2))  # Output: -1
print("Second largest in arr3:", find_second_largest(arr3))  # Output: -1

