# Functional Treat Project
# Data Analyzer and Transformer Program

dataset = []
dataset_summary = {}


def update_dataset_summary(data):
    global dataset_summary
    dataset_summary = {
        "total_elements": len(data),
        "average": sum(data) / len(data)
    }


def input_data():
    print("\n1. Enter data manually")
    print("2. Use sample data")
    choice = input("Please enter your choice: ")

    if choice == "1":
        values = input("Enter data for a 1D array (separated by spaces): ").split()
        data = [int(value) for value in values]
    elif choice == "2":
        data = [34, 12, 56, 78, 43, 21, 90]
        print("Sample data loaded successfully!")
    else:
        print("Invalid choice. Sample data loaded instead.")
        data = [34, 12, 56, 78, 43, 21, 90]

    update_dataset_summary(data)
    return data


def display_data_summary(data):
    print("\nData Summary:")
    print("- Total elements:", len(data))
    print("- Minimum value:", min(data))
    print("- Maximum value:", max(data))
    print("- Sum of all values:", sum(data))
    print("- Average value:", round(sum(data) / len(data), 2))


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def filter_data(data, threshold):
    filtered = list(filter(lambda x: x > threshold, data))
    return filtered


def sort_data(data):
    print("\nChoose sorting option:")
    print("1. Ascending")
    print("2. Descending")
    choice = input("Enter your choice: ")

    new_data = data[:]

    if choice == "1":
        new_data.sort()
        print("\nSorted Data in Ascending Order:")
        print(*new_data, sep=", ")
    elif choice == "2":
        new_data.sort(reverse=True)
        print("\nSorted Data in Descending Order:")
        print(*new_data, sep=", ")
    else:
        print("Invalid choice.")


def dataset_statistics(data):
    minimum = min(data)
    maximum = max(data)
    average = sum(data) / len(data)
    return minimum, maximum, average


def main():
    global dataset

    print("Welcome to the Data Analyzer and Transformer Program")

    while True:
        print("\nMain Menu:")
        print("1. Input Data")
        print("2. Display Data Summary (Built-in Functions)")
        print("3. Calculate Factorial (Recursion)")
        print("4. Filter Data by Threshold (Lambda Function)")
        print("5. Sort Data")
        print("6. Display Dataset Statistics (Return Multiple Values)")
        print("7. Exit Program")

        choice = input("Please enter your choice: ")

        if choice == "1":
            dataset = input_data()
            print("\nData has been stored successfully!")

        elif choice == "2":
            if dataset:
                display_data_summary(dataset)
            else:
                print("Please input data first.")

        elif choice == "3":
            number = int(input("\nEnter a number to calculate its factorial: "))
            print(f"\nFactorial of {number} is: {factorial(number)}")

        elif choice == "4":
            if dataset:
                threshold = int(input("\nEnter a threshold value to filter out data above this value: "))
                filtered = filter_data(dataset, threshold)
                print(f"\nFiltered Data (values > {threshold}):")
                if filtered:
                    print(*filtered, sep=", ")
                else:
                    print("No values found.")
            else:
                print("Please input data first.")

        elif choice == "5":
            if dataset:
                sort_data(dataset)
            else:
                print("Please input data first.")

        elif choice == "6":
            if dataset:
                minimum, maximum, average = dataset_statistics(dataset)
                print("\nDataset Statistics:")
                print("- Minimum value:", minimum)
                print("- Maximum value:", maximum)
                print("- Average value:", round(average, 2))
            else:
                print("Please input data first.")

        elif choice == "7":
            print("\nThank you for using the Data Analyzer and Transformer Program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


main()