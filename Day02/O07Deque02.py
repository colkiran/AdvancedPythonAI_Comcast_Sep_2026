from collections import deque

def moving_average(strm, wn_size=5):
    dq = deque(maxlen=wn_size)
    avgs = []

    for value in strm:
        dq.append(value)
        avg = sum(dq) / len(dq)
        avgs.append(avg)

    return avgs

readings = list(range(10, 80, 10))
print(f"readings :{readings}")

print(moving_average(readings, wn_size=3))
