def sum_of_multiples(limit, multiples):
    list = []
    for element in multiples:
        if element != 0:
            factor = 1
            while element*factor < limit:
                if element*factor not in list:
                    list.append(element*factor)
                factor += 1
    return sum(i for i in list)
