from collections import deque

import sys
sys.setrecursionlimit(10**6) # 이거 안해주면 시간초과 뜸



n,m,v = map(int,input().split())

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
visited[v] = True

dfs_ls = [v]
bfs_ls = [v]


for _ in range(m):
    s, e = map(int,input().split())

    graph[s].append(e)
    graph[e].append(s)

def dfs (start):
    for i in sorted(graph[start]):
        if not visited[i]:
            dfs_ls.append(i)
            visited[i] = True
            dfs(i)



def bfs(start) :
    for i in sorted(graph[start]):
        if not visited[i] and i not in queue:
            queue.append(i)
        
    if len(queue) >= 1:
        next = queue.popleft()
        visited[next] = True
        bfs_ls.append(next)

        bfs(next)
    


dfs(v)


visited = [False for _ in range(n+1)]
visited[v] = True

queue = deque()

bfs(v)


print(' '.join(map(str,dfs_ls)))
print(' '.join(map(str,bfs_ls)))