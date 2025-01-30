n = int(input())
s_card_list = sorted(list(map(int, input().split(' '))))
len_s = len(s_card_list)

m  = int(input())
card_list = list(map(int, input().split(' ')))

result = []

min_idx = 0

def b_search (i, min_idx) :
    max_idx = len_s-1


    while min_idx <= max_idx :

        mid = (min_idx + max_idx)//2

        if i == s_card_list[mid] : 
            return '1'
        elif i < s_card_list[mid] :
            max_idx = mid - 1

        elif i > s_card_list[mid] :
            min_idx = mid + 1
    return '0'


for i in card_list :
    result.append(b_search(i, min_idx))

print(' '.join(result))
    



    


