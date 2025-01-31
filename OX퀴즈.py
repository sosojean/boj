
input_n = int(input())

input_list = []
for i in range(input_n):
    input_list.append(input())


def sum_from_one(n):
    return int((n+1)*(n/2))

def ox(s):
    rst = 0
    s_list = s.split('X')
    for t in s_list:
        # print(t)
        if 'O' in t :
            rst += sum_from_one(len(t))
    print(rst) 





for s in input_list:
    ox(s)