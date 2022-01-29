for _ in range(int(input())):
        s,k=map(int,input().strip().split(" "))
        b=input()
        max=""
        p=-1
        for i in range(s):
            if max < b:
                max=b
                d=i
            elif max==b:
                p=i-d
                break
            b=b[1:]+b[:1]
        if p==-1:
            print(d+(k-1)*s)
        else:
            print(d+(k-1)*p)
        print("")