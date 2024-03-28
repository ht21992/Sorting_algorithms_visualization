import time

def selection_sort(data, drawData, timeTick):
    start = time.perf_counter()
    for i in range(len(data)):
        min_idx = i
        for j in range(i+1, len(data)):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
        drawData(data, ['#FFD700' if x == i or x == min_idx else "#A90042" for x in range(len(data))])
        time.sleep(timeTick)
    drawData(data, ['yellow' for x in range(len(data))])
    elapsed_time_fl = (time.perf_counter() - start)
    return round(elapsed_time_fl, 2)
