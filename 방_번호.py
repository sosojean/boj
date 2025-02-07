
import math

num_list = list(map(int,list(str(input()))))

cnt_list = [0 for _ in range(10)]

for i in num_list :
    cnt_list[i] +=1

cnt_6_9 = math.ceil((cnt_list[6] + cnt_list[9])/2)
cnt_list[6] = cnt_6_9
cnt_list[9] = cnt_6_9


print(max(cnt_list))


