class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def display(self):
        print("\nPerson Details:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Employee(Person):
    def __init__(self, name="", age=0, employee_id="", salary=0.0):
        super().__init__(name, age)
        self.__employee_id = employee_id
        self.__salary = salary

    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def display(self):
        print("\nEmployee Details:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.__employee_id}")
        print(f"Salary: ${self.__salary}")

    def __del__(self):
        pass


class Manager(Employee):
    def __init__(self, name="", age=0, employee_id="", salary=0.0, department=""):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display(self):
        print("\nManager Details:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.get_employee_id()}")
        print(f"Salary: ${self.get_salary()}")
        print(f"Department: {self.department}")


people = []


def menu():
    print("\n--- Python OOP Project: Employee Management System ---")
    print("\nChoose an operation:")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Exit")


while True:
    menu()
    choice = input("\nEnter your choice: ")

    if choice == "1":
        name = input("\nEnter Name: ")
        age = int(input("Enter Age: "))
        person = Person(name, age)
        people.append(person)
        print(f"\nPerson created with name: {name} and age: {age}.")
        print("\n--- Choose another operation ---")

    elif choice == "2":
        name = input("\nEnter Name: ")
        age = int(input("Enter Age: "))
        employee_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        employee = Employee(name, age, employee_id, salary)
        people.append(employee)
        print(f"\nEmployee created with name: {name}, age: {age}, ID: {employee_id}, and salary: ${salary}.")
        print("\n--- Choose another operation ---")

    elif choice == "3":
        name = input("\nEnter Name: ")
        age = int(input("Enter Age: "))
        employee_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        department = input("Enter Department: ")
        manager = Manager(name, age, employee_id, salary, department)
        people.append(manager)
        print(f"\nManager created with name: {name}, age: {age}, ID: {employee_id}, salary: ${salary}, and department: {department}.")
        print("\n--- Choose another operation ---")

    elif choice == "4":
        if len(people) == 0:
            print("\nNo records found.")
            print("\n--- Choose another operation ---")
            continue

        print("\nChoose details to show:")
        for i in range(len(people)):
            if isinstance(people[i], Manager):
                print(f"{i + 1}. Manager")
            elif isinstance(people[i], Employee):
                print(f"{i + 1}. Employee")
            else:
                print(f"{i + 1}. Person")

        detail_choice = int(input("\nEnter your choice: "))

        if 1 <= detail_choice <= len(people):
            people[detail_choice - 1].display()
        else:
            print("\nInvalid choice.")

        print("\n--- Choose another operation ---")

    elif choice == "5":
        print("\nExiting the system. All resources have been freed.")
        print("\nGoodbye!")
        break

    else:
        print("\nInvalid choice. Please try again.")