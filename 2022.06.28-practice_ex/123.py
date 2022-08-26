#python 
#print ("Hello" + " World")
##print ("Bu kod 201" + str(len("123456789")) + " yazilmistir" )

##print(" ")

#alt + 3, что бы закомментрровать строчки
#alt + 4, что бы раскомментровать строчки

'''
PRINT FUNCTION

Функция end изменяет то что будет после функции
Функция separator (sep) заменяет замятые на другие символы

example
print(1,2,3,sep='0')
print('Hello. Who are you?')
a=input()
print('Hello ', end=(''))
print(a + ' nice to meet you!')


способы вывода текста с переменной

dollarsrt = str(10)
centsrt = str(5)
dollar = 10
cent = 5

print("У меня есть " + dollarsrt + " долларов и " + centsrt + " центов")
print("У меня есть",dollar,"долларов и",cent ,"центов")
print("У меня есть %s долларов и %s центов"%(dollar,cent))

#все выдают одно и тоже


#Разложение чисел

x=int(input("Введите чилос пятизначное число: "))
a=x//10000
b=x//1000%10
c=x//100%10
d=x//10%10
e=x%10


print(a,b,c,d,e,sep='-')

'''

#END OF PRINT FUNCTIONS





'''
#VARIABLES

#Variables lets us store values* in a name*. 
#Than we can use the name later to refer to value.

#animal1 = "Lion"
#animal2 = "Zebra"
#print (animal)
#print ("Lion")
#last two command do the same thing
#print (animal1 + " " + animal2)
'''
#END OF VARIABLES





'''
# INTEGERS

#x=3.1415
#y=0.06
#z= x + y

#print (z)

#or

#print (3.1415 + 0.06)
#print (3*5)
#print (3/2)
'''
#END OF INTEGERS





'''
#TRUE OR FALSE BOLEANS

#fish = True
#lion = False
#bird = not lion            #Bird equal to true
#butterfly = not True       #Butterfly equal to false

#print(butterfly)
#print(bird)

#print(int(fish))
#True equal to one

#print(int(lion))
#False equal to zero

#print(fish and lion)       #False
#print(fish or lion)        #True

#a=False
#b=0

#print(a == b)              #True
'''
#END OF TRUE AND FALSE BOLEANS





'''
#IF STATEMENTS

#hot = True
#cold = False

#if hot == True and cold == False:
#  print("its hot")

#temp = 20
#freezing = 0
#raining = True
#snowing = False
#if temp <= 5:
#  print("cold")
  
#elif temp <= 15:
#  print("warm")

#else:
#  print("hot")

#if temp >= freezing and (raining == True or snowing == True):
#  print("Bad weather")
  
#if temp <=19:
#  print("warm")

#else:
#  if raining == True:
#    print("Its rainy")
#  else:
#    print("its not raining")
'''
# END OF IF CONDITIONS 





'''
#LIST FUNCTIONS

#shoppingList = [1, "Apples", 222, "Milk"]
#shoppingList.append('extra') #to add something in list func
#shoppingList.append("23")
#shoppingList.pop() #to delete something in list func


#print(shoppingList[0]) #list starts with 0
#print(shoppingList[1])
#print(shoppingList)
#print(len(shoppingList))

#print("Apples" in shoppingList) #true
#print(2 in shoppingList) #False

#example 1

#l = ['c','b','a']
#l.pop(0)

#if ('c' in l):
#  print("Yes")
  
#else:
#  print("No")
'''
#END OF LIST FUNCTIONS





# DICTIONARIES

l = {'Melon': Water, "Butter": "Fly"}
print(l['Melon])
