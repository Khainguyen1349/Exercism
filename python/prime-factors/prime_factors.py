def factors(value):
    value_temp = value
    f = []
    n = 1
    while value_temp > n*n:
        n += 1
        while value_temp % n == 0:
            value_temp = int(value_temp/n)
            f.append(n)
    if value_temp < n*n and value_temp != 1:
        f.append(value_temp)
    return f
