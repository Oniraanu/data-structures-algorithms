def solution(my_list, target):
    low = 0
    high = len(my_list) - 1
    while low <= high:
        mid = (low + high) // 2
        number = my_list[mid]
        if number == target:
            return mid
        elif number < target:
            low = mid + 1
        else:
            high = mid - 1
    return None


saved_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(solution(saved_list, 6))
