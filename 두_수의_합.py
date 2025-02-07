n = int(input())

n_list = set(map(int,input().split()))

target = int(input())

cnt = 0


for i in n_list:
    if (target - i) in n_list:
        cnt+=1

print(cnt//2)



