def accel_calc(v1, v2, t1, t2):
    a = (v2-v1)/(t2-t1)
    return a

print(accel_calc(0, 10, 0, 20))
