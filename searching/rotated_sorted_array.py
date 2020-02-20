

def rotated_sorted_array(arr, key):
    lo = 0
    hi = len(arr) - 1
    res = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == key:
            res = mid
            return res
        if arr[mid] < arr[hi]:
            if key > arr[mid] and key <= arr[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
        elif arr[mid] > arr[lo]:
            if key < arr[mid] and key >= arr[lo]:
                hi = mid - 1
            else:
                lo = mid + 1
    return res


arr = [12, 14, 18, 21, 3, 6, 8, 9]
arr = [73, 85, 94, 21, 27, 34, 47, 54, 66]
elem = 73
result = rotated_sorted_array(arr, elem)
print(result)

