def max_value(arr):
    max_val = arr[0]
    for num in arr[1:]:
        if num > max_val:
            max_val = num
    return max_val
print(max_value([3, 5, 1, 9, 2]))