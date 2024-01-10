'''
10. Money Counting Game
Create a change-counting game that gets the user to enter the number of coins required 
to make exactly one dollar. The program should prompt the user to enter the number of 
pennies, nickels, dimes, and quarters. If the total value of the coins entered is equal to one 
dollar, the program should congratulate the user for winning the game. Otherwise, the 
program should display a message indicating whether the amount entered was more than 
or less than one dollar.
'''

pennies = int(input("Enter the number of pennies: ")) 
nickels = int(input("Enter the number of nickels: "))
dimes = int(input("Enter the number of dimes: "))
quarters = int(input("Enter the number of quarters: "))

total_value = pennies + (nickels * 5) + (dimes * 10) + (quarters * 25)

if total_value == 100:
    print(f'Total: {total_value}')
    print("Congratulations! You won the game!")
elif total_value > 100:
    print(f'Total: {total_value}')
    print("Sorry, the amount entered was greater than one dollar.")
else:
    print(f'Total: {total_value}')
    print("Sorry, the amount entered was more than one dollar.")
