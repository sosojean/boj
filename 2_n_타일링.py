n = int(input())


dp = [0]*(max(n+1,3))
dp[0] = 0
dp[1] = 1
dp[2] = 2


def tile(n) :
    for i in range(3,n+1):
        dp[i] = ((dp[i-1]) +(dp[i-2])) % 10007
        
tile(n)
print(dp[n])