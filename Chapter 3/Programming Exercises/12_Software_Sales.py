'''
12. Software Sales
A software company sells a package that retails for $99. Quantity discounts are given 
according to the following table:

                       Quantity         Discount
                       10-19              10%
                       20-49              20%
                       50-99              30%
                       100 or more        40%
Write a program that asks the user to enter the number of packages purchased. The program should then display the amount of the discount (if any) and the total amount of the purchase after the discount.
'''

packages_purchased = int(input('Enter the number of packages you have purchased: '))
price_of_package   = 99

if packages_purchased >= 10 and packages_purchased <= 19:
    discount = 0.10  #10%
    
elif packages_purchased >= 20 and packages_purchased <= 49:
    discount = 0.20  #20%
    
elif packages_purchased >= 50 and packages_purchased <= 99:
    discount = 0.30  #30%
    
elif packages_purchased >= 100:
    discount = 0.40  #40%
    
else:
    discount = 0
    
amount   = price_of_package * packages_purchased
discount_amount = amount * discount
total_amount = amount - discount_amount

print(f'Amount is: {amount}')
print(f'Discount is: {discount_amount:,.2f}')
print(f'Total Amount after discount is: {total_amount:,.2f}')