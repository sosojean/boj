n = int(input())



def f():
    s = list(str(input()))

    final_list = []
    index_list = [0 for i in range(len(s))]

    index = 0
    for i in range(len(s)):

        print(index)

        if s[i] == '<' :
            if index!=0 : index -=1
            
        elif s[i] == '>':
            if index!= len(final_list)-1 : index+=1
            
        elif s[i] == '-'  :
            if index != 0 : print('delete')
            
        else :
            final_list.append(s[i])
            index+=1


            if  index!=0 :

                if index_list[index-1] == 0:

                    index_list[index-1] = index 
                else :
                    index_list[index-1] = index_list[index_list[index-1]]
                    index_list[index_list[index-1]] = index

                
            


            

        print(index_list)
        print(final_list)
        




for i in range(n):
    f()