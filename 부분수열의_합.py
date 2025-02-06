import sys
sys.setrecursionlimit(10 ** 6)

n , target = map(int, input().split())

num_list = sorted(list(map(int,input().split())))

count =0

def dfs(k, sum) :

    global count

    if k == n :

        if sum == target:
            count+=1
        return

    dfs(k+1, sum)
    dfs(k+1, sum+num_list[k])
    
dfs(0,0)

if target == 0 :
    count -=1
print(count)