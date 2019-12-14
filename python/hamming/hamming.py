def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('Lengths of texts are not equal')
    # return sum(value != strand_b[counter] for counter, value in enumerate(strand_a))
    return sum(value1 != value2 for value1 in strand_a and value2 in strand_b)
