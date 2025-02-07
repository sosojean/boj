n = int(input())
card_list = sorted(list(map(int,input().split(" "))))

m = int(input())
s_card_list = list(map(int,input().split(" ")))

c_len = len(card_list)



def b_search(i):
    min_idx = 0
    max_idx = c_len - 1
    found_idx = -1  # 찾은 위치를 저장

    while min_idx <= max_idx:
        mid = (min_idx + max_idx) // 2

        if card_list[mid] < i:
            min_idx = mid + 1
        elif card_list[mid] > i:
            max_idx = mid - 1
        else:
            found_idx = mid  # 값을 찾았지만, 더 왼쪽이 있는지 확인
            max_idx = mid - 1  # 더 작은 쪽을 탐색 (왼쪽 끝 찾기)

    return found_idx  # 없으면 -1 반환


def search_same (idx) :
    
    left = idx -1
    right = idx +1
    count = 1

        # 왼쪽 탐색
    while left >= 0 and card_list[left] == card_list[idx]:
        count += 1
        left -= 1

    # 오른쪽 탐색
    while right < n and card_list[right] == card_list[idx]:
        count += 1
        right += 1

    return str(count)


rst_list = []

for i in s_card_list : 
    rst = '0'
    idx = b_search(i)

    if idx!= -1 :
        rst = search_same(idx)

    rst_list.append(rst)

print(' '.join(rst_list))
