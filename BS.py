class EmployeePerformanceExpertSystem:

    def __init__(self):

        self.criteria = {}

        self.employee_data = {}

 

    def add_evaluation_criteria(self, criterion, weight):

        self.criteria[criterion] = weight

 

    def add_employee_data(self, employee_id, data):

        self.employee_data[employee_id] = data

 

    def evaluate_performance(self, employee_id):

        if employee_id in self.employee_data:

            employee_data = self.employee_data[employee_id]

            total_score = 0

 

            print("Performance Evaluation for Employee ID:", employee_id)

            print("Evaluation Criteria and Weightage:")

            for criterion, weight in self.criteria.items():

                print(f"{criterion}: {weight}")

                score = input(f"Enter the score for {criterion}: ")

                total_score += float(score) * weight

 

            print("------------------------------")

            print("Total Performance Score:", total_score)

        else:

            print("Employee ID not found.")

 

    def interact(self):

        print("Welcome to the Employee Performance Evaluation Expert System!")

        print("Add evaluation criteria, employee data, and evaluate performance.")

 

        while True:

            print("1. Add Evaluation Criteria")

            print("2. Add Employee Data")

            print("3. Evaluate Performance")

            print("4. Exit")

 

            choice = input("Enter your choice (1-4): ")

            print("--------------------------")

 

            if choice == "1":

                criterion = input("Enter the evaluation criterion: ")

                weight = float(input("Enter the weightage (0-1): "))

                self.add_evaluation_criteria(criterion, weight)

            elif choice == "2":

                employee_id = input("Enter the employee ID: ")

                data = input("Enter the employee data: ")

                self.add_employee_data(employee_id, data)

            elif choice == "3":

                employee_id = input("Enter the employee ID for performance evaluation: ")

                self.evaluate_performance(employee_id)

            elif choice == "4":

                print("Goodbye!")

                break

            else:

                print("Invalid choice. Please try again.")

            print("------------------------------")

 

 

expert_system = EmployeePerformanceExpertSystem()

expert_system.interact()
