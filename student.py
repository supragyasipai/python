students_list=['ram','sita']
print("1.Add student")
print("2.Remove student")
print("3.Display student")
print("4.Exit")
choice=int(input("Enter your choice:"))
if choice==1:
    print("Existing students",students_list)
    name=input("Name of the student you want to add: ")
    students_list.append(name)
    print("Now the students are:")
    print(students_list)
elif choice==2:
    print("Existing students",students_list)
    name=input("Name of the student you want to remove: ")
    students_list.remove(name)
    print("Now the students are:")
    print(students_list)
elif choice==3:
    print("Existing students: ",students_list)
else:
    exit()




