def student_result_system():
    print("--- Advanced Student Result System ---")

    subjects_number = int(input("How many subjects do you have? "))
    subjects_data = {}

    for i in range(1, subjects_number+1):
        sub_name = input(f"Enter the name of subject {i}: ")
        marks = float(input(f"Enter marks for {sub_name}: "))
        subjects_data[sub_name] = marks
    print("\n================ Subject-wise Grades ================")

    total_marks = 0
    has_failed = False

    for sub_name, marks in subjects_data.items():
        total_marks += marks

        if marks >= 80:
            grade = "A+"
        elif marks >= 70:
            grade = "A"
        elif marks >= 60:
            grade = "B"
        elif marks >= 50:
            grade = "C"
        elif marks >= 40:
            grade = "D"
        else:
            grade = "F"
            has_failed = True

        print(f"{sub_name}: Marks = {marks} -> Grade = {grade}")


    average_marks = total_marks / subjects_number
    
    print("\n================ Final Summary ================")
    print(f"Total Marks: {total_marks}")
    print(f"Average Marks: {average_marks:.2f}")

    if has_failed:
        print("Final Status: FAILED ❌ (You failed in one or more subjects)")
    else:
        if average_marks >= 80:
            final_grade = "A+"
        elif average_marks >= 70:
            final_grade = "A"
        elif average_marks >= 60:
            final_grade = "B"
        elif average_marks >= 50:
            final_grade = "C"
        else:
            final_grade = "D"
        print(f"Final Status: PASSED 🎉 -> Overall Grade: {final_grade}")

student_result_system()