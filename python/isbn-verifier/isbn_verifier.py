def is_valid(isbn):
    s = isbn.replace('-', '')
    if (len(s) == 10) and (s[:-1].isdigit()) and (s[-1].isdigit() or s[-1] == 'X'):
        if s[-1].isdigit():
            t = int(s[-1])
        else:
            t = 10
        index = 10
        for i in s[:-1]:
            t = t + index*int(i)
            index = index-1
        return t % 11 == 0
    else:
        return False
