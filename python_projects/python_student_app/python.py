from typing import Any

class StudentApp:
    def __init__(self) -> None:
        self.students: list[dict[str, Any]] = []

    def add_student(self, name: str, age: int, course: str) -> None:
        student = {"name": name, "age": age, "course": course, "id": len(self.students) + 1}
        self.students.append(student)
        print("Student added successfully.")

    def remove_student(self, id: int) -> None:
        for student in self.students:
            if student["id"] == id:
                self.students.remove(student)
                print("Student deleted successfully.")
        print("Student not found.")

    def update_student_info(self, id: int, new_name: str, new_age: int, new_course: str) -> None:
        for student in self.students:
            if student["id"] == id:
                student["name"] = new_name
                student["age"] = new_age
                student["course"] = new_course
                print("Student updated successfully.")
            else:
                print("Student not found")

    def display_students_info(self) -> None:
        if not self.students:
            print("No students to display.")
        print("List of students:")
        for student in self.students:
            print(f"Name: {student['name']}, Age: {student['age']}, course: {student['course']}, id:{student['id']}")

app = StudentApp()
while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Update Student")
    print("4. Display Students")
    print("5. Exit")

    choice = input("Enter your choice: ")

    match choice:
        case '1':
            name = input("Enter student's name: ")
            age = int(input("Enter student's age: "))
            course = input("Enter student's course: ")
            app.add_student(name, age, course)
        case '2':
            id = int(input("Enter student's id to delete: "))  
            app.remove_student(id)
        case '3':
            id = int(input("Enter student's id to update: "))
            new_name = input("Enter student's name:  ")
            new_age = int(input("Enter new age: "))
            new_course = input("Enter new course: ")
            app.update_student_info(id, new_name, new_age, new_course)
        case '4':
            app.display_students_info()
        case '5':
            print("Exiting the program.")
            break
        case _:
            print("Invalid choice. Please enter a valid option.")
