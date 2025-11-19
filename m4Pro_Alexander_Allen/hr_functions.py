#
#
#
#

"""
HR Functions Module
Contains all functions for querying and analyzing HR database
"""

from company_db_dict import company_db


def get_employee_info(employee_id):
    """Displays all information for a specific employee"""
    # Search through all departments for the employee
    for dept_name, dept_data in company_db.items():
        if employee_id in dept_data['employees']:
            emp_info = dept_data['employees'][employee_id]['personal_info']
            
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
    print(f"\nError: No employee found with ID '{employee_id}'")


def get_employee_department(employee_id):
    """Displays the department name where employee works (department location)"""
    # Search through all departments for the employee
    for dept_name, dept_data in company_db.items():
        if employee_id in dept_data['employees']:
            dept_info = dept_data['department_info']
            emp_name = dept_data['employees'][employee_id]['personal_info']['name']
            
            print("\n" + "="*50)
            print("EMPLOYEE DEPARTMENT")
            print("="*50)
            print(f"Employee:    {emp_name}")
            print(f"Department:  {dept_info['name']}")
            print(f"Location:    {dept_info['location']}")
            print("="*50)
            return
    
    # If we get here, employee wasn't found
    print(f"\nError: No employee found with ID '{employee_id}'")


def get_department_info(department_name):
    """Displays the department budget, location, manager's id AND name"""
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
    """Calculate and displays total payroll (salary) for a department"""
    dept_name = department_name.lower()
    
    if dept_name not in company_db:
        print(f"\nError: No department found with name '{department_name}'")
        return
    
    dept_info = company_db[dept_name]['department_info']
    employees = company_db[dept_name]['employees']
    
    print("\n" + "="*60)
    print(f"{dept_info['name'].upper()} DEPARTMENT PAYROLL")
    print("="*60)
    print(f"{'Employee Name':<25}{'Salary':>15}")
    print("-"*60)
    
    total_payroll = 0
    for emp_id, emp_data in employees.items():
        emp_info = emp_data['personal_info']
        name = emp_info['name']
        salary = emp_info['salary']
        total_payroll += salary
        print(f"{name:<25}${salary:>14,}")
    
    print("-"*60)
    print(f"{'TOTAL PAYROLL:':<25}${total_payroll:>14,}")
    print("="*60)


def get_salary_statistics(department_name):
    """Displays min, max, and average salary for department"""
    dept_name = department_name.lower()
    
    if dept_name not in company_db:
        print(f"\nError: No department found with name '{department_name}'")
        return
    
    dept_info = company_db[dept_name]['department_info']
    employees = company_db[dept_name]['employees']
    
    # Collect all salaries
    salaries = []
    for emp_id, emp_data in employees.items():
        salaries.append(emp_data['personal_info']['salary'])
    
    min_salary = min(salaries)
    max_salary = max(salaries)
    avg_salary = sum(salaries) / len(salaries)
    
    print("\n" + "="*50)
    print(f"{dept_info['name'].upper()} SALARY STATISTICS")
    print("="*50)
    print(f"Minimum Salary:  ${min_salary:>12,}")
    print(f"Maximum Salary:  ${max_salary:>12,}")
    print(f"Average Salary:  ${avg_salary:>12,.2f}")
    print(f"Employee Count:  {len(salaries):>12}")
    print("="*50)


def find_highest_paid_employees(n=2):
    """Displays top N highest paid employees, display their name, 
    department they work at, positions and their salaries"""
    
    # Helper function to get salary from employee dictionary
    def get_salary(employee):
        """Returns the salary value for sorting"""
        return employee['salary']
    
    # Collect all employees with their info
    all_employees = []
    
    for dept_name, dept_data in company_db.items():
        dept_info = dept_data['department_info']
        for emp_id, emp_data in dept_data['employees'].items():
            emp_info = emp_data['personal_info']
            all_employees.append({
                'name': emp_info['name'],
                'department': dept_info['name'],
                'position': emp_info['position'],
                'salary': emp_info['salary']
            })
    
    # Sort by salary in descending order
    all_employees.sort(key=get_salary, reverse=True)
    
    # Get top N employees
    top_employees = all_employees[:n]
    
    print("\n" + "="*80)
    print(f"TOP {n} HIGHEST PAID EMPLOYEES")
    print("="*80)
    print(f"{'Name':<20}{'Department':<20}{'Position':<25}{'Salary':>15}")
    print("-"*80)
    
    for emp in top_employees:
        print(f"{emp['name']:<20}{emp['department']:<20}{emp['position']:<25}${emp['salary']:>14,}")
    
    print("="*80)


def generate_department_report(department_name):
    """Generate comprehensive department report including: 
    Employee count, Total payroll, Average salary"""
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

