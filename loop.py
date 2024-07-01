# WAP to print 10 to 1 using while Loop
# x=10
# while x>0:
#     print(x)
#     x-=1

# WAP to print total even number between 1 to 100
# x=2
# while x<=100:
#     print(x)
#     x+=2

# x=1
# while x<=50:
#     print(x*2)
#     x+=1

# WAP to print your name 10 times
# x=1
# while x<11:
#     print("Supragya Singh Sipai")
#     x+=1


# students=[]
# num=int(input("Enter the number of students: "))
# x=1
# while x<=num:
#     name=input("Enter the name of student: ")
#     students.append(name)
#     x+=1

# a=0
# while a<len(students):
#     print(students[a])
#     a+=1


    # 5 sub total percentage
    # nested Loop

students=[]
num=int(input("Enter the number of students: "))
x=1
while x<=num:
    name=input("Enter the name of student: ")
    students.append(name)
    x+=1

i=0
eng=[]
nep=[]
sci=[]
math=[]
comp=[]
while i<len(students):
    eng[i]=int(input("Enter your marks in eng:"))
    nep[i]=int(input("Enter your marks in nep:"))
    sci[i]=int(input("Enter your marks in sci:"))
    math[i]=int(input("Enter your marks in math:"))
    comp[i]=int(input("Enter your marks in comp:"))
    total=eng[i]+nep[i]+sci[i]+math[i]+comp[i]
    percentage=(total/500)*100
    print("Name: ",students[i])
    print("Percentage: " ,percentage,"%")
    if percentage<35:
        print("You are fail.")
    elif percentage>35 and percentage<45:
        print("You got C.")
    elif percentage>45 and percentage<60:
        print("You got B.")
    elif percentage>60 and percentage<75:
        print("You got A.")
    else:
        print("You got A+")
    i+=1




