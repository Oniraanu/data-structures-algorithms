def compareTriplets(a, b):
    # Write your code here
    count_a, count_b = [0, 0]
    for i, j in zip(a, b):
        if a[i] <= b[j]:
            count_a[0] += 1
        elif a[i] >= b[j]:
            count_b[1] += 1
    return [count_a, count_b]


x = [5, 6, 7]
y = [3, 6, 10]
print(compareTriplets(x, y))
