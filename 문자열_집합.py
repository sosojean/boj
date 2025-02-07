n,m = map(int,input().split())



target_list = set()

cnt = 0
for i in range(n):
    target_list.add(input())

for i in range(m):
    s = input()

    if s in target_list :
        cnt += 1

print(cnt)
    