arr = [7, 10, 4, 3, 20, 15]
k = int(input("Enter k: "))

arr.sort()

print(f"{k}th Smallest Element =", arr[k - 1])
print(f"{k}th Largest Element =", arr[-k])