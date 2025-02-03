n = int(input())

stack = []

for i in range(n):
    stack.append(int(input()))


# print(stack)
curr = 0

new_stack = []
ans_list = []

possible = True

for i in stack :

    while(i > curr):
        curr +=1

        new_stack.append(curr)
        # print(new_stack, curr,i)

        ans_list.append('+')

    if i == new_stack[len(new_stack)-1] :

        new_stack.pop()
        ans_list.append('-')
    else : 
        possible = False


if not possible :
    print('NO')
else :
    for ans in ans_list:
        print(ans)

# print(len(new_stack))








