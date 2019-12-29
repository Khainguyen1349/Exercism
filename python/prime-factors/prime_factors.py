def factors(value):
    if value == 1:
        return []
    isPrime = True
    for i in range(2, int(value**0.5)+1):
        if value % i == 0:
            f = i
            isPrime = False
            break
    if isPrime:
        return [value]
    return [f] + factors(int(value/f))
