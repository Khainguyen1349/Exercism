def factors(value):
    value_temp = value
    f = []
    n = 1
    stop = False
    while value_temp > n-1:
        if not stop:
            n += 1
        stop = False
        if value_temp % n == 0:
            value_temp = int(value_temp/n)
            f.append(n)
            stop = True
    return f
