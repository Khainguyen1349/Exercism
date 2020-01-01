def recite(start_verse, end_verse):
    gifts = ["and a Partridge in a Pear Tree.", "two Turtle Doves, ",
             "three French Hens, ", "four Calling Birds, ", "five Gold Rings, ",
             "six Geese-a-Laying, ", "seven Swans-a-Swimming, ", "eight Maids-a-Milking, ",
             "nine Ladies Dancing, ", "ten Lords-a-Leaping, ", "eleven Pipers Piping, ",
             "twelve Drummers Drumming, "]
    numbers = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh',
               'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']
    r = []
    for verse_number in range(start_verse-1, end_verse):
        s = 'On the ' + numbers[verse_number] + ' day of Christmas my true love gave to me: ' + \
            ''.join([gifts[gift_number] for gift_number in range(verse_number, -1, -1)])
        if verse_number == 0:
            s = s.replace('and ', '')
        r.append(s)
    return r
