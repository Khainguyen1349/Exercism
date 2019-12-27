def factors(value):
    if value == 1:
        return []
    not_found_factor = True
    for i in range(2, int(value**0.5)+1):
        if value % i == 0:
            f = i
            not_found_factor = False
            break
    if not_found_factor:
        return [value]
    return [f] + factors(int(value/f))
