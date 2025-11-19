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
#Import Functions for the store
import m2Lab_Function_Store_AlexanderAllen as store

#Choices for the menu in display()
calc = 1
Quit = 2

# The main function
def main():
    
    choice = 0
    
    while choice != Quit:
        
        #display menu
        store.display()
        #get user choice
        print()
        choice = int(input("Enter a choice: "))
        # Preform inputed action
        if choice == calc:
            count = store.calcCost()
            #items, grossCost, discount, tax, afterTax, netCost = calcCost()
            items, grossCost, discount, tax, afterTax, netCost = count
            store.displayLine(items, grossCost, discount, tax, afterTax, netCost)
        elif choice == Quit:
            print("Exiting the program.......")
        else:
            print("Error: invalid entry")

if __name__ =="__main__":
    main()