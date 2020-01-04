def list_of_2_multiples(list1, list2, max):
    list_ = list2
    for element1 in list1:
        list_.extend([element1*element2 for element2 in list2 if element1*element2 < max])
    return list_


def sum_of_multiples(limit, multiples):
    if any([i for i in multiples if i == 0]):
        return 0
    list = []
    for element in multiples:
        list_of_self_multiples = []
        factor = 1
        while element*factor < limit:
            list_of_self_multiples.append(element*factor)
            factor += 1
        list_extension = list_of_2_multiples(list, list_of_self_multiples.copy(), limit)
        list.extend(list_extension)
    return sum(i for i in list)
