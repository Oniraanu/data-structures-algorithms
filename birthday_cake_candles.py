def birthdayCakeCandles(candles):
    candles.sort()
    candles.reverse()
    count = 0
    for i in range(len(candles)):
        if candles[0] == candles[i]:
            count += 1
    return count

    #       OR

    # candles.sort()
    # candles.reverse()
    # return len([x for x in candles if x >= candles[0]])


lst = [82, 49, 82, 82, 41, 82, 15, 63, 38, 25]
print(birthdayCakeCandles(lst))
print('aaab' < 'aaac')