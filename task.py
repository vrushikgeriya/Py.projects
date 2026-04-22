import math
import time
from datetime import datetime
import uuid
import random
import string

class PackageModule:
    def __init__(self):
        self.dt = None
    def dt_operations(self):
        print("\nDate and Time Operations: ")
        print("1. Dispaly current date and time")
        print("2. Calculate difference betwwen two dates/times")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            now = datetime.now()
            print("Current Date & Time:", now)
        elif choice == 2:
            date1 = input("Enter first date (YYYY-MM-DD): ")
            date2 = input("Enter Second date (YYYY-MM-DD): ")
            d1 = datetime.strptime(date1, "%Y-%m-%d")
            d2 = datetime.strptime(date2, "%Y-%m-%d")
            difference = d2-d1
            print("Difference: ",difference)

        elif choice == 3:
            now = datetime.now()
            formatted_date = now.strftime("%d-%m-%Y %H:%M:%S")
            print("Formatted Date: ",formatted_date)
        elif choice == 4:
            input("press Enter to start stopwatch...")
            start = time.time()
            input("press Enter to stop stopwatch...")
            end = time.time()
            elapsed = end - start
            print("Time elapsed:", round(elapsed, 2), "seconds")

        elif choice == 5:
            seconds = int(input("Enter time in seconds: "))

            while seconds > 0:
             print("Time left:", seconds, "seconds")
             time.sleep(1)   
             seconds -= 1

            print("Time's up!")
        elif choice == 6:
            return
            

        else:
            print("Invalid choice!")
    def math_operations(self):
     print("\nMathematical Operations:")
     print("1. Calculate Factorial")
     print("2. Solve Compound Interest")
     print("3. Trigonometric Calculations")
     print("4. Area of Geometric Shapes")
     print("5. Back to Main Menu")

     choice = int(input("Enter your choice: "))

     if choice == 1:
        num = int(input("\nEnter a number: "))
        fact = 1
        for i in range(1, num + 1):
            fact = fact * i
        print("Factorial:", fact)

     elif choice == 2:
        p = float(input("\nEnter principal amount: "))
        r = float(input("Enter rate of interest (in %): "))
        t = float(input("Enter time (in years): "))

        amount = p * (1 + r/100) ** t
        print("Compound Interest:", round(amount, 2))

     elif choice == 3:
        angle = float(input("\nEnter angle in degrees: "))
        rad = math.radians(angle)

        print("Sin:", round(math.sin(rad), 2))
        print("Cos:", round(math.cos(rad), 2))
        print("Tan:", round(math.tan(rad), 2))

     elif choice == 4:
        print("\n1. Area of Circle")
        print("2. Area of Rectangle")
        print("3. Area of Triangle")

        shape = int(input("Choose shape: "))

        if shape == 1:
            r = float(input("Enter radius: "))
            area = math.pi * r * r
            print("Area of Circle:", round(area, 2))

        elif shape == 2:
            l = float(input("Enter length: "))
            b = float(input("Enter breadth: "))
            area = l * b
            print("Area of Rectangle:", area)

        elif shape == 3:
            b = float(input("Enter base: "))
            h = float(input("Enter height: "))
            area = 0.5 * b * h
            print("Area of Triangle:", area)

     elif choice == 5:
        return

     else:
        print("Invalid choice!")   

    def random_data(self):
     print("\nRandom Data Generation:")
     print("1. Generate Random Number")
     print("2. Generate Random List")
     print("3. Create Random Password")
     print("4. Generate Random OTP")
     print("5. Back to Main Menu")

     choice = int(input("Enter your choice: "))


     if choice == 1:
        num = random.randint(1, 100)
        print("Random Number:", num)

     elif choice == 2:
        size = int(input("\nEnter size of list: "))
        rand_list = []

        for i in range(size):
            rand_list.append(random.randint(1, 100))

        print("Random List:", rand_list)

     elif choice == 3:
        length = int(input("\nEnter password length: "))
        chars = string.ascii_letters + string.digits + string.punctuation

        password = ""
        for i in range(length):
            password += random.choice(chars)

        print("Generated Password:", password)

     elif choice == 4:
        otp = ""
        for i in range(6):
            otp += str(random.randint(0, 9))

        print("Generated OTP:", otp)

     elif choice == 5:
        return

     else:
        print("Invalid choice!") 


    def file_operations(self):
     print("\nFile Operations:")
     print("1. Create a new file")
     print("2. Write to a file")
     print("3. Read from a file")
     print("4. Append to a file")
     print("5. Back to Main Menu")

     choice = int(input("Enter your choice: "))

     if choice == 1:
        filename = input("\nEnter file name: ")
        f = open(filename, "w")
        f.close()
        print("File created successfully!")

     elif choice == 2:
        filename = input("\nEnter file name: ")
        data = input("Enter data to write: ")
        f = open(filename, "w")
        f.write(data)
        f.close()
        print("Data written successfully!")

     elif choice == 3:
        filename = input("\nEnter file name: ")
        f = open(filename, "r")
        content = f.read()
        f.close()
        print("File Content:")
        print(content)

     elif choice == 4:
        filename = input("\nEnter file name: ")
        data = input("Enter data to append: ")
        f = open(filename, "a")
        f.write("\n" + data)
        f.close()
        print("Data appended successfully!")

     elif choice == 5:
        return

     else:
        print("Invalid choice!")

    def explore_module(self):
     print("\nExplore Module Attributes:")

     m = input("Enter module to explore: ")

     module = __import__(m)
     attributes = dir(module)

     print(f"Available Attributes in {m} module:")
     print(attributes)




     

def main():
    task = PackageModule()
    
    while True:
     print("==========================")
     print("Welcome to Multi-Utility Toolkit")
     print("==========================")
     print("Choose an option: ")
     print("1. Datetime and Time Operations")
     print("2. Mathematical Operations")
     print("3. Random Data Generation")
     print("4. Generate Unique Identifiers (UUID)")
     print("5. File Operations (Custom Module)")
     print("6. Explore Module Attributes (dir())")
     print("7. Exit")
     print("==========================")

     choice = int(input("Enter your choice: "))

     if choice == 1:
         task.dt_operations()
     elif choice == 2:
         task.math_operations()
     elif choice == 3:
         task.random_data()
     elif choice == 4:
         print("Generated UUID: ",uuid.uuid4())  
     elif choice == 5:
        task.file_operations()
     elif choice == 6:
        task.explore_module()


         
     elif choice == 7:
         print("==========================")
         print("Thank you for using Multi-Utility Toolkit!")
         print("==========================")
         break
         
     else:
        print("\nInvalid choice!")
main()


    



