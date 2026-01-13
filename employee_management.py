class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id},{self.name},{self.salary}"


class EmployeeManagement:
    def __init__(self, filename="employees.txt"):
        self.filename = filename

    def add_employee(self):
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        salary = input("Enter Salary: ")

        emp = Employee(emp_id, name, salary)

        with open(self.filename, "a") as file:
            file.write(str(emp) + "\n")

        print("✅ Employee added successfully")

    def view_employees(self):
        try:
            with open(self.filename, "r") as file:
                print("\n--- Employee List ---")
                for line in file:
                    emp_id, name, salary = line.strip().split(",")
                    print(f"ID: {emp_id}, Name: {name}, Salary: {salary}")
        except FileNotFoundError:
            print("No employee records found")

    def search_employee(self):
        search_id = input("Enter Employee ID to search: ")
        found = False

        with open(self.filename, "r") as file:
            for line in file:
                emp_id, name, salary = line.strip().split(",")
                if emp_id == search_id:
                    print(f"Found → ID: {emp_id}, Name: {name}, Salary: {salary}")
                    found = True
                    break

        if not found:
            print("❌ Employee not found")

    def delete_employee(self):
        delete_id = input("Enter Employee ID to delete: ")
        lines = []

        with open(self.filename, "r") as file:
            lines = file.readlines()

        with open(self.filename, "w") as file:
            for line in lines:
                emp_id, _, _ = line.strip().split(",")
                if emp_id != delete_id:
                    file.write(line)

        print("✅ Employee deleted successfully")


def main():
    system = EmployeeManagement()

    while True:
        print("\n1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            system.add_employee()
        elif choice == "2":
            system.view_employees()
        elif choice == "3":
            system.search_employee()
        elif choice == "4":
            system.delete_employee()
        elif choice == "5":
            print("Thank you!")
            break
        else:
            print("Invalid choice")


main()
