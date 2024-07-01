students=[]
num=int(input("Enter the number of students: "))
x=1
while x<=num:
    name=input("Enter the name of student: ")
    students.append(name)
    x+=1

i=0
total_marks=[]
while i<len(students):
    print("For",students[i])
    eng=int(input("Enter your marks of in eng:"))
    nep=int(input("Enter your marks of in nep:"))
    sci=int(input("Enter your marks of sci:"))
    math=int(input("Enter your marks of math:"))
    comp=int(input("Enter your marks of comp:"))
    total=eng+nep+sci+math+comp
    total_marks.append(total)
    i+=1

i=0 
for total in total_marks:
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