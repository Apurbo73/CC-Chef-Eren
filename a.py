import math
n = int (input())
for _ in range (n):
    a,b,c=list( map(int,input().split()))
    d=0
    e=0
    for i in range (1,a+1):
        if i%2==0:
            d=d+1
        else:
            e=e+1
    f= d*b+e*c
    print (f)