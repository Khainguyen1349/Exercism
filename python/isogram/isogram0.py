def is_isogram(string):
    string_mod = string.lower().replace('-', '').replace(' ', '')
    return len(string_mod) == len(set(string_mod))
