# students=[
#     {'name':'ram','gender':'male','status':True},
#     {'name':'sita','gender':'female','status':False},
#     {'name':'rita','gender':'female','status':True},
#     {'name':'laxmi','gender':'female','status':False},
#     {'name':'gopal','gender':'male','status':False},
# ]
# total_students=len(students)
# male=0
# female=0
# active=0
# inactive=0
# mein=0
# fein=0
# meac=0
# feac=0
# for student in students:
#     if student['gender']=='male':
#         male+=1
#     else:
#         female+=1
#     if student['status']==True:
#         active+=1
#     else:
#         inactive+=1
#     if student['status']==False and student['gender']=='male':
#         mein+=1
#     elif student['status']==True and student['gender']=='male':
#         meac+=1
#     elif student['status']==False and student['gender']=='female':
#         fein+=1
#     else:
#         feac+=1

# print(f"Total students: {total_students} \nTotal male: {male} \nTotal female: {female} \nTotal active students: {active} \nTotal inactive students: {inactive} \nMale who are active: {meac} \nMale who are inactive: {mein} \nFemale who are active= {feac} \nFemale who are inactive: {fein} ")

# search=input("Enter name you want to search:")

# if search in students():
#     print("Found")
# else:
#     print("Invalid")






# x=1
# while x<50 :
#     if x==22 or x==33 or x==44 or x==49:
#         print (x, end=',')
#     x+=1


# find=[22,33,44,49]
# x=0
# while x<=50:
#     if x in find:
#         print(x)
#     x+=1


# numbers=[10,20,30,40]
# new=[]
# total=len(numbers)
# x=0
# while x<total:
#     new.append(numbers[x]*2)
#     x+=1
# print(new)

# data=[12,13,34,65,78,19,18,17,16,15]
# new=[]
# total=len(data)
# x=0
# while x<total:
#     if data[x]%2==0:
#         new.append(data[x])
# print(data)
