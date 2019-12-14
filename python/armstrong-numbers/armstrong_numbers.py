import math


def is_armstrong_number(number):
    if(number == 0):
        return True
    else:
        number_temp = number
        i = 1
        digit = []
        while(i < math.floor(math.log10(number)) + 2):
            digit.append(number_temp % 10)
            number_temp = math.floor(number_temp/10)
            i = i+1
        return number == sum(math.pow(d, math.floor(math.log10(number)) + 1) for d in digit)
