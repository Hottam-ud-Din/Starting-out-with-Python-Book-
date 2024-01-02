'''
### 6. Payment Instalments
Write a program that asks the user to enter the amount of a purchase and the desired 
number of payment instalments. The program should add 5 percent to the amount to get 
the total purchase amount, and then divide it by the desired number of instalments, then display messages telling the user the total amount of the purchase and how much each 
instalment will cost.
'''

amount_of_purchase   = int(input("Enter the amount of purchase:"))
instalments          = int(input("Enter your desired number of payment instalments:"))

total_purchae_amount = amount_of_purchase + (amount_of_purchase*0.05)
each_instalment      = total_purchae_amount/instalments

print(f'The total purchase amount is: {total_purchae_amount}')
print(f'The amount 0f each instalment will be: {each_instalment}')
