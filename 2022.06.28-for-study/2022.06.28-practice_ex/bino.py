##a = int(input())
##
##if a%2==0 or a==1:
##    print("YES")
##
##else:
##    print("NO")

n=int(input())
k=1
while ((2**k)!=n) and ((2**k)<n): k=k+1
if (2**k)==n: print('YES')
else: print('NO')
