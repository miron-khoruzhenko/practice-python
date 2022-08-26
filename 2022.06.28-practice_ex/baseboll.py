a,b=[],[]
d,c = map(int,input().split())
a,b=a+[d],b+[c]
d,c = map(int,input().split())
a,b=a+[d],b+[c]
d,c = map(int,input().split())
a,b=a+[d],b+[c]
d,c = map(int,input().split())
a,b=a+[d],b+[c]

if sum(a)>sum(b):
    print(1)

elif sum(a)<sum(b):
    print(2)

else:
    print("DRAW")
