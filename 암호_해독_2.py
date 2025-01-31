a_list = [i for i in range(ord('a'),ord('z')+1)]

# print(a_list)


con_list = list(map(ord,list(input().lower())))
n = int(input())
keyword_list = []
for i in range(n):
    keyword = input()
    keyword_list.append(keyword)


def search():


    for i in range (1,len(a_list)+1):

        new_con_list = [(j + i)%(26) +ord('a') for j in con_list]
        new_con = ''.join(list(map(chr,new_con_list)))

        for keyword in keyword_list:
            if keyword in new_con:
                return(new_con)


print(search())