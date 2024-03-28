import time

def heapify(data, n, i, drawData, timeTick):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and data[l] > data[largest]:
        largest = l

    if r < n and data[r] > data[largest]:
        largest = r

    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        drawData(data, ['#FFD700' if x == i or x == largest else "#A90042" for x in range(len(data))])
        time.sleep(timeTick)
        heapify(data, n, largest, drawData, timeTick)

def heap_sort(data, drawData, timeTick):
    start = time.perf_counter()
    n = len(data)

    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i, drawData, timeTick)

    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        drawData(data, ['#FFD700' if x == 0 or x == i else "#A90042" for x in range(len(data))])
        time.sleep(timeTick)
        heapify(data, i, 0, drawData, timeTick)

    drawData(data, ['yellow' for x in range(len(data))])
    elapsed_time_fl = (time.perf_counter() - start)
    return round(elapsed_time_fl, 2)
