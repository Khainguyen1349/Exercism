def is_isogram(string):
    string_mod = [l for l in string.lower() if l.isalpha()]
    return len(string_mod) == len(set(string_mod))
