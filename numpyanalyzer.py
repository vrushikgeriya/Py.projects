import numpy as np

class DataAnalytics:
 def __init__(self):
  self.array = None

 def create_array(self):
        print("\nArray Creation:")
        print("Select the type of array to create:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            size = int(input("Enter number of elements: "))
            elements = list(map(int, input(f"Enter {size} elements separated by space: ").split()))
            self.array = np.array(elements)

        elif choice == 2:
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of coloumns: "))
            elements = list(map(int,input(f"Enter {rows * cols} elements seperated by space: ").split()))
            self.array = np.array(elements).reshape(rows,cols)

        elif choice == 3:
             depth = int(input("Enter Depth: "))
             rows = int(input("Enter number of rows: "))
             cols = int(input("Enter number of coloumns: "))
             elements = list(map(int,input(f"Enter {depth* rows * cols} elements seperated by space: ").split()))
             self.array = np.array(elements).reshape(depth,rows,cols)           


        else:
            print("\nInavlid choice")
            return
        print("\nArray Created Successfully")
        print(self.array)


 def mathematical_operations(self):

    if self.array is None:
        print("\nPlease create an array first!")
        return

    print("\nChoose a mathematical operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Enter your choice: "))

    total_elements = self.array.size

    elements = list(map(int, input(
        f"\nEnter the same-size array elements ({total_elements} elements separated by space): "
    ).split()))

    second_array = np.array(elements).reshape(self.array.shape)

    print("\nOriginal Array:")
    print(self.array)

    print("\nSecond Array:")
    print(second_array)

    if choice == 1:
        result = self.array + second_array
        print("\nResult of Addition:")
        print(result)

    elif choice == 2:
        result = self.array - second_array
        print("\nResult of Subtraction:")
        print(result)

    elif choice == 3:
        result = self.array * second_array
        print("\nResult of Multiplication:")
        print(result)

    elif choice == 4:
        result = self.array / second_array
        print("\nResult of Division:")
        print(result)

    else:
        print("\nInvalid Choice")
 
 def combine_split_arrays(self):

    if self.array is None:
        print("\nPlease create an array first!")
        return

    print("\nChoose an option:")
    print("1. Combine Arrays")
    print("2. Split Array")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        total_elements = self.array.size

        elements = list(map(int, input(
            f"\nEnter the elements of another array to combine ({total_elements} elements separated by space): "
        ).split()))

        second_array = np.array(elements).reshape(self.array.shape)

        print("\nOriginal Array:")
        print(self.array)

        print("\nSecond Array:")
        print(second_array)

        combined = np.vstack((self.array, second_array))

        print("\nCombined Array (Vertical Stack):")
        print(combined)

    elif choice == 2:

        print("\nOriginal Array:")
        print(self.array)

        split_arrays = np.array_split(self.array, 2)

        print("\nSplit Arrays:")

        for i in range(len(split_arrays)):
            print(f"\nPart {i+1}:")
            print(split_arrays[i])

    else:
        print("\nInvalid Choice")


 def search_sort_filter(self):

    if self.array is None:
        print("\nPlease create an array first!")
        return

    print("\nChoose an option:")
    print("1. Search a value")
    print("2. Sort the array")
    print("3. Filter values")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        value = int(input("\nEnter value to search: "))

        print("\nOriginal Array:")
        print(self.array)

        result = np.where(self.array == value)

        print(f"\nValue {value} found at index positions:")
        print(result)

    elif choice == 2:

        print("\nOriginal Array:")
        print(self.array)

        sorted_array = np.sort(self.array)

        print("\nSorted Array:")
        print(sorted_array)

        print("(Sorting applied row-wise.)")

    elif choice == 3:

        value = int(input("\nShow values greater than: "))

        print("\nOriginal Array:")
        print(self.array)

        filtered = self.array[self.array > value]

        print(f"\nFiltered Values Greater Than {value}:")
        print(filtered)

    else:
        print("\nInvalid Choice")
 def aggregates_statistics(self):

    if self.array is None:
        print("\nPlease create an array first!")
        return

    print("\nAggregates and Statistics:")
    print("Choose an aggregate/statistical operation:")
    print("1. Sum")
    print("2. Mean")
    print("3. Median")
    print("4. Standard Deviation")
    print("5. Variance")

    choice = int(input("Enter your choice: "))

    print("\nOriginal Array:")
    print(self.array)

    if choice == 1:

        result = np.sum(self.array)

        print(f"\nSum of Array: {result}")

    elif choice == 2:

        result = np.mean(self.array)

        print(f"\nMean of Array: {result}")

    elif choice == 3:

        result = np.median(self.array)

        print(f"\nMedian of Array: {result}")

    elif choice == 4:

        result = np.std(self.array)

        print(f"\nStandard Deviation of Array: {result}")

    elif choice == 5:

        result = np.var(self.array)

        print(f"\nVariance of Array: {result}")

    else:
        print("\nInvalid Choice")

def main():
    analyzer = DataAnalytics() 
    


    while True:
       print("Welccome to the Numpy Analyzer!")
       print("========================================")
       print("Choose an option:")
       print("1. Create a numpy Array")
       print("2. Perform a Mathematical Operatoions")
       print("3. Combine or Split Arrays")
       print("4. Search, Sort, or Filter Arrays")
       print("5. Compute Aggregates and Statistics")
       print("6. Exit")
       choice = int(input("Enter your choice: "))

       if choice == 1:
           analyzer.create_array()
       elif choice == 2:
           analyzer.mathematical_operations()
       elif choice == 3:
           analyzer.combine_split_arrays()
       elif choice == 4:
           analyzer.search_sort_filter()
       elif choice == 5:
           analyzer.aggregates_statistics()        
       elif choice == 6:
           print("\nThank you for using the NumPy Analyzer! Goodbye! \n")
           break
       else:
           print("\nInvalid Choice!")
main ()
    
        

