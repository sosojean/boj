from collections import deque


inf = 1001

n,m = map(int,input().split())

arr = []
rst_arr = [[-1 for _ in range(m)] for _ in range(n)]

d_x = [0,0,-1,1]
d_y = [1,-1,0,0]

target_x = 0
target_y = 0
for i in range(n):
    ls = list(map(int,input().split()))
    arr.append(ls)
    for j in range(len(ls)):
        if ls[j] == 2 :
            target_y = i
            target_x = j

        if ls[j] == 0 :
            rst_arr[i][j] = 0

            

def bfs(start_x,start_y) :
    queue = deque([(start_x, start_y)])

    rst_arr[start_y][start_x] = 0

    while queue :
        x, y = queue.popleft()

        for i in range(4):
            nx = x + d_x[i]
            ny = y + d_y[i]

            is_movable = 0 <= nx and m > nx and 0 <= ny and n > ny

            if is_movable and arr[ny][nx] == 1 and rst_arr[ny][nx] == -1:
                rst_arr[ny][nx] = rst_arr[y][x]+1
                queue.append((nx,ny))


bfs(target_x, target_y) 



for ls in rst_arr:
    print(' '.join(map(str,ls)))
