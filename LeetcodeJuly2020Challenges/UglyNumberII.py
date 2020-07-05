import time

start = time.time()

def nthUglyNumber(n: int) -> int:
    L = [1]
    L2 = 1
    L3 = 1
    L5 = 1
    i = 0
    j = 0
    k = 0
    while len(L) < n:
        if L2 in L:
            L2 = L[i] * 2
            i = i + 1
        #print("L2: ", L2)
        if L3 in L:
            L3 = L[j] * 3
            j = j + 1
        #print("L3: ", L3)
        if L5 in L:
            L5 = L[k] * 5
            k = k + 1
        #print("L5: ", L5)
        L.append(min(L2, L3, L5))
        #print("L: ", L)        
    return L[-1]

N = nthUglyNumber(242)
print(N)

end = time.time()
print(end - start)
