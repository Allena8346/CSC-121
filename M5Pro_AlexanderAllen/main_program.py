# Movie Sales Analysis Program
# 03Nov25
# CSC-121 M5Pro
# Alexander Allen

"""
Main program for analyzing movie sales data from CSV file.
Provides menu-driven interface for:
1. Reading data and calculating revenue
2. Classifying movies and writing reports to files
3. Exit

Reads from: movie_sales-2.csv
Outputs: updated_movie_sales.csv and updated_movie_sales.txt
"""

import movie_utils as mau


def display_menu():
    """
    Display the main menu options for the movie sales analysis system.
    """
    print("\n" + "=" * 60)
    print("MOVIE SALES ANALYSIS SYSTEM".center(60))
    print("=" * 60)
    print("1) Read Data and Calculate Revenue (Display results)")
    print("2) Classify Movies and Write Ratings to Files (csv and txt)")
    print("3) Exit")
    print("=" * 60)


def option_one():
    """
    Option 1: Read movie data from CSV and display revenue report.
    Handles file reading and data conversion errors.
    """
    try:
        # Read data from CSV file
        movie_names, tickets_sold, ticket_prices = mau.read_movie_data('movie_sales-2.csv')
        
        # Calculate revenue for each movie
        revenues = []
        for i in range(len(movie_names)):
            revenue = mau.calculate_revenue(tickets_sold[i], ticket_prices[i])
            revenues.append(revenue)
        
        # Display the revenue report
        mau.display_revenue_report(movie_names, revenues)
        
    except FileNotFoundError as e:
        print(f"\n{e}")
        print("Please make sure 'movie_sales-2.csv' is in the same directory as this program.")
    except KeyError as e:
        print(f"\nData Error: {e}")
        print("Please check that the CSV file has the required columns.")
    except ValueError as e:
        print(f"\nData Error: {e}")
        print("Please check the CSV file format.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")


def option_two():
    """
    Option 2: Read data, calculate revenue, classify movies,
    and write reports to CSV and TXT files.
    Handles file operations and data conversion errors.
    """
    try:
        # Read data from CSV file
        movie_names, tickets_sold, ticket_prices = mau.read_movie_data('movie_sales-2.csv')
        
        # Calculate revenue for each movie
        revenues = []
        for i in range(len(movie_names)):
            revenue = mau.calculate_revenue(tickets_sold[i], ticket_prices[i])
            revenues.append(revenue)
        
        # Classify each movie based on revenue
        ratings = []
        for revenue in revenues:
            rating = mau.classify_movie(revenue)
            ratings.append(rating)
        
        # Sort all data by revenue (highest first)
        sorted_movies, sorted_tickets, sorted_prices, sorted_revenues, sorted_ratings = \
            mau.sort_data_by_revenue(movie_names, tickets_sold, ticket_prices, revenues, ratings)
        
        # Write CSV report
        mau.write_csv_report('updated_movie_sales.csv', sorted_movies, sorted_tickets, 
                            sorted_prices, sorted_revenues, sorted_ratings)
        
        # Write TXT report
        mau.write_txt_report('updated_movie_sales.txt', sorted_movies, sorted_tickets, 
                            sorted_prices, sorted_revenues, sorted_ratings)
        
        print("\n" + "=" * 60)
        print("Reports generated successfully!".center(60))
        print("=" * 60)
        
    except FileNotFoundError as e:
        print(f"\n{e}")
        print("Please make sure 'movie_sales-2.csv' is in the same directory as this program.")
    except KeyError as e:
        print(f"\nData Error: {e}")
        print("Please check that the CSV file has the required columns.")
    except ValueError as e:
        print(f"\nData Error: {e}")
        print("Please check the CSV file format.")
    except IOError as e:
        print(f"\nFile Writing Error: {e}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")


def main():
    """
    Main function to run the movie sales analysis system.
    Provides menu-driven interface with three options.
    Program continues until user chooses to exit (option 3).
    """
    choice = ''
    
    while choice != '3':
        display_menu()
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1':
            option_one()
            
        elif choice == '2':
            option_two()
            
        elif choice == '3':
            print("\n" + "=" * 60)
            print("Thank you for using Movie Sales Analysis System!".center(60))
            print("Goodbye!".center(60))
            print("=" * 60)
            
        else:
            print("\nInvalid choice! Please enter 1, 2, or 3.")


# Run the program
if __name__ == "__main__":
    main()
