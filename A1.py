def fun1(n):
    return n*(n+1)/2    #number of iteration is 1(one time)

print(fun1(4))


def fun2(m):
    sum=0
    for i in range(1,m+1):   #number of iteration is 4
        sum+=i
    return sum

print(fun2(4))