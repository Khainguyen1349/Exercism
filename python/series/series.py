def slices(series, length):
    if length < 1:
        raise ValueError("Asking for zero or negative length number!")
    if length > len(series):
        raise ValueError("Input has its length shorter than asked length!")
    return [series[counter:counter + length] for counter in range(0, len(series)-length+1)]
