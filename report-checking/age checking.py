student_attendance = int(input("Enter Your attendance Percantage: "))
student_mark = int(input("Enter Your Mark: "))

if student_mark >= 80:
    if student_attendance >= 90:
        print("Congratulations! A Grade + Full Scholarship.")
    else:
        print("Congratulations! A Grade + No Scholarship.")
elif student_mark >= 60:
    if student_attendance >=80:
        print("Congratulations! B Grade + Partial Scholarship.")
    else:
        print("Congratulations! B Grade + No Scholarship.")
else:
    print("Sorry, You're Failed. Better Luck Next Time.")

print("Thank You For Choosing Us!")