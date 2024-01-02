'''
### 8. Tip, Tax, and Total
Write a program that calculates the total amount of a meal purchased at a restaurant. The 
program should ask the user to enter the charge for the food, then calculate the amounts 
of a 18 percent tip and 7 percent sales tax. Display each of these amounts and the total.
'''

food_charge   = float(input("Enter the charge for the food:"))
tip_amount    = food_charge * 0.18 # 18%
tax_amount    = food_charge * 0.07 # 7%
total_amount  = food_charge + tip_amount + tax_amount

print(f'The food charge was: {food_charge:,.2f}')
print(f'The tip amount of 18% is: {tip_amount:,.2f}')
print(f'The amount of 7% is: {tax_amount:,.2f}')
print(f'The total amount is: {total_amount:,.2f}')