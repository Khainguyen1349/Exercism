def is_valid(isbn):
    s = isbn.replace('-', '')
    t = 1
    if (len(s) == 10) and (s[:-1].isdigit()):
        t = 0
        index = 10
        for i in s[:-1]:
            t = t + index*int(i)
            index = index-1

        if s[-1].isdigit():
            t = t + int(s[-1])
        elif s[-1] == 'X':
            t = t + 10
        else:
            t = 1

    return t % 11 == 0
