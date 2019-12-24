def response(hey_bob):
    hey_bob_mod = hey_bob.strip()
    is_yelling = hey_bob_mod == hey_bob_mod.upper() and any([c.isalpha() for c in hey_bob_mod])
    is_questioning = hey_bob_mod.endswith('?')
    if hey_bob_mod == "":
        return 'Fine. Be that way!'
    if is_questioning and is_yelling:
        return "Calm down, I know what I'm doing!"
    if is_questioning:
        return 'Sure.'
    if is_yelling:
        return 'Whoa, chill out!'
    return 'Whatever.'
