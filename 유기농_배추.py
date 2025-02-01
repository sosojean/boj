import sys
sys.setrecursionlimit(10 ** 6)


tc = int(input())



def dfs(x,y) :
    if x < 0 or y < 0 or x >= m or y >= n:
        return False
    
    if g[y][x] == 1:
        g[y][x] = 0
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    
    return False
    


for i in range(tc):
    rst = 0
    m,n,k = list(map(int, input().split(' ')))
    g = [[0] * m for i in range(n)]

    for i in range(k):
        x, y = list(map(int,input().split(' ')))
        g[y][x] = 1
    # print(g)



    for y in range(len(g)) :
        for x in range(len(g[y])):
            if dfs(x,y) :
                rst += 1

    print(rst)

