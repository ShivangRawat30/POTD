t = int(input())
for i in range(t):
    a,b,c = map(int,input().split(" "))
    if a+b+c==2*max(a,b,c):
        print("yes")
    else:
        print("no")
