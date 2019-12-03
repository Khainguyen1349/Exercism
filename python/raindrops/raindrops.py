def convert(number):
    s = ""
    flag = 0;
    if number%3 == 0:
        s = s + 'Pling'
        flag = 1;
    if number%5 == 0:
        s = s + 'Plang'
        flag = 1;
    if number%7 == 0:
        s = s + 'Plong'
        flag = 1;

    if flag == 0:
        s = str(number)
    return s
