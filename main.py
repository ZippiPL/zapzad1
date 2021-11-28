from magazine.Student import Student


if __name__ == '__main__':
    print("start")
    student_one = Student('Lukasz', 51)
    student_two = Student('Bartek', 49)
    print(student_one.is_passed)
    print(student_two.is_passed)
