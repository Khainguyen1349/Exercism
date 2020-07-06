import time

start = time.time()

def plusOne(digits):
    sumPlusOne = sum([digits[-1 - i]*(10**i) for i in range(len(digits))]) + 1
    return [int(d) for d in str(sumPlusOne)]

h = plusOne([1,2,3])
print(h)

end = time.time()
print(end - start)
        
