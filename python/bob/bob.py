def response(hey_bob):
    hey_bob_mod = hey_bob.strip()
    is_yelling = hey_bob_mod == hey_bob_mod.upper() and any([c.isalpha() for c in hey_bob_mod])
    if hey_bob_mod == "":
        return 'Fine. Be that way!'
    if hey_bob_mod[-1] == '?' and is_yelling:
        return "Calm down, I know what I'm doing!"
    if hey_bob_mod[-1] == '?':
        return 'Sure.'
    if is_yelling:
        return 'Whoa, chill out!'
    return 'Whatever.'
