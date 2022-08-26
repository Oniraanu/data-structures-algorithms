def diagonalDifference(arr):
    left_to_right = 0
    right_to_left = 0
    for i in range(len(arr)):
        # 0,0   0,1   0,2
        # 1,0   1,1   1,2
        # 2,0   2,1   2,2
        left_to_right += arr[i][i]
        right_to_left += arr[i][-(1 + i)]
    return abs(left_to_right - right_to_left)