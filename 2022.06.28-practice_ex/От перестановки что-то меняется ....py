a=int(input())
b=0
c=[]

while b<a:
    b+=1
    c+=[int(input())]

print(' '.join(list(reversed(c))))
