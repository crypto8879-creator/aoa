def bucket_sort(arr):
    buckets = [[] for _ in range(10)]
    for num in arr:
        buckets[num // 10].append(num)

    res = []
    for bucket in buckets:
        res.extend(sorted(bucket))
    return res


# Test
print("Bucket Sort:", bucket_sort([42, 32, 33, 52, 37, 47, 51]))