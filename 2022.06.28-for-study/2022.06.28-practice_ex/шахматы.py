##a=input().upper()
##c=list(a)
##b=['A','B','C','E','F','G','H','1','2','3','4','5','6','7','8','9','-']
##
##x=['A','B','C','E','F','G','H']
##y=['1','2','3','4','5','6','7','8','9']
##
##
##
##if len(a)==5 and (a.isalpha() and a.isdigital())==0 and a.find('-')==2 and ((c[0] and c[3]) in b)==1:
##    if (c[3] == (x[a.find(c[3-2])]) or (x[a.find(c[3+2])])) and (c[4] == (y[a.find(c[4-1])]) or x[a.find(c[4+1])]):
##        print("YES")
##    elif (c[3] == (x[a.find(c[3-1])]) or (x[a.find(c[3+1])])) and (c[4] == (y[a.find(c[4-2])]) or x[a.find(c[4+2])]):
##        print("YES")
##    else:
##        print("NO")
##else:
##    print('ERROR')



#Попытка 2


#A 1 - B 2
#0 1 2 3 4


##a=input().upper()
##a_list=list(a)
##
##symbolcontrol = a.isalpha() and a.isdigital()
##listcontrol = a_list[0] and a_list[3]
##
##b=['A','B','C','D','E','F','G','H','1','2','3','4','5','6','7','8','9','-']
##
##y="ABCDEFGH"
##x="123456789"
##ylist=['A','B','C','D','E','F','G','H']
##xlist=['1','2','3','4','5','6','7','8']
##
##first=(a_list[3]==(xlist[(x.find(a_list[0])+2)] or xlist[(x.find(a_list[0])-2)]) and a_list[4]==(ylist[(y.find(a_list[1])+1)] or ylist[(y.find(a_list[1])-1)]))
##second=(a_list[3]==(xlist[(x.find(a_list[0])+1)] or xlist[(x.find(a_list[0])-1)]) and a_list[4]==(ylist[(y.find(a_list[1])+2)] or ylist[(y.find(a_list[1])-2)]))
##
####print(a_list[1])
####print(y.find(a_list[1])-2)
####print(ylist[(y.find(a_list[1])-2)])
##
##if len(a)==5 and (symbolcontrol)==0 and a.find('-')==2 and (listcontrol in b)==1:
##    if first or second:
##        print(1)
##    else:
##        print(0)
##else:
##    print("ERROR")


points = [] # список целевых клеток
 
def move(x, y, step=0):
    if step == 2:
        points.append(str(y) + str(x))
        
    else:
        if x>1 and y>2: move(x-1, y-2, step+1)
        if x>2 and y>1: move(x-2, y-1, step+1)
        
        if x<8 and y>2: move(x+1, y-2, step+1)
        if x<7 and y>1: move(x+2, y-1, step+1)
        
        if x<7 and y<8: move(x+2, y+1, step+1)
        if x<8 and y<7: move(x+1, y+2, step+1)
 
        if x>1 and y<7: move(x-1, y+2, step+1)
        if x>2 and y<8: move(x-2, y+1, step+1)
 
#Ввод исходной позиции коня на шахматной доске
x0, y0 = list(input('Введите позицию коня: ').upper())
x0 = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}[x0]
y0 = int(y0)
 
#Получение списка целевых клеток с цифрой вместо буквы
#Координаты клеток изначально реверсированы в целях упрощенной сортировки
move(x0, y0) # (x0, y0) - исходная позиция
 
#Удаление дубликатов в списке, сортировка и замена первой цифры буквой от A до H
points = ['ABCDEFGH'[int(point[1])-1]+point[0] for point in sorted(set(points), key=lambda point: int(point))]
 
#Вывод отсортированного списка из целевых клеток
print(*points)






















