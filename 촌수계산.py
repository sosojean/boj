import math

n = int(input())

s, e = map(int,input().split())

m = int(input())


graph = [[] for _ in range (n+1)]



for _ in range (m):
    p, c = map(int,input().split())

    graph[p].append(c)
    graph[c].append(p)


# print(graph)



def dfs (node, visited, count):


    if node not in visited :
        count +=1

        visited.append(node)

        for neigh in graph[node]:
            # print(count, neigh)
            if rst_list[neigh] == -1:
                rst_list[neigh] = count

            dfs(neigh, visited, count)



rst_list = [-1 for _ in range(n+1)]

dfs(s,[],0)


print(rst_list[e])
        

    
