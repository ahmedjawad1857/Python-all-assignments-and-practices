from typing import Union

PerType = Union[float, int]

percentages: list[PerType] = [22, 33, 34, 9, 65, 33]
grades: list[str] = []

for per in percentages:
    grade: str = ""

    if 0 <= per < 33:
        grade = "Fail"
    elif 33 <= per < 40:
        grade = "E"
    elif 40 <= per < 50:
        grade = "D"
    elif 50 <= per < 60:
        grade = "C"
    elif 60 <= per < 70:
        grade = "B"
    elif 70 <= per < 80:
        grade = "A"
    elif 80 <= per <= 100:
        grade = "A+"

    grades.append(grade)
    print(f"Percentage: {per}%, Grade: {grade}")

print("\nPercentages of students in exams:", percentages)
print("Grades of the students are:", grades)
