def calculate_grade():
    print("--- Student Grade System ---")
    physics = float(input("Enter Physics marks: "))
    chemistry = float(input("Enter Chemistry marks: "))
    math = float(input("Enter Math marks: "))
    english = float(input("Enter English marks: "))
    bangla = float(input("Enter Bangla marks: "))

    total_marks = physics + chemistry + math + english + bangla
    average_marks = total_marks / 5

    print("\n--- Results ---")
    print(f"Total Marks: {total_marks}")
    print(f"Average Marks: {average_marks:.2f}")

    if average_marks >= 80:
        print("Grade: A+")
    elif average_marks >= 70:
        print("Grade: A")
    elif average_marks >= 60:
        print("Grade: B")
    elif average_marks >= 50:
        print("Grade: C")
    elif average_marks >= 40:
        print("Grade: D")
    else:
        print("Grade: F (Fail) ❌")

calculate_grade()