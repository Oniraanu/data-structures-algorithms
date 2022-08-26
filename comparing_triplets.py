def compareTriplets(a, b):
    count_a, count_b = 0, 0
    for i, j in zip(a, b):
        count_a += i > j
        count_b += i < j
    return count_a, count_b