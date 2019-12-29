def factors(value):
    value_temp = value
    f = []
    n = 1
    while value_temp > n:
        n += 1
        while value_temp % n == 0:
            value_temp = int(value_temp/n)
            f.append(n)
    return f
