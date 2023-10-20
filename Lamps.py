n,k,x,y=map(int,input().split())
b=n-k
if x>y:
    print((k*x)+(b*y))
else:
    print((k*x)+(b*x))