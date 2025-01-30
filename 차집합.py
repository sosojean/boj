import sys

a, b = list(map(int, input().split(' ')))

set_a = set(map(int,input().split(' ')))
set_b = set(map(int,input().split(' ')))

# print(set_a, set_b)

set_sub = set_a - set_b

print(len(set_sub))
print(' '.join(map(str,sorted(set_sub))))

