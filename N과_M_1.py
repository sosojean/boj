n,m = map(int,input().split(" "))


n_list = [i+1 for i in range (n)]




def dfs(selected) : 
    if len(selected) == m :
        print(' '.join(map(str, selected)))
        return selected
    for i in n_list :
        if i not in selected:
            selected.append (i)
            dfs(selected)
            selected.pop()



dfs([])