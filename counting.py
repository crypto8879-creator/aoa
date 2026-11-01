def counting_sort(arr):
    count = [0] * (max(arr) + 1)
    for num in arr:
        count[num] += 1

    sorted_arr = []
    for num, freq in enumerate(count):
        sorted_arr.extend([num] * freq)
    return sorted_arr


# Test
print("Counting Sort:", counting_sort([4, 2, 2, 8, 3, 3, 1]))