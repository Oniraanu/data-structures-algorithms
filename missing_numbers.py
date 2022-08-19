from collections import Counter


def missingNumbers(arr, brr):
    missing = set()
    for i in brr:
        if i in arr:
            arr.remove(i)
        else:
            missing.add(i)
    return list(sorted(missing))
    # a = Counter(arr)
    # b = Counter(brr)
    # return sorted((b - a).keys())


x = [7, 2, 5, 3, 5, 3]
y = [7, 2, 5, 4, 6, 3, 5, 3]
print(missingNumbers(x, y))