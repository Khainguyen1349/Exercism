import time


def reverseBits(n:int):
    n_str = '{0:032b}'.format(n)
    return int(n_str[::-1],2)

inputs = 43261596

start = time.time()
h = reverseBits(inputs)
end = time.time()

print(h)

print('For loop takes ', end - start, ' to finish')
