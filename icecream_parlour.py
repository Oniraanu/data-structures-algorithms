def icecreamParlor(m, arr):
    # Write your code here
    result = []
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] + arr[j] == m:
                result = [j + 1, i + 1]
    return result

    # s = {}
    # for i in range(len(arr)):
    #     if m - arr[i] in s:
    #         return [s[m - arr[i]], i + 1]
    #     else:
    #         s[arr[i]] = i + 1


print(icecreamParlor(4, [1, 4, 5, 3, 2]))
