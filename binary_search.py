def solution(my_list, target):
    # for a sorted list, get the lowest index and highest index in the list
    low = 0
    high = len(my_list) - 1
    # use a loop to check if the number of items in the list has been exhausted
    while low <= high:
        # get the middle index of the list
        mid = (low + high) // 2
        number = my_list[mid]
        if number == target:
            return mid
        # list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], target = 6
        # mid in this case is 4...if 4 is less than 6, then new low will be 5.
        # i.e. our new list to be searched will be list = [5, 6, 7, 8, 9, 10]
        elif number < target:
            low = mid + 1
        # list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], target = 2
        # mid is 4...if 4 > 2, the new high will be 3.
        # i.e. our new list to be searched will be list = [1, 2, 3]
        else:
            high = mid - 1
    return None


saved_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(solution(saved_list, 6))
