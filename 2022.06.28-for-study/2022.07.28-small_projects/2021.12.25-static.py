quizSum = 0
minGrade = 5000

#Q*30 + V*30 + F*40 >= 5000

#===================================
#quiz grade take
print("Quiz grades: ")
for i in range(8):
    print(i+1, ": ", end="", sep="")
    x = input()

    if x == "":
        i -= 1
        break
    
    quizSum += float(x)

quizSum = (quizSum/8)*30

vize = float(input("\nMidterm grade: ")) * 30
#===================================


#===================================
#min quiz
final = 40*100 #final 100puan
quiz = 0

if(final + quiz + vize >= minGrade):
    "If final 100 you already pass it"

while minGrade > final + quiz + vize:
    quiz += 30

print("\nMin quiz (if final is 100) grade is ", float(quiz)/30)
#===================================


#===================================
#min final
final = 0
quiz = (8-(i+1))*100/8*30 + quizSum

if(final + quiz + vize >= minGrade):
    "If quiz 100 you already pass it"


while minGrade > final + quiz + vize:
    final += 40

print("Min final (if quiz is ", quiz/30, ") grade is ", float(final)/40, "\n")
#===================================

x = input()



