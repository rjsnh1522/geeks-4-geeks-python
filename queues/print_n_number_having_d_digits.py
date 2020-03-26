from copy import copy


def print_digits_with_these(d, n):
    digits = d
    queue = copy(digits)
    for i in range(n):
        ele = queue.pop(0)
        print(ele)
        for k in digits:
            queue.append(int(f"{ele}{k}"))


dd = [1, 2, 3, 4]
nn = 20
print_digits_with_these(dd, nn)
