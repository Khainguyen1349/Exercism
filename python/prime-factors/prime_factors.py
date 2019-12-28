def factors(value):
    # if value == 2:
    #    return [2]
    value_temp = value
    f = []
    for i in range(2, int(value)):
        while (value_temp % i) == 0:
            value_temp = int(value_temp/i)
            f.append(i)
    return f
