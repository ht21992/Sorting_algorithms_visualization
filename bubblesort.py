import time

def bubble_sort(data,drawdata,timetick):
    #start_time = time.strftime("%H:%M:%S", time.gmtime())
    start = time.perf_counter()
    for i in range(len(data) - 1):
        for j in range(len(data) -1):
            if data[j]>data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]
                drawdata(data,['#FFD700' if x==j or x==j+1 else "#A90042" for x in range(len(data)) ])
                time.sleep(timetick)
    drawdata(data,['yellow' for x in range(len(data))])
    # end_time = time.strftime("%H:%M:%S", time.gmtime())
    elapsed_time_fl = (time.perf_counter() - start)
    return round(elapsed_time_fl,2)


