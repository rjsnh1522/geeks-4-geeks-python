def find_subset(arr):
    sublist = [[]]
    for i in range(len(arr)+1):
        for j in range(i+1, len(arr)+1):
            sub = arr[i:j]
            sublist.append(sub)
    return sublist

arr = [1, 2, 3]
results = find_subset(arr)
print(results)


# now by recursion

# def subset_by_recursion(given_array):
#     subset = [None]*len(given_array)
#     subset_helper(given_array, subset, 0)
#
#
# def subset_helper(given_array, subset, index):
#     if len(given_array) == index:
#         print([i for i in subset if i])
#     else:
#         subset[index] = None
#         subset_helper(given_array,subset, index+1)
#         subset[index] = given_array[index]
#         subset_helper(given_array, subset, index + 1)
#
#
# arr = [1, 2, 3]
# subset_by_recursion(arr)

#
# def solution_recur(given_array, subset, index, len):
#     print(subset)
#     for i in range(index, len):
#         subset.append(given_array[i])
#         solution_recur(given_array,subset, i+1, len)
#         subset.pop()
#
#
# arr = [1, 2, 3]
# solution_recur(arr, [], 0, len(arr))


# def subset_lopper(arr, subset, index, results):
#     results.append(subset.copy())
#     for i in range(index, len(arr)):
#         subset.append(arr[i])
#         subset_lopper(arr, subset, i+1, results)
#         subset.pop(-1)
#     return
#
#
# arr = [1, 2, 3]
# subs = []
# result = []
# subset_lopper(arr, subs, 0, result)
# print(result)
#
