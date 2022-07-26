
def miniMaxSum(arr):
    arr.sort()
    minimum = 0
    maximum = 0
    reverse = len(arr) - 1
    for i in range(0, 4):
        minimum += arr[i]
    for i in range(reverse, reverse - 4, -1):
        maximum += arr[i]
    return minimum, maximum


print(miniMaxSum([4, 5, 1, 2, 3, 6]))
