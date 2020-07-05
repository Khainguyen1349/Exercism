import time

start = time.time()

def hammingDistance(x: int, y: int) -> int:
    value1 = [1 if digit=='1' else 0 for digit in bin(x)[2:]]
    value2 = [1 if digit=='1' else 0 for digit in bin(y)[2:]]
    if len(value1) < len(value2):
        value1 = [0 for _ in range(len(value2) - len(value1))] + value1
        #for i in range(len(value2) - len(value1)):
            #value1.insert(0,0)
    else:
        value2 = [0 for _ in range(len(value1) - len(value2))] + value2
        #for i in range(len(value1) - len(value2)):
            #value2.insert(0,0)
    print(value1)
    print(value2)
    return sum(v1 != v2 for (v1, v2) in zip(value1, value2))

h = hammingDistance(1,4)
print(h)

end = time.time()
print(end - start)
