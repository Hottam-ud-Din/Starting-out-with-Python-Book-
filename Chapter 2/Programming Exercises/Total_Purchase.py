'''
4. Total Purchase
A customer in a store is purchasing five items. Write a program that asks for the price of 
each item, then displays the subtotal of the sale, the amount of sales tax, and the total. 
Assume the sales tax is 7 percent.
'''

subtotal = 0
for i in range(1,6):
    price = float(input(f"Enter the price of item {i}:"))
    subtotal += price
    
tax_rate = 0.07
sales_tax = subtotal * tax_rate
total = subtotal + sales_tax

print(f'The subtotal is ${subtotal:.2f}')
print(f"The Tax is ${sales_tax:.2f}")
print(f"The Toatl amount is ${total:.2f}")