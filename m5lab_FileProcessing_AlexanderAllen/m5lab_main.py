# Sales Data Processing System
# 29Oct25
# CSC121 M5Lab
# Alexander Allen

'''
This program processes sales data from a CSV file and generates various reports.
It provides a menu-driven interface to:
- Calculate total sales by product
- Calculate total sales by customer
- Lookup specific product or customer sales data
- Export data to CSV and text files
'''

import sales_functions as sf


def display_menu():
    """
    Display the main menu options for the sales data processing system.
    
    """
    print("\n" + "=" * 70)
    print("SALES DATA PROCESSING SYSTEM".center(70))
    print("=" * 70)
    print("1) Read file and Calculate Total Sales (write to csv file)")
    print("2) Calculate Sales Per Customer and Write to 'cus_total' txt file")
    print("3) Lookup Product Sales")
    print("4) Lookup Total Sales for Customer")
    print("5) Exit")
    print("=" * 70)


def main():
    """
    Main function to run the sales processing program.
    Provides menu-driven interface for various sales reporting options.
    Processes sales data and generates reports based on user selection.
    
    """
    choice = '0'
    while choice != '5':
        display_menu()
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            # Part 1: Calculate and display product sales
            print("\n" + "=" * 70)
            print("PROCESSING TOTAL SALES BY PRODUCT".center(70))
            print("=" * 70)
            sf.calculate_product_sales('sales.csv', 'total_sales.csv')
            
        elif choice == '2':
            # Part 2: Calculate and display customer sales
            print("\n" + "=" * 70)
            print("PROCESSING SALES BY CUSTOMER".center(70))
            print("=" * 70)
            sf.calculate_customer_sales('sales.csv', 'cus_total.csv', 'cus_total_txt.txt')
            
        elif choice == '3':
            # Part 3: Lookup specific product sales
            print("\n" + "=" * 70)
            print("PRODUCT SALES LOOKUP".center(70))
            print("=" * 70)
            print("Calculating total sales data...")
            sf.calculate_product_sales('sales.csv', 'total_sales.csv')
            sf.lookup_product_sales('total_sales.csv')
            
        elif choice == '4':
            # Part 4: Lookup specific customer sales
            print("\n" + "=" * 70)
            print("CUSTOMER SALES LOOKUP".center(70))
            print("=" * 70)
            print("Calculating customer sales data...")
            sf.calculate_customer_sales('sales.csv', 'cus_total.csv', 'cus_total_txt.txt')
            sf.lookup_customer_sales('cus_total.csv')
            
        elif choice == '5':
            # Exit program
            print("\n" + "=" * 70)
            print("Thank you for using Sales Data Processing System!".center(70))
            print("Goodbye!".center(70))
            print("=" * 70)
            
        else:
            print("\n   Invalid choice! Please enter a number between 1 and 5.")


# Run the program
if __name__ == "__main__":
    main()
