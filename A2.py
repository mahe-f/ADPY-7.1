def fun3(m):
    sum=0
    for i in range(1,m+1):
        for j in range(1,i+1):     #number of iteration is 4 = 1+2+3+4...+m
             sum+=1
    return sum

print(fun3(4))