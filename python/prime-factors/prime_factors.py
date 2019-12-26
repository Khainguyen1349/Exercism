def factors(value):
    if value == 1:
        return []
    f = 1
    for i in range(2, value):
        if value % i == 0:
            f = i
            break
    return factors(int(value/f)).append(f)
