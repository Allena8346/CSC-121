"""
HR Functions Module - Enhanced for M6Lab
Contains all functions for querying and analyzing HR database
with string validation and file I/O capabilities
"""

from company_db_dict import company_db
import csv


def validate_employee_id(employee_id):
    """
    Validates employee ID format: emp_XXX where X is a digit
    Returns tuple: (is_valid, error_message, corrected_id)
    """
    # Convert to lowercase for checking
    emp_id_lower = employee_id.lower()
    
    # Check if starts with "emp"
    if not emp_id_lower.startswith("emp"):
        return False, "Employee ID must start with 'emp'", None
    
    # Check if "emp" is followed by underscore
    if len(emp_id_lower) < 4 or emp_id_lower[3] != "_":
        return False, "Employee ID must have an underscore after 'emp' (format: emp_XXX)", None
    
    # Check if underscore is followed by exactly 3 digits
    if len(emp_id_lower) != 7:
        return False, "Employee ID must have exactly 3 digits after underscore (format: emp_XXX)", None
    
    # Check if last 3 characters are digits
    if not emp_id_lower[4:].isdigit():
        return False, "Employee ID must have exactly 3 digits after underscore (format: emp_XXX)", None
    
    return True, "", emp_id_lower


def get_employee_info(employee_id):
    """Displays all information for a specific employee with validation"""
    # Validate employee ID format
    is_valid, error_msg, corrected_id = validate_employee_id(employee_id)
    
    if not is_valid:
        print(f"\nError: Invalid employee ID format!")
        print(f"Issue: {error_msg}")
        return
    
    # Search through all departments for the employee
    for dept_name, dept_data in company_db.items():
        if corrected_id in dept_data['employees']:
            emp_info = dept_data['employees'][corrected_id]['personal_info']
            
            print("\n" + "="*50)
            print("EMPLOYEE INFORMATION")
            print("="*50)
            print(f"Employee ID:  {emp_info['employee_id']}")
            print(f"Name:         {emp_info['name']}")
            print(f"Position:     {emp_info['position']}")
            print(f"Email:        {emp_info['email']}")
            print(f"Phone:        {emp_info['phone']}")
            print(f"Hire Date:    {emp_info['hire_date']}")
            print(f"Salary:       ${emp_info['salary']:,}")
            print("="*50)
            return
    
    # If we get here, employee wasn't found
    print(f"\nError: No employee found with ID '{corrected_id}'")


def get_employee_department(employee_id):
    """Displays the department name where employee works with validation"""
    # Validate employee ID format
    is_valid, error_msg, corrected_id = validate_employee_id(employee_id)
    
    if not is_valid:
        print(f"\nError: Invalid employee ID format!")
        print(f"Issue: {error_msg}")
        return
    
    # Search through all departments for the employee
    for dept_name, dept_data in company_db.items():
        if corrected_id in dept_data['employees']:
            dept_info = dept_data['department_info']
            emp_name = dept_data['employees'][corrected_id]['personal_info']['name']
            
            print("\n" + "="*50)
            print("EMPLOYEE DEPARTMENT")
            print("="*50)
            print(f"Employee:    {emp_name}")
            print(f"Department:  {dept_info['name']}")
            print(f"Location:    {dept_info['location']}")
            print("="*50)
            return
    
    # If we get here, employee wasn't found
    print(f"\nError: No employee found with ID '{corrected_id}'")


def get_department_info(department_name):
    """Displays the department budget, location, manager's id AND name"""
    # Convert to lowercase for lookup
    dept_name = department_name.lower()
    
    if dept_name not in company_db:
        print(f"\nError: No department found with name '{department_name}'")
        return
    
    dept_info = company_db[dept_name]['department_info']
    manager_id = dept_info['manager']
    manager_name = company_db[dept_name]['employees'][manager_id]['personal_info']['name']
    
    print("\n" + "="*50)
    print("DEPARTMENT INFORMATION")
    print("="*50)
    print(f"Department:   {dept_info['name']}")
    print(f"Location:     {dept_info['location']}")
    print(f"Budget:       ${dept_info['budget']:,}")
    print(f"Manager ID:   {manager_id}")
    print(f"Manager Name: {manager_name}")
    print("="*50)


def calculate_department_payroll(department_name):
    """Calculate and write department payroll to CSV file"""
    # Convert to lowercase for lookup
    dept_name = department_name.lower()
    
    if dept_name not in company_db:
        print(f"\nError: No department found with name '{department_name}'")
        return
    
    employees = company_db[dept_name]['employees']
    
    # Create CSV file
    filename = f"{dept_name}.csv"
    
    try:
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            
            # Write header row
            writer.writerow(['Employee Id', 'Employee Name', 'Salary'])
            
            # Write employee data and calculate total
            total_payroll = 0
            for emp_id, emp_data in employees.items():
                emp_info = emp_data['personal_info']
                name = emp_info['name']
                salary = emp_info['salary']
                total_payroll += salary
                writer.writerow([emp_id, name, f'${salary:,}'])
            
            # Write total row
            writer.writerow(['', '', f'${total_payroll:,}'])
        
        print(f"\nPayroll data successfully written to '{filename}'")
        print(f"Total Payroll: ${total_payroll:,}")
        
    except Exception as e:
        print(f"\nError writing to file: {e}")


