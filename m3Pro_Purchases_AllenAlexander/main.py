# Box Office Report Generator
# 29Sep25
# CSC-121 m3Pro - movie_tickets
# Alexander Allen

'''
For this assignment, you are to create a program that helps generate
box office reports showing total earnings per movie. More details given below

Create a program that uses 3 lists:
    
movie_titles: movie names ( a minimum of 5 movie names)

tickets_sold: number of tickets sold per movie ( number here don't need to be accurate )
                                                
ticket_prices: ticket price per movie ( you could add random ticket price
               or lookup accurate prices in movie theaters next to you ) 

                                               
'''

import box_office_utils as bou

# List of movie titles
movie_titles = [
    "Space Marines 2",
    "Silent Hill f",
    "Knives Out",
    "Flipper",
    "Journey to the Center of the Earth",
    "Digimon",
    "Race to Witch Mountain"
]

# Number of tickets sold per movie
tickets_sold = [1250, 890, 2100, 1575, 945, 1820, 1340]

# Ticket price per movie (in dollars)
ticket_prices = [12.50, 10.00, 15.00, 13.50, 11.00, 14.00, 12.00]


def display_menu():
    """
    Display the main menu options for the box office report system.

    """
    print("\n" + "=" * 60)
    print("BOX OFFICE REPORT SYSTEM".center(60))
    print("=" * 60)
    print("1. Display Box Office Report")
    print("2. Show Top-Earning Movie")
    print("3. Show Average Revenue")
    print("4. Display Report (Sorted by Revenue)")
    print("5. Exit")
    print("=" * 60)


def main():
    """
    Main function to run the box office report system.
    Provides menu-driven interface for various reporting options.
    Calculates total revenue per movie and displays reports based on user selection.

    """
    # Calculate total revenue for each movie
    total_revenues = []
    for i in range(len(movie_titles)):
        revenue = bou.cal_total_rev(tickets_sold[i], ticket_prices[i])
        total_revenues.append(revenue)
    
    choice = '0'
    while choice != '5':
        display_menu()
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            # Display standard report
            bou.display_report(movie_titles, tickets_sold, ticket_prices, total_revenues)
            
            # Display summary statistics
            print(f"\nTotal Movies: {len(movie_titles)}")
            print(f"Total Tickets Sold: {sum(tickets_sold):,}")
            print(f"Average Ticket Price: ${sum(ticket_prices) / len(ticket_prices):.2f}")
            print(f"TOTAL BOX OFFICE REVENUE: ${sum(total_revenues):,.2f}")
            print("=" * 90)
        
        elif choice == '2':
            # Show top-earning movie
            top_movie, top_revenue = bou.find_top_movie(movie_titles, total_revenues)
            print("\n" + "=" * 60)
            print("   TOP PERFORMING MOVIE".center(60))
            print("=" * 60)
            print(f"   Movie: {top_movie}")
            print(f"   Earnings: ${top_revenue:,.2f}")
            print("=" * 60)
        
        elif choice == '3':
            # Show average revenue
            avg_revenue = bou.calculate_average_revenue(total_revenues)
            print("\n" + "=" * 60)
            print("AVERAGE REVENUE STATISTICS".center(60))
            print("=" * 60)
            print(f"Average Revenue Across All Movies: ${avg_revenue:,.2f}")
            print("=" * 60)
        
        elif choice == '4':
            # Display report sorted by revenue
            sorted_movies, sorted_tickets, sorted_prices, sorted_revenues = \
                bou.sort_by_revenue(movie_titles, tickets_sold, ticket_prices, total_revenues)
            print("\n   MOVIES SORTED BY REVENUE (HIGHEST TO LOWEST)")
            bou.display_report(sorted_movies, sorted_tickets, sorted_prices, sorted_revenues)
        
        elif choice == '5':
            # Exit program
            print("\n" + "=" * 60)
            print("Thank you for using Box Office Report System!".center(60))
            print("Goodbye!".center(60))
            print("=" * 60)
            
        
        else:
            print("\n   Invalid choice! Please enter a number between 1 and 5.")


# Run the program
if __name__ == "__main__":
    main()