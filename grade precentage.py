class Student:
    def __init__(self, name):
        self.name = name
        self.subject1 = float(input(f"Enter the marks of {self.name} in subject 1: "))
        self.subject2 = float(input(f"Enter the marks of {self.name} in subject 2: "))

    def calculate_average(self):
        return (self.subject1 + self.subject2) / 2

# Create two student objects
student1 = Student("Student 1")
student2 = Student("Student 2")

# Calculate and display average marks
print(f"\nAverage marks for {student1.name}: {student1.calculate_average():.2f}")
print(f"Average marks for {student2.name}: {student2.calculate_average():.2f}")
