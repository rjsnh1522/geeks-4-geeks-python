# def find_subset(arr):
#     sublist = [[]]
#     for i in range(len(arr)+1):
#         for j in range(i+1, len(arr)+1):
#             print(i, j)
#             sub = arr[i:j]
#             print(sub)
#             sublist.append(sub)
#     return sublist
#
# arr = [1, 2, 3]
# results = find_subset(arr)
# print(results)


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


def solution_recur(given_array, index, len):
    if index >= len:
        print(given_array)
        return
    for i in range(len):
        i
        solution_recur(given_array[index:i], index+1, len)


arr = [1, 2]
solution_recur(arr, 0, len(arr))
