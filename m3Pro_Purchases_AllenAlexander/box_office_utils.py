# Box Office Report Generator
# 29Sep25
# CSC-121 m3Pro - movie_tickets
# Alexander Allen
"""
Module containing utility functions for box office report generation.

"""


def cal_total_rev(tickets_sold, ticket_price):
    """
    Calculate total revenue for a movie.

    """
    return tickets_sold * ticket_price


def display_report(movie_name_list, tickets_sold_list, ticket_price_list, total_revenue_list):
    """
    Display box office report in tabular format with proper formatting.
    Displays movie title, tickets sold, price, and revenue.

    """
    print("\n" + "=" * 90)
    print("BOX OFFICE REPORT".center(90))
    print("=" * 90)
    
    # Table header
    print(f"{'Movie Title':<40} {'Tickets':<15} {'Price':<15} {'Revenue':<15}")
    print("-" * 90)
    
    # Table rows
    for i in range(len(movie_name_list)):
        print(f"{movie_name_list[i]:<40} {tickets_sold_list[i]:<15,} "
              f"${ticket_price_list[i]:<14,.2f} ${total_revenue_list[i]:<14,.2f}")
    
    print("=" * 90)


def find_top_movie(movie_name_list, total_revenue_list):
    """
    Find and return the top-earning movie.
  
    """
    max_index = total_revenue_list.index(max(total_revenue_list))
    return movie_name_list[max_index], total_revenue_list[max_index]


def calculate_average_revenue(total_revenue_list):
    """
    Calculate average revenue across all movies.

    """
    return sum(total_revenue_list) / len(total_revenue_list)


def sort_by_revenue(movie_name_list, tickets_sold_list, ticket_price_list, total_revenue_list):
    """
    Sort all lists by revenue in descending order (highest to lowest).
   
    """
# Create empty lists for sorted data
    sorted_movies = []
    sorted_tickets = []
    sorted_prices = []
    sorted_revenues = []
    
    # Create a copy of revenue list to track which indices to use
    revenue_copy = total_revenue_list.copy()
    
    # Sort by finding the maximum revenue each time
    for i in range(len(total_revenue_list)):
        # Find the index of the maximum revenue in the remaining data
        max_revenue = max(revenue_copy)
        max_index = total_revenue_list.index(max_revenue)
        
        # Append the corresponding data from each list
        sorted_movies.append(movie_name_list[max_index])
        sorted_tickets.append(tickets_sold_list[max_index])
        sorted_prices.append(ticket_price_list[max_index])
        sorted_revenues.append(total_revenue_list[max_index])
        
        # Remove this revenue from the copy so we don't select it again
        revenue_copy.remove(max_revenue)
    
    return sorted_movies, sorted_tickets, sorted_prices, sorted_revenues