marks = input("Enter marks scored:")
if marks == '90-100':
    print("GRADE A")
elif marks =='80-89':
    print("GRADE B")
elif marks =='70-79':
    print("GRADE C")
elif marks =='60-69':
    print("GRADE D")
elif marks =='50-59':
    print("GRADE E")
else:
    print("FAIL")




def calculate_grade(mark):
    if mark >= 90 and mark <= 100:
        return "A"
    elif mark >= 80 and mark < 90:
        return "B"
    elif mark >= 70 and mark < 80:
        return "C"
    elif mark >= 60 and mark < 70:
        return "D"
    elif mark >= 50 and mark < 60:
        return "E"
    else:
        return "Fail"

# Test the function
mark = float(input("Enter the student's mark (percentage): "))
grade = calculate_grade(mark)

print(f"Mark: {mark}%")
print(f"Grade: {grade}")

#