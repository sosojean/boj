key = input()
c_text = input()

len_key = len(key)
len_text= len(c_text)
col = len(c_text)//len(key)

def sort_key():
    key_list = list(key)
    sorted_index_list = sorted(range(len(key_list)), key = lambda i : key_list[i])
    return(sorted_index_list)


def slice_text():
    sliced_list = ["" for _ in range(col)]
    for i in range(len_key):
        text = c_text[i*col: (i+1)*col]
        # print(text)
        for j in range (col):
            sliced_list[j]+= text[j]
    # print(sliced_list)
        

    return sliced_list

def rearrange_text(sliced_list, index_list):
    result_list = []
    for sliced in sliced_list:
        sorted_word = [x for _, x in sorted(zip(index_list, sliced))]
        result_list.append(''.join(sorted_word))
    return result_list












index_list = sort_key()
sliced_list = slice_text()
result_list = rearrange_text(sliced_list, index_list)

print(''.join(result_list))

