# Exercise 1
first_name = input("Enter First Name\n")  # Student details
last_name = input("Enter Last Name\n")
exam_mark = int(input("Enter Exam Mark\n"))

Outstanding = ("Grade A")
Satisfactory = ("Grade B")
Pass = ("Grade C")
Fail = ("Grade D")

Student_Details = first_name + (" ") + last_name
print(Student_Details)

if (exam_mark <= 100) and (exam_mark >= 80):  # Display Grade according to user input
    print(Outstanding)
elif (exam_mark <= 79) and (exam_mark >= 60):
    print(Satisfactory)
elif (exam_mark <= 59) and (exam_mark >= 50):
    print(Pass)
elif (exam_mark <= 49):
    print(Fail)

# Exercise 2
driver_speed = int(input("Enter Driver Speed in km/h\n"))
speed_limit = int(input("Enter Speed limit in km/h\n"))
if driver_speed <= speed_limit:
    print ("OK")
elif driver_speed > speed_limit:
    demerits = (driver_speed - speed_limit)/5
    print(demerits)







