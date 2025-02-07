import sys

cnt,n = map(int,sys.stdin.readline().split())

num_list = list(map(int,sys.stdin.readline().split()))

prefix_list = [0]

for i in range(len(num_list)):
    if len(prefix_list) ==0:
        prefix_list.append(num_list[i])
    else:
        prefix_list.append(num_list[i]+prefix_list[i])

for _ in range(n):
    s,e = map(int, sys.stdin.readline().split())
    
    print(prefix_list[e]-prefix_list[s-1])
