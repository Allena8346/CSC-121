# Sales Data Processing Functions Module
# 29Oct25
# CSC121 M5Lab
# Alexander Allen

"""
Module containing utility functions for sales data processing.
Handles reading CSV files, calculating sales totals, and generating reports.
Provides functions for product and customer sales analysis.
"""

import csv

# Constants for formatting
REPORT_WIDTH = 60
COLUMN_WIDTH = 20


def read_sales_data(filename):
    """
    Read sales data from CSV file and return as a list of dictionaries.
    Each dictionary represents one sales transaction record.
    
    Parameters:
        filename (str): Name of the CSV file to read
        
    Returns:
        list: List of dictionaries containing sales records, empty list if error
    """
    sales_data = []
    file = open(filename, 'r')
    reader = csv.DictReader(file)
    
    for row in reader:
        sales_data.append(row)
    
    file.close()
    
    if len(sales_data) > 0:
        print(f"   Successfully read {len(sales_data)} records from {filename}")
    else:
        print(f"   Warning: No data found in {filename}")
    
    return sales_data


def calculate_product_totals(sales_data):
    """
    Calculate total sales for each product.
    Total sales = units sold × price per unit
    Aggregates all transactions for each unique product.
    
    Parameters:
        sales_data (list): List of sales records (dictionaries)
        
    Returns:
        dict: Dictionary with product IDs as keys and total sales as values
    """
    product_totals = {}
    
    for record in sales_data:
        product_id = record['prodID']
        units = int(record['units'])
        price = float(record['price'])
        total = units * price
        
        if product_id in product_totals:
            product_totals[product_id] += total
        else:
            product_totals[product_id] = total
    
    return product_totals


def calculate_customer_totals(sales_data):
    """
    Calculate total sales for each customer.
    Total sales = units sold × price per unit
    Aggregates all transactions for each unique customer.
    
    Parameters:
        sales_data (list): List of sales records (dictionaries)
        
    Returns:
        dict: Dictionary with customer IDs as keys and total sales as values
    """
    customer_totals = {}
    
    for record in sales_data:
        customer_id = record['custID']
        units = int(record['units'])
        price = float(record['price'])
        total = units * price
        
        if customer_id in customer_totals:
            customer_totals[customer_id] += total
        else:
            customer_totals[customer_id] = total
    
    return customer_totals


def write_product_sales_csv(product_totals, output_file):
    """
    Write product sales data to CSV file with headers.
    Format: Product ID, Total Sales (with $ sign)
    Data is sorted by product ID for consistency.
    
    Parameters:
        product_totals (dict): Dictionary of product totals
        output_file (str): Name of output CSV file
    """
    file = open(output_file, 'w', newline='')
    writer = csv.writer(file)
    
    # Write header row
    writer.writerow(['Product ID', 'Total Sales'])
    
    # Write data rows sorted by product ID
    for product_id in sorted(product_totals.keys()):
        total = product_totals[product_id]
        writer.writerow([product_id, f'${total:.2f}'])
    
    file.close()
    print(f"   Product sales data written to {output_file}")


def write_customer_sales_csv(customer_totals, output_file):
    """
    Write customer sales data to CSV file with headers.
    Format: Customer ID, Total Sales (with $ sign)
    Data is sorted by customer ID for consistency.
    
    Parameters:
        customer_totals (dict): Dictionary of customer totals
        output_file (str): Name of output CSV file
    """
    file = open(output_file, 'w', newline='')
    writer = csv.writer(file)
    
    # Write header row
    writer.writerow(['Customer ID', 'Total Sales'])
    
    # Write data rows sorted by customer ID
    for customer_id in sorted(customer_totals.keys()):
        total = customer_totals[customer_id]
        writer.writerow([customer_id, f'${total:.2f}'])
    
    file.close()
    print(f"   Customer sales data written to {output_file}")


def write_customer_sales_txt(customer_totals, output_file):
    """
    Write customer sales data to formatted text file.
    Includes headers, proper alignment, and dollar signs.
    Creates professional-looking report with borders and spacing.
    
    Parameters:
        customer_totals (dict): Dictionary of customer totals
        output_file (str): Name of output text file
    """
    file = open(output_file, 'w')
    
    # Write header section
    file.write("=" * REPORT_WIDTH + "\n")
    file.write("CUSTOMER SALES REPORT".center(REPORT_WIDTH) + "\n")
    file.write("=" * REPORT_WIDTH + "\n\n")
    
    # Write column headers
    file.write(f"{'Customer ID':<{COLUMN_WIDTH}} {'Total Sales':>{COLUMN_WIDTH}}\n")
    file.write("-" * REPORT_WIDTH + "\n")
    
    # Write data rows sorted by customer ID
    for customer_id in sorted(customer_totals.keys()):
        total = customer_totals[customer_id]
        file.write(f"{customer_id:<{COLUMN_WIDTH}} ${total:>{COLUMN_WIDTH-1}.2f}\n")
    
    # Write footer
    file.write("=" * REPORT_WIDTH + "\n")
    file.close()
    print(f"   Customer sales data written to {output_file}")


