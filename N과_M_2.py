n, m = map(int,input().split(' '))

n_list = [i+1 for i in range(n)]

def dfs (selected):

    if len(selected) == m :
        print(" ".join(map(selected)))
        return selected


    for i in n_list:

        is_able = False
        if len(selected) == 0:
            is_able = True
        elif selected[len(selected)-1] <= i :
            is_able = True

        if (i not in selected) and is_able :
            selected.append(i)
            dfs(selected)
            selected.pop()

dfs([])