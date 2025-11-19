# Movie Sales Analysis Utilities
# 03Nov25
# CSC-121 M5Pro
# Alexander Allen

"""
Module containing utility functions for movie sales analysis.
Handles file reading, revenue calculations, movie classification,
and report generation.
"""

import csv


def read_movie_data(filename):
    """
    Read movie data from CSV file.
    
    Args:
        filename: Path to CSV file containing movie sales data
        
    Returns:
        tuple: (movie_names, tickets_sold, ticket_prices) as lists
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        ValueError: If data format is invalid
        KeyError: If required columns are missing
    """
    movie_names = []
    tickets_sold = []
    ticket_prices = []
    
    try:
        file = open(filename, 'r')
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: The file '{filename}' was not found.")
    
    csv_reader = csv.DictReader(file)
    
    try:
        for row in csv_reader:
            try:
                movie_names.append(row['Movie'])
                tickets_sold.append(int(row['TicketsSold']))
                ticket_prices.append(float(row['TicketPrice']))
            except KeyError as e:
                file.close()
                raise KeyError(f"Missing required column in CSV: {e}")
            except ValueError as e:
                file.close()
                raise ValueError(f"Invalid data format in CSV: {e}")
    finally:
        file.close()
    
    return movie_names, tickets_sold, ticket_prices


def calculate_revenue(tickets_sold, ticket_price):
    """
    Calculate total revenue for a movie.
    
    Args:
        tickets_sold: Number of tickets sold
        ticket_price: Price per ticket
        
    Returns:
        float: Total revenue
    """
    return tickets_sold * ticket_price


def classify_movie(revenue):
    """
    Classify movie based on revenue.
    
    Args:
        revenue: Total revenue amount
        
    Returns:
        str: Movie rating classification
    """
    if revenue >= 3000:
        return "Blockbuster"
    elif revenue >= 2000:
        return "Moderate Hit"
    else:
        return "Low Performer"


def display_revenue_report(movie_names, revenues):
    """
    Display movie names and their revenues on screen.
    
    Args:
        movie_names: List of movie titles
        revenues: List of revenue amounts
    """
    print("\n" + "=" * 70)
    print("MOVIE REVENUE REPORT".center(70))
    print("=" * 70)
    print(f"{'Movie Title':<40} {'Revenue':<20}")
    print("-" * 70)
    
    for i in range(len(movie_names)):
        print(f"{movie_names[i]:<40} ${revenues[i]:>18,.2f}")
    
    print("=" * 70)
    print(f"{'Total Revenue:':<40} ${sum(revenues):>18,.2f}")
    print("=" * 70)


def get_revenue_for_sorting(item):
    """
    Helper function to extract revenue from tuple for sorting.
    
    Args:
        item: Tuple containing (revenue, name, tickets, price, rating)
        
    Returns:
        float: Revenue value (first element of tuple)
    """
    return item[0]


def sort_data_by_revenue(movie_names, tickets_sold, ticket_prices, revenues, ratings):
    """
    Sort all data by revenue in descending order.
    
    Args:
        movie_names: List of movie titles
        tickets_sold: List of tickets sold
        ticket_prices: List of ticket prices
        revenues: List of revenues
        ratings: List of movie ratings
        
    Returns:
        tuple: Sorted lists (movies, tickets, prices, revenues, ratings)
    """
    # Create list of tuples for sorting
    combined = []
    for i in range(len(movie_names)):
        combined.append((revenues[i], movie_names[i], tickets_sold[i], 
                        ticket_prices[i], ratings[i]))
    
    # Sort by revenue (first element) in descending order using helper function
    combined.sort(reverse=True, key=get_revenue_for_sorting)
    
    # Unzip the sorted data manually
    sorted_revenues = []
    sorted_movies = []
    sorted_tickets = []
    sorted_prices = []
    sorted_ratings = []
    
    for item in combined:
        sorted_revenues.append(item[0])
        sorted_movies.append(item[1])
        sorted_tickets.append(item[2])
        sorted_prices.append(item[3])
        sorted_ratings.append(item[4])
    
    return (sorted_movies, sorted_tickets, sorted_prices, 
            sorted_revenues, sorted_ratings)


def write_csv_report(filename, movie_names, tickets_sold, ticket_prices, revenues, ratings):
    """
    Write updated movie sales report to CSV file.
    
    Args:
        filename: Output CSV filename
        movie_names: List of movie titles
        tickets_sold: List of tickets sold
        ticket_prices: List of ticket prices
        revenues: List of revenues
        ratings: List of movie ratings
    
    Raises:
        IOError: If unable to write to file
    """
    try:
        file = open(filename, 'w', newline='')
        writer = csv.writer(file)
        
        # Write header
        writer.writerow(['Movie', 'TicketsSold', 'TicketPrice', 'Revenue', 'Rating'])
        
        # Write data rows with formatting
        for i in range(len(movie_names)):
            writer.writerow([
                movie_names[i],
                f"{tickets_sold[i]:,}",
                f"${ticket_prices[i]:,.2f}",
                f"${revenues[i]:,.2f}",
                ratings[i]
            ])
        
        file.close()
        print(f"\n✓ CSV file '{filename}' created successfully!")
        
    except IOError as e:
        raise IOError(f"Error writing CSV file: {e}")


def write_txt_report(filename, movie_names, tickets_sold, ticket_prices, revenues, ratings):
    """
    Write updated movie sales report to text file in tabular format.
    
    Args:
        filename: Output text filename
        movie_names: List of movie titles
        tickets_sold: List of tickets sold
        ticket_prices: List of ticket prices
        revenues: List of revenues
        ratings: List of movie ratings
    
    Raises:
        IOError: If unable to write to file
    """
    try:
        file = open(filename, 'w')
        
        # Write header
        file.write("=" * 100 + "\n")
        file.write("MOVIE SALES REPORT WITH RATINGS\n")
        file.write("=" * 100 + "\n")
        
        # Column headers
        file.write(f"{'Movie':<30} {'Tickets Sold':<15} {'Ticket Price':<15} "
                  f"{'Revenue':<15} {'Rating':<20}\n")
        file.write("-" * 100 + "\n")
        
        # Data rows
        for i in range(len(movie_names)):
            file.write(f"{movie_names[i]:<30} "
                      f"{tickets_sold[i]:>13,}  "
                      f"${ticket_prices[i]:>12,.2f}  "
                      f"${revenues[i]:>12,.2f}  "
                      f"{ratings[i]:<20}\n")
        
        file.write("=" * 100 + "\n")
        file.write(f"{'TOTAL REVENUE:':<60} ${sum(revenues):>12,.2f}\n")
        file.write("=" * 100 + "\n")
        
        file.close()
        print(f"✓ Text file '{filename}' created successfully!")
        
    except IOError as e:
        raise IOError(f"Error writing text file: {e}")
