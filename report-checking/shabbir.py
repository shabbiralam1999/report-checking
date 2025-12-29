student_name = str(input("What Is Your Name? "))
print(f"Report Card For {student_name}")
subject_1 = int(input("What Is Your First Subject's Mark? "))
subject_2 = int(input("What Is Your Second Subject's Mark? "))
subject_3 = int(input("What Is Your Third Suject's mark? "))
subject_4 = int(input("What Is Your Fourth Subject's mark? "))

result = (subject_1 + subject_2 + subject_3 + subject_4) // 4

if result <= 100 and result >= 90:
    print(f'Your Average Score : {result}')
    print(f'Grade: A')
    print(f'Message : Excellent Work!')
elif result < 90 and result >= 80:
    print(f'Your Average Score : {result}')
    print(f'Grade : B')
    print(f'Message : Well Done!')
elif result < 80 and result >= 70:
    print(f'Your Average Score : {result}')
    print(f'Grade : C')
    print(f'Message : Good Mark')
elif result < 70 and result >= 60:
    print(f'Your Average Mark : {result}')
    print(f'Grade : D')
    print(f'Message : Satisfactory!')
elif result < 60:
    print(f'Your Average Mark : {result}')
    print(f'Grade : F')
    print(f'Message : Keep Practicing!')