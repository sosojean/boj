cnt = int(input())

n_list = list(map(int, input().split()))


dp = [1]*(cnt)

for i in range(1,cnt) :
    for j in range(i):

        if n_list[j] < n_list[i] :
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))