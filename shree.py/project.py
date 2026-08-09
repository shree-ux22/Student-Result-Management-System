from datetime import datetime


def display_header():
    print("=" * 65)
    print("        STUDENT RESULT MANAGEMENT SYSTEM")
    print("=" * 65)
    print("College   : St. Andrews Institute of Technology & Management")
    print("Course    : Bachelor of Computer Applications (BCA)")
    print("Developer : Tanushree Panda")

    current = datetime.now()
    print("Date      :", current.strftime("%d-%m-%Y"))
    print("Time      :", current.strftime("%I:%M %p"))
    print("=" * 65)


def get_student_details():
    print("\nEnter Student Details\n")

    student = {
        "name": input("Student Name     : ").strip(),
        "roll": input("Roll Number      : ").strip(),
        "course": input("Course           : ").strip(),
        "semester": input("Semester         : ").strip(),
        "college": input("College Name     : ").strip()
    }

    return student


def input_marks():
    subjects = [
        "Python Programming",
        "Database Management System",
        "Probability & Statistics",
        "Software Engineering",
        "Value Added Course"
    ]

    marks = {}

    print("\nEnter Subject Marks (0 - 100)\n")

    for subject in subjects:
        while True:
            try:
                mark = float(input(f"{subject} : "))

                if 0 <= mark <= 100:
                    marks[subject] = mark
                    break
                else:
                    print("Marks should be between 0 and 100.")

            except ValueError:
                print("Please enter valid numeric marks.")

    return marks


def calculate_percentage(marks):
    total = sum(marks.values())
    percentage = total / len(marks)

    return total, percentage


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+", "Outstanding"
    elif percentage >= 80:
        return "A", "Excellent"
    elif percentage >= 70:
        return "B+", "Very Good"
    elif percentage >= 60:
        return "B", "Good"
    elif percentage >= 50:
        return "C", "Average"
    elif percentage >= 40:
        return "D", "Pass"
    else:
        return "F", "Fail"


def result_status(marks):
    for mark in marks.values():
        if mark < 40:
            return "FAIL"

    return "PASS"


def highest_lowest(marks):
    highest_subject = max(marks, key=marks.get)
    lowest_subject = min(marks, key=marks.get)

    return (
        highest_subject,
        marks[highest_subject],
        lowest_subject,
        marks[lowest_subject]
    )


def display_report(student, marks, total, percentage):
    grade, remarks = calculate_grade(percentage)
    result = result_status(marks)

    high_sub, high_mark, low_sub, low_mark = highest_lowest(marks)

    print("\n")
    print("=" * 65)
    print("                  STUDENT REPORT CARD")
    print("=" * 65)

    print(f"Student Name : {student['name']}")
    print(f"Roll Number  : {student['roll']}")
    print(f"Course       : {student['course']}")
    print(f"Semester     : {student['semester']}")
    print(f"College      : {student['college']}")

    print("-" * 65)
    print("{:<40}{:>10}".format("Subject", "Marks"))
    print("-" * 65)

    for subject, mark in marks.items():
        print("{:<40}{:>10}".format(subject, mark))

    print("-" * 65)

    print(f"Total Marks : {total:.0f} / 500")
    print(f"Percentage  : {percentage:.2f}%")
    print(f"Grade       : {grade}")
    print(f"Result      : {result}")
    print(f"Remarks     : {remarks}")

    print("-" * 65)

    print(f"Highest Subject : {high_sub} ({high_mark})")
    print(f"Lowest Subject  : {low_sub} ({low_mark})")

    print("=" * 65)
    print("        Thank You for Using This Project")
    print("=" * 65)


def save_report(student, marks, total, percentage):
    grade, remarks = calculate_grade(percentage)
    result = result_status(marks)

    file_name = student["roll"] + "_Result.txt"

    with open(file_name, "w") as file:
        file.write("=" * 60 + "\n")
        file.write("STUDENT RESULT MANAGEMENT SYSTEM\n")
        file.write("=" * 60 + "\n\n")

        file.write(f"Student Name : {student['name']}\n")
        file.write(f"Roll Number  : {student['roll']}\n")
        file.write(f"Course       : {student['course']}\n")
        file.write(f"Semester     : {student['semester']}\n")
        file.write(f"College      : {student['college']}\n\n")

        file.write("-" * 60 + "\n")

        for subject, mark in marks.items():
            file.write(f"{subject:<40}{mark}\n")

        file.write("-" * 60 + "\n")

        file.write(f"Total Marks : {total:.0f}/500\n")
        file.write(f"Percentage  : {percentage:.2f}%\n")
        file.write(f"Grade       : {grade}\n")
        file.write(f"Result      : {result}\n")
        file.write(f"Remarks     : {remarks}\n")

    print(f"\nReport saved successfully as '{file_name}'")


def main():
    while True:
        display_header()

        student = get_student_details()
        marks = input_marks()

        total, percentage = calculate_percentage(marks)

        display_report(student, marks, total, percentage)
        save_report(student, marks, total, percentage)

        print()

        choice = input(
            "Do you want to enter another student's result? (Y/N): "
        ).upper()

        if choice != "Y":
            print("\nThank you for using Student Result Management System.")
            print("Have a Nice Day!")
            break


if __name__ == "__main__":
    main()