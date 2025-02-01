n = int(input())

n_list = []
for i in range(n) :
    n_list.append(int(input()))


def dfs(selected,n,ans):

    if sum(selected) > n :
        return

    if sum(selected) == n :
        ans.append(selected)
        return (selected)
    

    for i in range(1,4) :

        selected.append(i)
        # print(selected)

        dfs(selected,n,ans)
        selected.pop()
    

    


for n in n_list :
    ans = []
    dfs([],n,ans)
    print(len(ans))


