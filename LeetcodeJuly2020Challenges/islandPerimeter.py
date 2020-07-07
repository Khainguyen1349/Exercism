import time

start = time.time()

def islandPerimeter(grid) -> int:
    peri = 0
    for h in range(len(grid)):
        for v in range(len(grid[0])):
            if grid[h][v]:
                peri = peri + 4 
                if h:
                    if grid[h - 1][v]:
                        peri = peri - 1
                if v:
                    if grid[h][v - 1]:
                        peri = peri - 1
                if h != len(grid) - 1:
                    if grid[h + 1][v]:
                        peri = peri - 1
                if v != len(grid[0]) - 1:
                    if grid[h][v + 1]:
                        peri = peri - 1
    return peri
    
inputs = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
h = islandPerimeter(inputs)
print(h)

end = time.time()
print(end - start)
        
