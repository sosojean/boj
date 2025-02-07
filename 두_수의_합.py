n = int(input())

n_list = list(map(int,input().split()))

target = int(input())

cnt = 0


start = 0
end = 0

for i in n_list:
    if (target - i) in n_list:
        cnt+=1

print(cnt//2)



