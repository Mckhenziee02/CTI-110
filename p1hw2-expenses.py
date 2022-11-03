#CT1 110
#P1HW2 - Expenses
#JacksonM
#11/3

#input: three expenses, the budget
#processing:total the expenses, compare with budget
#output:did you go over or under
def main():
    #our variables - type float, because of the decimal place
    gas = 0.0
    food = 0.0
    hotel = 0.0
    totalExpenses = 0.0 # gas + food + hotel
    budget = 0.0
    destination = ""
    print("This program calculates on displays travel expenses")
    print("Enter your budget ")
    budget = float(input())
    destination = input("Where are you heading? ")

    print("OK, lets total your expenses.")

    gas = float(input("Gas: $") )
    hotel = float(input("Hotel: $") )
    food = float(input("Food: $") )

    #add everything up
    totalExpenses = gas + hotel + food
    #output - did they go over the budget?
    print("Your total expenses are:  $", totalExpenses)
    print("Your budget was:  $", budget)

    if  totalExpenses > budget :
           print ("You went over budget!")
           print("by: $", budget - totalExpenses)
    else:
          print("You stayed within your budget.")
          print("money left: $", budget - totalExpenses)

    goagin =input("Run again? y/n")
    if goagin == "y":
        main( )
    else:
        print("goodbye.")

#start the program
main( )

