import pandas as pd
import matplotlib.pyplot as plt


class SalesDataAnalyzer:
    def __init__(self):
        self.data = None

    def load_data(self, file_path):
        try:
            self.data = pd.read_csv(file_path)
            print("Dataset loaded successfully!")
        except Exception as e:
            print("Error loading dataset:", e)

    def explore_data(self):
        if self.data is None:
            print("No dataset loaded!")
            return

        print("\n== Explore Data ==")
        print("1. Display the first 5 rows")
        print("2. Display the last 5 rows")
        print("3. Display column names")
        print("4. Display data types")
        print("5. Display basic info")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print(self.data.head())
        elif choice == 2:
            print(self.data.tail())
        elif choice == 3:
            print(self.data.columns)
        elif choice == 4:
            print(self.data.dtypes)
        elif choice == 5:
            print(self.data.info())

    def dataframe_operations(self):
        if self.data is None:
           print("No dataset loaded!")
           return

        print("\n== DataFrame Operations ==")
        print("1. Add new column")
        print("2. Delete column")
        print("3. Filter data")
        print("4. Sort data")
        print("5. Search value")

        choice = int(input("Enter your choice: "))

        if choice == 1:
         col_name = input("Enter new column name: ")
         value = input("Enter value for all rows: ")
         self.data[col_name] = value
         print(f"Column '{col_name}' added successfully!")

        elif choice == 2:
         col_name = input("Enter column name to delete: ")
         if col_name in self.data.columns:
              self.data.drop(columns=[col_name], inplace=True)
              print(f"Column '{col_name}' deleted successfully!")
         else:
              print("Column not found!")

        elif choice == 3:
         col = input("Enter column name: ")
         val = input("Enter value to filter: ")

         if col in self.data.columns:
            result = self.data[self.data[col].astype(str) == val]
            print(result)
         else:
            print("Invalid column name!")

        elif choice == 4:
         col = input("Enter column to sort by: ")
         order = input("Ascending? (yes/no): ")

         if col in self.data.columns:
            ascending = True if order.lower() == "yes" else False
            sorted_data = self.data.sort_values(by=col, ascending=ascending)
            print(sorted_data)
         else:
            print("Invalid column name!")

        elif choice == 5:
         val = input("Enter value to search: ")
         result = self.data[self.data.astype(str).apply(lambda row: row.str.contains(val).any(), axis=1)]
         print(result)

        else:
         print("Invalid choice!")

    def handle_missing_data(self):
        if self.data is None:
            print("No dataset loaded!")
            return

        print("\n== Handle Missing Data ==")
        print("1. Display rows with missing values")
        print("2. Fill missing values with mean")
        print("3. Drop rows with missing values")
        print("4. Replace missing values with a specific value")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            missing = self.data[self.data.isnull().any(axis=1)]
            if missing.empty:
                print("No missing values found in the dataset!")
            else:
                print(missing)

        elif choice == 2:
            self.data.fillna(self.data.mean(numeric_only=True), inplace=True)
            print("Missing values filled with mean!")

        elif choice == 3:
            self.data.dropna(inplace=True)
            print("Rows with missing values dropped!")

        elif choice == 4:
            value = input("Enter value to replace missing values: ")
            self.data.fillna(value, inplace=True)
            print("Missing values replaced!")

    def descriptive_stats(self):
        if self.data is None:
            print("No dataset loaded!")
            return

        print("\n== Descriptive Statistics ==")
        print(self.data.describe())

    def visualize_data(self):
     if self.data is None:
        print("No dataset loaded!")
        return

     print("\n== Data Visualization ==")
     print("1. Bar Plot")
     print("2. Line Plot")
     print("3. Scatter Plot")
     print("4. Pie Chart")
     print("5. Histogram")
     print("6. Stack Plot")

     choice = int(input("Enter your choice: "))

     print("Available columns:", list(self.data.columns))

     if choice == 1:
        col = input("Enter column for bar plot: ")
        if col in self.data.columns:
            self.data[col].value_counts().plot(kind='bar')
            plt.title("Bar Plot")
            plt.show()
        else:
            print("Invalid column!")

     elif choice == 2:
        x = input("Enter x-axis column: ")
        y = input("Enter y-axis column: ")

        if x in self.data.columns and y in self.data.columns:
            plt.plot(self.data[x], self.data[y])
            plt.xlabel(x)
            plt.ylabel(y)
            plt.title("Line Plot")
            plt.show()
        else:
            print("Invalid column!")

     elif choice == 3:
        x = input("Enter x-axis column name: ")
        y = input("Enter y-axis column name: ")

        if x in self.data.columns and y in self.data.columns:
            print("Generating scatter plot...")
            plt.scatter(self.data[x], self.data[y])
            plt.xlabel(x)
            plt.ylabel(y)
            plt.title("Scatter Plot")
            plt.show()
            print("Scatter plot displayed successfully!")
        else:
            print("Invalid column!")
     elif choice == 4:
        col = input("Enter column for pie chart: ")
        if col in self.data.columns:
            self.data[col].value_counts().plot(kind='pie', autopct='%1.1f%%')
            plt.title("Pie Chart")
            plt.ylabel("")
            plt.show()
        else:
            print("Invalid column!")
     elif choice == 5:
        col = input("Enter column for histogram: ")
        if col in self.data.columns:
            self.data[col].hist()
            plt.title("Histogram")
            plt.show()
        else:
            print("Invalid column!")
     elif choice == 6:
        print("Stack plot requires multiple numeric columns.")
        cols = input("Enter columns separated by comma: ").split(",")

        cols = [c.strip() for c in cols if c.strip() in self.data.columns]

        if len(cols) >= 2:
            self.data[cols].plot.area()
            plt.title("Stack Plot")
            plt.show()
        else:
            print("Enter at least 2 valid columns!")

     else:
        print("Invalid choice!")

    def save_plot(self):
        filename = input("Enter file name to save the plot (e.g., scatter_plot.png): ")
        plt.savefig(filename)
        print(f"Visualization saved as {filename} successfully!")


def main():
    analyzer = SalesDataAnalyzer()

    while True:
        print("\n========== Data Analysis & Visualization Program ==========")
        print("Please select an option:")
        print("1. Load Dataset")
        print("2. Explore Data")
        print("3. Perform DataFrame Operations")
        print("4. Handle Missing Data")
        print("5. Generate Descriptive Statistics")
        print("6. Data Visualization")
        print("7. Save Visualization")
        print("8. Exit")
        print("==========================================================")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("\n== Load Dataset ==")
            path = input("Enter the path of the dataset (CSV file): ")
            analyzer.load_data(path)

        elif choice == 2:
            analyzer.explore_data()

        elif choice == 3:
            analyzer.dataframe_operations()

        elif choice == 4:
            analyzer.handle_missing_data()

        elif choice == 5:
            analyzer.descriptive_stats()

        elif choice == 6:
            analyzer.visualize_data()

        elif choice == 7:
            print("\n== Save Visualization ==")
            analyzer.save_plot()

        elif choice == 8:
            print("Exiting the program, Goodbye!")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()