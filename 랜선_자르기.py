input_val = input()
n,k = input_val.split(" ")
n = int(n)
k = int(k)

lan_list = []

for i in range(n):
    lan_info = int(input())
    lan_list.append(lan_info)
    
#####end input#####

min_length = 1
max_length = max(lan_list)

result = 0

while min_length <= max_length : 

    mid = (max_length + min_length) // 2
    split_lan = sum(lan // mid for lan in lan_list)


    if split_lan >= k : 
        result = mid
        min_length = mid + 1

    else :
        max_length = mid - 1


print(result)
    


