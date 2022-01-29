t=int(input())
while t!=0:
    n=int(input())
    arr=list(map(int,input().split(' ')))
    arr.sort()
    mi=arr[0] ^ arr[1]
    for i in range(1,n-1):
        temp=arr[i] ^ arr[i+1]
        if temp<mi:
            mi=temp
    print(mi)
    t=t-1