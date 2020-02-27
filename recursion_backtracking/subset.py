def find_subset(arr, len, index, results):
    if len == 0:
        results.append([])
        return
    if len == 1:
        results.append([arr[len - 1]])

    for i in range(len):
        find_subset(arr[:-i], i, index+1, results)

results = []
index = 0
arr = [1, 2]
find_subset(arr, len(arr), index, results)
print(results)
