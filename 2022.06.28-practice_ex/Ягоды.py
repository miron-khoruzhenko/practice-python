a,b,c=map(int,input().split())

dl=[a,b,c]
dls=sorted(dl)

if dls[0]>=94 and dls[2]<=727:
    print(dls[2])

else:
    print("Error")
