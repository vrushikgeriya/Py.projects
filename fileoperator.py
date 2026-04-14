import os
from datetime import datetime

class JournalManager:

    def __init__(self, filename="journal.txt"):
        self.filename = filename

    def add_entry(self):
        entry = input("Enter your journal entry:\n")
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

        file = open(self.filename, "a")
        file.write(timestamp + "\n")
        file.write(entry + "\n\n")
        file.close()

        print("\nEntry added successfully!")

    def view_entries(self):
        if not os.path.exists(self.filename):
            print("\nNo journal entries found. Start by adding a new entry!")
            return

        file = open(self.filename, "r")
        content = file.read()
        file.close()

        if content.strip() == "":
            print("\nNo journal entries found. Start by adding a new entry!")
        else:
            print("\nYour Journal Entries:")
            print("------------------------------")
            print(content)

    def search_entry(self):
        if not os.path.exists(self.filename):
            print("\nError: The journal file does not exist. Please add a new entry first.")
            return

        keyword = input("Enter a keyword or date to search: ")

        file = open(self.filename, "r")
        lines = file.readlines()
        file.close()

        found = False
        print("\nMatching Entries:")
        print("------------------------------")

        for line in lines:
            if keyword.lower() in line.lower():
                print(line.strip())
                found = True

        if not found:
            print(f"\nNo entries were found for the keyword: {keyword}.")

    def delete_entries(self):
        confirm = input("Are you sure you want to delete all entries? (yes/no): ")

        if confirm.lower() == "yes":
            if os.path.exists(self.filename):
                os.remove(self.filename)
                print("\nAll journal entries have been deleted.")
            else:
                print("\nNo journal entries to delete.")
        else:
            print("\nDeletion cancelled.")


def main():
    jm = JournalManager()

    while True:
        print("\nWelcome to Personal Journal Manager!")
        print("Please select an option:\n")
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Exit")

        choice = input("\nUser Input:\n")

        if choice == "1":
            jm.add_entry()

        elif choice == "2":
            jm.view_entries()

        elif choice == "3":
            jm.search_entry()

        elif choice == "4":
            jm.delete_entries()

        elif choice == "5":
            print("\nThank you for using Personal Journal Manager. Goodbye!")
            break

        else:
            print("\nInvalid option. Please select a valid option from the menu.")


if __name__ == "__main__":
    main()