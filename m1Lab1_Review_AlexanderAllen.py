# Creation of the Dollar Store using loops
# 27Aug2025
# CSC121 m1Lab1– Review
# Alexander Allen

"""
A store sells all items for $1. Customers buying 10 or more items receive a 5% discount.
Additionally, there is 7.5% sales tax.

Write a program that prompts the user for the number of items purchased and calculates
the total cost before and after tax.
Here is an example run:

Enter number of items: 11
Gross cost: 11.0
Discount:   0.55
Net cost:   10.45
Tax:        0.78
After tax:  11.23
"""

#Get input form user
items = float(input("Enter the number of items to buy or 0 to exit: "))

#Establish loop for dollar store
while items != 0:
    
    #If user inputs a negative number have them try again
    while items < 0:
        print("Invalid number try again!!")
        items = float(input("Enter a positive number of items to buy or 0 to exit: "))
        
    #If user inputs 0 end progam
    if items == 0:
        print("Thanks for shopping please come agian!")
        
    #Find Gross cost
    grossCost = items * 1
    
    #Apply discount
    if items >= 10:
        discount = grossCost * 0.05
    #No discount    
    if items < 10 > 0:
        discount = 0
    #Apply variables to aquire net cost, gross cost, tax, and after tax    
    netCost = grossCost - discount
    tax = netCost * 0.075
    afterTax = netCost + tax
    
    if grossCost != 0:
        #Display Variables
        print("Gross cost: $", grossCost, sep ='')
        print("Discount: $", discount, sep = '')
        print("Net cost: $", netCost, sep = '')
        print(f"Tax: ${tax:.2f}")
        print(f"After tax: ${afterTax:.2f}")
        
        #Aquire user input if program is required again
        items = float(input("Enter the number of items to buy or 0 to exit: "))
    
    
         
    
    