def get_salary_statistics(department_name):
    """Write salary statistics to text file"""
    # Convert to lowercase for lookup
    dept_name = department_name.lower()
    
    if dept_name not in company_db:
        print(f"\nError: No department found with name '{department_name}'")
        return
    
    dept_info = company_db[dept_name]['department_info']
    employees = company_db[dept_name]['employees']
    
    # Find min and max salary employees
    min_salary = float('inf')
    max_salary = 0
    min_emp_id = ""
    max_emp_id = ""
    total_salary = 0
    
    for emp_id, emp_data in employees.items():
        salary = emp_data['personal_info']['salary']
        total_salary += salary
        
        if salary < min_salary:
            min_salary = salary
            min_emp_id = emp_id
        
        if salary > max_salary:
            max_salary = salary
            max_emp_id = emp_id
    
    avg_salary = total_salary / len(employees)
    
    # Get employee names
    min_emp_name = employees[min_emp_id]['personal_info']['name']
    max_emp_name = employees[max_emp_id]['personal_info']['name']
    
    # Write to text file
    filename = f"{dept_name}.txt"
    
    try:
        with open(filename, 'w') as txtfile:
            # Write centered title
            title = f"{dept_info['name']} Department Statistics"
            txtfile.write(title.center(60) + "\n")
            txtfile.write("="*60 + "\n\n")
            
            # Write lowest salary info
            txtfile.write("Lowest Salary:\n")
            txtfile.write(f"  Employee id: {min_emp_id}\n")
            txtfile.write(f"  Employee name: {min_emp_name}\n")
            txtfile.write(f"  Salary: ${min_salary:,}\n\n")
            
            # Write highest salary info
            txtfile.write("Highest Salary:\n")
            txtfile.write(f"  Employee id: {max_emp_id}\n")
            txtfile.write(f"  Employee name: {max_emp_name}\n")
            txtfile.write(f"  Salary: ${max_salary:,}\n\n")
            
            # Write average salary
            txtfile.write(f"Salary Average: ${avg_salary:,.2f}\n")
        
        print(f"\nSalary statistics successfully written to '{filename}'")
        
    except Exception as e:
        print(f"\nError writing to file: {e}")


def find_highest_paid_employees(n=2):
    """Write top N highest paid employees from each department to files"""
    
    # Collect all employees with their info
    all_employees = []
    
    for dept_name, dept_data in company_db.items():
        dept_info = dept_data['department_info']
        
        # Get employees for this department
        dept_employees = []
        for emp_id, emp_data in dept_data['employees'].items():
            emp_info = emp_data['personal_info']
            dept_employees.append({
                'dept_name': dept_info['name'],
                'emp_id': emp_info['employee_id'],
                'name': emp_info['name'],
                'position': emp_info['position'],
                'salary': emp_info['salary']
            })
        
        # Sort by salary descending
        for i in range(len(dept_employees)):
            for j in range(i + 1, len(dept_employees)):
                if dept_employees[j]['salary'] > dept_employees[i]['salary']:
                    dept_employees[i], dept_employees[j] = dept_employees[j], dept_employees[i]
        
        # Get top N from this department
        top_n = dept_employees[:n]
        all_employees.extend(top_n)
    
    # Write to CSV file
    try:
        with open('highest_paid.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Dep Name', 'EmpId', 'Employee Name', 'Position', 'Salary'])
            
            for emp in all_employees:
                writer.writerow([
                    emp['dept_name'],
                    emp['emp_id'],
                    emp['name'],
                    emp['position'],
                    f"${emp['salary']:,}"
                ])
        
        print("\nCSV file 'highest_paid.csv' created successfully")
        
    except Exception as e:
        print(f"\nError writing CSV file: {e}")
    
    # Write to text file
    try:
        with open('highest_paid.txt', 'w') as txtfile:
            # Write header
            txtfile.write(f"{'Dep Name':<15}{'EmpId':<12}{'Employee Name':<25}{'Position':<30}{'Salary':>15}\n")
            txtfile.write("="*97 + "\n")
            
            for emp in all_employees:
                txtfile.write(f"{emp['dept_name']:<15}{emp['emp_id']:<12}{emp['name']:<25}{emp['position']:<30}${emp['salary']:>14,}\n")
        
        print("Text file 'highest_paid.txt' created successfully")
        
    except Exception as e:
        print(f"\nError writing text file: {e}")


def generate_department_report(department_name):
    """Generate comprehensive department report"""
    # Convert to lowercase for lookup
    dept_name = department_name.lower()
    
    if dept_name not in company_db:
        print(f"\nError: No department found with name '{department_name}'")
        return
    
    dept_info = company_db[dept_name]['department_info']
    employees = company_db[dept_name]['employees']
    
    # Calculate statistics
    employee_count = len(employees)
    salaries = [emp_data['personal_info']['salary'] for emp_data in employees.values()]
    total_payroll = sum(salaries)
    avg_salary = total_payroll / employee_count
    
    # Get manager info
    manager_id = dept_info['manager']
    manager_name = employees[manager_id]['personal_info']['name']
    
    print("\n" + "="*60)
    print(f"{dept_info['name'].upper()} DEPARTMENT REPORT")
    print("="*60)
    print(f"\nDepartment Information:")
    print(f"  Location:        {dept_info['location']}")
    print(f"  Budget:          ${dept_info['budget']:,}")
    print(f"  Manager:         {manager_name} ({manager_id})")
    
    print(f"\nStaffing Information:")
    print(f"  Employee Count:  {employee_count}")
    
    print(f"\nPayroll Information:")
    print(f"  Total Payroll:   ${total_payroll:,}")
    print(f"  Average Salary:  ${avg_salary:,.2f}")
    print(f"  Minimum Salary:  ${min(salaries):,}")
    print(f"  Maximum Salary:  ${max(salaries):,}")
    
    print(f"\nEmployee Roster:")
    print(f"  {'Name':<25}{'Position':<30}{'Salary':>15}")
    print("  " + "-"*70)
    
    for emp_id, emp_data in employees.items():
        emp_info = emp_data['personal_info']
        print(f"  {emp_info['name']:<25}{emp_info['position']:<30}${emp_info['salary']:>14,}")
    
    print("="*60)