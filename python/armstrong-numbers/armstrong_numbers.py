def is_armstrong_number(number):
    number_str = str(number)
    return number == sum(int(i)**len(number_str) for i in number_str)
