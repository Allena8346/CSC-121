# HR Database Management System - M6Lab Enhanced Version
# 10Nov25
# CSC-121 M6Lab
# Alexander Allen

"""
HR Database Management System - Main Program
Menu-driven interface for querying employee and department data
Enhanced with string validation and file output capabilities
"""

from hr_functions import (
    get_employee_info,
    get_employee_department,
    get_department_info,
    calculate_department_payroll,
    get_salary_statistics,
    find_highest_paid_employees,
    generate_department_report
)


def display_menu():
    """Display the main menu options"""
    print("\n" + "="*50)
    print("HR DATABASE MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Get Employee Information")
    print("2. Get Employee Department")
    print("3. Get Department Information")
    print("4. Calculate Department Payroll")
    print("5. Get Salary Statistics")
    print("6. Find Highest Paid Employees")
    print("7. Generate Department Report")
    print("8. Exit")
    print("="*50)


def main():
    """Main program loop"""
    
    choice = 0
    
    while choice != 8:
        display_menu()
        
        try:
            choice = int(input("\nEnter your choice (1-8): "))
            
            if choice == 1:
                employee_id = input("Enter employee ID: ")
                get_employee_info(employee_id)
            
            elif choice == 2:
                employee_id = input("Enter employee ID: ")
                get_employee_department(employee_id)
            
            elif choice == 3:
                department_name = input("Enter department name: ")
                get_department_info(department_name)
            
            elif choice == 4:
                department_name = input("Enter department name: ")
                calculate_department_payroll(department_name)
            
            elif choice == 5:
                department_name = input("Enter department name: ")
                get_salary_statistics(department_name)
            
            elif choice == 6:
                print("\nGenerating highest paid employees report...")
                find_highest_paid_employees(n=2)
            
            elif choice == 7:
                department_name = input("Enter department name: ")
                generate_department_report(department_name)
            
            elif choice == 8:
                print("\n" + "="*50)
                print("Thank you for using the HR Database Management System!")
                print("The program will now terminate.")
                print("="*50 + "\n")
            
            else:
                print("\nError: Invalid option! Please enter a number between 1 and 8.")
        
        except ValueError:
            print("\nError: Please enter a valid number!")
            choice = 0


if __name__ == "__main__":
    main()