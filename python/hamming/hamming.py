def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('Lengths of texts are not equal')
    return sum(1 for counter, value in enumerate(strand_a) if value != strand_b[counter])
