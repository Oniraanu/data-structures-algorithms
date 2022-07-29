# def compareTriplets(a, b):
    # Write your code here
    # result = []
    # for i, (a, b) in enumerate(zip(a, b)):
    #     count_a = 0
    #     count_b = 0
    #     if a < b:
    #         result.append(count_b)
    #     elif a > b:
    #         result.append(count_a)
    #     else:
    #         return 0
    # return result
x = [5, 6, 7]
y = [3, 6, 10]
result = []
for i, j in zip(x, y):
    my_zip = i, j
    print(my_zip)


# print(compareTriplets(x, y))
