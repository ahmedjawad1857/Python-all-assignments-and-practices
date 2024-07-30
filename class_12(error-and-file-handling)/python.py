class StudentCard():
    def __init__(self, roll_no:int, name:str, age:int) -> None:
        if age < 18 or age > 60:
            raise StudentAgeError("Your are not eligible for this program!")
        self.roll_no = roll_no
        self.name = name
        self.age = age


class StudentAgeError(Exception):# custom error class
    pass

student1 = StudentCard(10,"John Doe",30)

print(f"Student Name:\n\t\"{student1.name}\"\n Student Roll_No:\n\t \"{student1.roll_no}\"\n Student Age:\n\t \"{student1.age}\"")

student1 = StudentCard(10,"John Doe",75)

print(f"Student Name:\n\t{student1.name}\n Student Roll_No:\n\t {student1.roll_no}\n Student Age:\n\t {student1.age}") # raise an error