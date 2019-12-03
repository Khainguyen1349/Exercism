def is_pangram(sentence):
    letter_count = [l.lower() for l in sentence if l.isalpha()]
    # letter_count.sort()
    letter_short = []
    i = 0
    for l in letter_count:
        if i == letter_count.index(l):
            letter_short.append(l)
        i = i+1

    if len(letter_short) == 26:
        return True
    else:
        return False
