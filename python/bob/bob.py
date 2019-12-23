def response(hey_bob):
    hey_bob_mod = ''.join(hey_bob.split())
    if len(hey_bob_mod) == 0:
        return 'Fine. Be that way!'
    elif hey_bob_mod[-1] == '?' and hey_bob_mod == hey_bob_mod.upper() and len([c for c in hey_bob_mod if c.isalpha()]) != 0:
        return "Calm down, I know what I'm doing!"
    elif hey_bob_mod[-1] == '?':
        return 'Sure.'
    elif hey_bob_mod == hey_bob_mod.upper() and len([c for c in hey_bob_mod if c.isalpha()]) != 0:
        return 'Whoa, chill out!'
    else:
        return 'Whatever.'
