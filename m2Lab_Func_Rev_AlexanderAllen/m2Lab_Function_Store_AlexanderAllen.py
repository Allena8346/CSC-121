# Creation of the Dollar Store using functions and be menu driven
# 11Sep2025
# CSC121 m2Lab– Review
# Alexander Allen

"""
A store sells all items for $1. Customers buying 10 or more items receive a 5% discount.
Additionally, there is 7.5% sales tax.
Write a program that prompts the user for the number of items purchased, and 
calculates the total cost before and after tax. Here is an example session:

Enter number of items: 10
Net Cost:    9.50
Tax:         0.71
After tax:  10.21

def functions:
    
calcCost(count)
displayLine(label, amount)
display(cost, tax)

"""
def calcCost():
    #Get input form user
    items = float(input("Enter the number of items to buy or 0 to exit: "))
    #Establish loop for dollar store
    while items != 0:
        
        #If user inputs a negative number have them try again
        while items < 0:
            print("Invalid number try again!!")
            print()
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
        #return variables to main for use and distrobution
        return items, grossCost, discount, tax, afterTax, netCost

#Function to display results of calcCost()
def displayLine(items, grossCost, discount, tax, afterTax, netCost):
    print(f"Net Cost: {netCost:>6}")
    print(f"Tax: {tax:>6.2f}")
    print(f"After tax: {afterTax:>6.2f}")

#Function to display menu options
def display():
    print()
    print("Menu")
    print('1) Enter a Number')
    print('2) Exit')
    
    
    
    
    
    
    
    
if __name__ =="__main__":
    display()