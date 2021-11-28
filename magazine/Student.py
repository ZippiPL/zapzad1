class Student:

    def __init__(self, name: str, marks: int):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student {self.name} z ocenami {self.marks}"

    @property
    def is_passed(self) -> bool:
        return True if self.marks > 50 else False
