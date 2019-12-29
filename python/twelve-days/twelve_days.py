def recite(start_verse, end_verse):
    things = ["and a Partridge in a Pear Tree.", "two Turtle Doves, ",
              "three French Hens, ", "four Calling Birds, ", "five Gold Rings, ",
              "six Geese-a-Laying, ", "seven Swans-a-Swimming, ", "eight Maids-a-Milking, ",
              "nine Ladies Dancing, ", "ten Lords-a-Leaping, ", "eleven Pipers Piping, ",
              "twelve Drummers Drumming, "]
    numbers = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh',
               'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']
    r = []
    for i in range(start_verse-1, end_verse):
        if i != 0:
            r.append('On the ' + numbers[i] +
                     ' day of Christmas my true love gave to me: ' +
                     ''.join([things[i-j] for j in range(i+1)]))
        else:
            r.append("On the first day of Christmas my true love gave to me: "
                     "a Partridge in a Pear Tree.")
    return r
