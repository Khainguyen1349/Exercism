import time


def subsets_recursive(nums):
    # First solution --- using recursive
    if len(nums) != 0:
        L = subsets_recursive(nums[:-1])
        return L + [l + [nums[-1]] for l in L]
    else:
        return [[]]


def subsets_forloop(nums):
    # Second solution --using for loop
    L = [[]]
    for i in range(len(nums)):
        L = L + [l + [nums[i]] for l in L]
    return L


inputs = [i for i in range(12)]

start_re = time.time()
h = subsets_recursive(inputs)
print(h)
end_re = time.time()
print('Recursive takes ', end_re - start_re, ' to finish')

start_fo = time.time()
h = subsets_forloop(inputs)
print(h)
end_fo = time.time()
print('For loop takes ', end_fo - start_fo, ' to finish')
