n = int(input())


num_list =[]
for i in range(n):
    num_list.append(int(input()))



def df_func(num):

    dp =[0]*(max(6,num+1))

    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 2


    for i in range(6,num+1):
        dp[i] = dp[i-2] + dp[i-3]
    print(dp[num])
        



for num in num_list :
    df_func(num)