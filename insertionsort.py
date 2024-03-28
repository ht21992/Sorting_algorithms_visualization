import time

def insertion_sort(data, drawData, timeTick):
    start = time.perf_counter()
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
        drawData(data, ['#FFD700' if x == i or x == j + 1 else "#A90042" for x in range(len(data))])
        time.sleep(timeTick)
    drawData(data, ['yellow' for x in range(len(data))])
    elapsed_time_fl = (time.perf_counter() - start)
    return round(elapsed_time_fl, 2)
