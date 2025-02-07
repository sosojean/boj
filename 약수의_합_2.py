n = int(input())

rst = 0

def a(n):
    rst = 0
    if n == 1 :
        return 1
    elif n <= 3 :
        return 1+n
        
    g_set = set()

    for i in range(1, n):

        if n % i == 0 :
            g_set.add(i)
            g_set.add(n)

    return(sum(g_set))


for i in range(1,n+1) :
    rst += a(i)
print(rst)



