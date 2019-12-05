def is_valid(isbn):
    s = isbn.replace('-', '')
    if len(s) == 10:
        if s[-1].isdigit():
            # transform the whole number and check mod 11

        else:
            # transform first 9 number and add 10
