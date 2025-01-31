def parse_to_num (n):
    return ord(n) - ord('a')+1


n = int(input()) 
l = list(input())

r = 31
m = 1234567891


rst = 0

for i in range(len(l)) :
    curr = parse_to_num (l[i])
    rst += (curr%m * (r**i)%m)

print(rst%m)

