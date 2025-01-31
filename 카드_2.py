from collections import deque

n = int(input())

queue = deque(range(1,n+1))

i=0

while(len(queue) != 1):

    if i %2 == 0 :
        queue.popleft()
    else:
        queue.append(queue.popleft())
   
    i+=1

if len(queue) == 1 : 
    print(queue.popleft())
