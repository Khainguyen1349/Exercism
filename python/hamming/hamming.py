def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise Exception('ValueError')
    elif len(strand_a) != 0:
        return sum(1 for counter, value in enumerate(strand_a) if value != strand_b[counter])
    else:
        return 0
