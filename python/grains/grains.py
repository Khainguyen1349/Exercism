def square(number):
    if number < 1 or number > 64:
        raise ValueError("Invalid input number!")
    return 2**(number-1)
    # bits shifting
    # return 1 << (number-1)


def total():
    return sum(2**i for i in range(0, 64))
    # return (1<<n) - 1
