students=int(input("Enter number of students: "))
start=1
total_student_marks=[]
while start<=students:
    print(f"*****Roll No: {start}*****")
    for i in range(1):
        nep=int(input("Enter marks in nepali:"))
        eng=int(input("Enter marks in english:"))
        math=int(input("Enter marks in math:"))
        sci=int(input("Enter marks in science:"))
        com=int(input("Enter marks in computer:"))
        total=nep+eng+math+sci+com
        total_student_marks.append(total)
    start+=1

i=1
for total in total_student_marks:
    per=total/5
    grade=""
    if per>35 and per<45:
        grade='C'
    elif per>45 and per<60:
        grade='B'
    elif per>60 and per<100:
        grade='A'
    else:
        grade='D'
    print(f"Roll no: {i} \t Total: {total} \t percentage:{per} \t grade:{grade}")
    i+=1