def display_product_totals(product_totals):
    """
    Display product sales in tabular format with proper alignment.
    Shows Product ID and Total Sales with dollar signs.
    Creates formatted console output with borders and headers.
    
    Parameters:
        product_totals (dict): Dictionary of product totals
    """
    print("\n" + "=" * REPORT_WIDTH)
    print("PRODUCT SALES REPORT".center(REPORT_WIDTH))
    print("=" * REPORT_WIDTH)
    print(f"{'Product ID':<{COLUMN_WIDTH}} {'Total Sales':>{COLUMN_WIDTH}}")
    print("-" * REPORT_WIDTH)
    
    for product_id in sorted(product_totals.keys()):
        total = product_totals[product_id]
        print(f"{product_id:<{COLUMN_WIDTH}} ${total:>{COLUMN_WIDTH-1}.2f}")
    
    print("=" * REPORT_WIDTH)


def display_customer_totals(customer_totals):
    """
    Display customer sales in tabular format with proper alignment.
    Shows Customer ID and Total Sales with dollar signs.
    Creates formatted console output with borders and headers.
    
    Parameters:
        customer_totals (dict): Dictionary of customer totals
    """
    print("\n" + "=" * REPORT_WIDTH)
    print("CUSTOMER SALES REPORT".center(REPORT_WIDTH))
    print("=" * REPORT_WIDTH)
    print(f"{'Customer ID':<{COLUMN_WIDTH}} {'Total Sales':>{COLUMN_WIDTH}}")
    print("-" * REPORT_WIDTH)
    
    for customer_id in sorted(customer_totals.keys()):
        total = customer_totals[customer_id]
        print(f"{customer_id:<{COLUMN_WIDTH}} ${total:>{COLUMN_WIDTH-1}.2f}")
    
    print("=" * REPORT_WIDTH)


def calculate_product_sales(input_file, output_file):
    """
    Main function for Part 1: Calculate and save product sales.
    Reads data, calculates totals, displays report, and writes to CSV.
    Orchestrates the complete product sales analysis workflow.
    
    Parameters:
        input_file (str): Input CSV filename
        output_file (str): Output CSV filename
    """
    sales_data = read_sales_data(input_file)
    
    if len(sales_data) > 0:
        product_totals = calculate_product_totals(sales_data)
        display_product_totals(product_totals)
        write_product_sales_csv(product_totals, output_file)
    else:
        print("   Unable to process sales data. Please check the input file.")


def calculate_customer_sales(input_file, csv_output, txt_output):
    """
    Main function for Part 2: Calculate and save customer sales.
    Reads data, calculates totals, displays report, and writes to CSV and TXT files.
    Orchestrates the complete customer sales analysis workflow.
    
    Parameters:
        input_file (str): Input CSV filename
        csv_output (str): Output CSV filename
        txt_output (str): Output text filename
    """
    sales_data = read_sales_data(input_file)
    
    if len(sales_data) > 0:
        customer_totals = calculate_customer_totals(sales_data)
        display_customer_totals(customer_totals)
        write_customer_sales_csv(customer_totals, csv_output)
        write_customer_sales_txt(customer_totals, txt_output)
    else:
        print("   Unable to process sales data. Please check the input file.")


def lookup_product_sales(product_file):
    """
    Look up sales for a specific product by Product ID.
    Searches the generated product sales CSV file and displays results.
    Prompts user for product ID and shows matching record if found.
    
    Parameters:
        product_file (str): CSV file containing product sales data
    """
    product_id = input("\nEnter Product ID to lookup: ").strip()
    
    file = open(product_file, 'r')
    reader = csv.DictReader(file)
    found = False
    found_row = None
    
    for row in reader:
        if row['Product ID'] == product_id:
            found = True
            found_row = row
    
    file.close()
    
    if found:
        print("\n" + "=" * REPORT_WIDTH)
        print("PRODUCT SALES FOUND".center(REPORT_WIDTH))
        print("=" * REPORT_WIDTH)
        print(f"   Product ID: {found_row['Product ID']}")
        print(f"   Total Sales: {found_row['Total Sales']}")
        print("=" * REPORT_WIDTH)
    else:
        print("\n" + "=" * REPORT_WIDTH)
        print(f"   Product ID '{product_id}' not found in the system.")
        print("=" * REPORT_WIDTH)


def lookup_customer_sales(customer_file):
    """
    Look up sales for a specific customer by Customer ID.
    Searches the generated customer sales CSV file and displays results.
    Prompts user for customer ID and shows matching record if found.
    
    Parameters:
        customer_file (str): CSV file containing customer sales data
    """
    customer_id = input("\nEnter Customer ID to lookup: ").strip()
    
    file = open(customer_file, 'r')
    reader = csv.DictReader(file)
    found = False
    found_row = None
    
    for row in reader:
        if row['Customer ID'] == customer_id:
            found = True
            found_row = row
    
    file.close()
    
    if found:
        print("\n" + "=" * REPORT_WIDTH)
        print("CUSTOMER SALES FOUND".center(REPORT_WIDTH))
        print("=" * REPORT_WIDTH)
        print(f"   Customer ID: {found_row['Customer ID']}")
        print(f"   Total Sales: {found_row['Total Sales']}")
        print("=" * REPORT_WIDTH)
    else:
        print("\n" + "=" * REPORT_WIDTH)
        print(f"   Customer ID '{customer_id}' not found in the system.")
        print("=" * REPORT_WIDTH)