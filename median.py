def median_of_two_arrays(arr1, arr2):
    merged = sorted(arr1 + arr2)
    n = len(merged)
    mid = n // 2

    if n % 2 != 0:
        return float(merged[mid])
    return (merged[mid - 1] + merged[mid]) / 2.0


# Test
a = [1, 3]
b = [2, 4]
print("Median of Merged Arrays:", median_of_two_arrays(a, b))