x,y,z=map(int,input().split())
xyzlist = [x,y,z]
sortedxyzlist = sorted(xyzlist)
print(sortedxyzlist[2]-sortedxyzlist[0])
