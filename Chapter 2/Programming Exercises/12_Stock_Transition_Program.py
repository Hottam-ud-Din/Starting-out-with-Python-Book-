'''
12.Stock Transaction Program
Last month, Joe purchased some stock in Acme Software, Inc. Here are the details of the 
purchase:
1. The number of shares that Joe purchased was 2,000.
2. When Joe purchased the stock, he paid $40.00 per share.
3. Joe paid his stockbroker a commission that amounted to 3 percent of the amount he paid 
for the stock.

Two weeks later, Joe sold the stock. Here are the details of the sale:
1. The number of shares that Joe sold was 2,000.
2. He sold the stock for $42.75 per share.
3. He paid his stockbroker another commission that amounted to 3 percent of the amount he received for the stock.

Write a program that displays the following information:
1. The amount of money Joe paid for the stock.
2. The amount of commission Joe paid his broker when he bought the stock.
3. The amount for which Joe sold the stock.
4. The amount of commission Joe paid his broker when he sold the stock.
5. Display the amount of money that Joe had left when he sold the stock and paid his broker (both times). If this amount is positive, then Joe made a profit. If the amount is negative, then Joe lost money.
'''

# Details of the purchased stock
shares          = 2000
purchase_price  = 40
purchase_amount = shares * purchase_price
commission_rate = 0.03
brokr_com_befor = purchase_amount * commission_rate

# Details of the stock sold

sold_price      = 42.75
sold_amount     = sold_price * shares
brokr_com_after = sold_amount * commission_rate

amount_left     = sold_amount - (brokr_com_after + brokr_com_befor + purchase_amount) 

print(f'The amount of money Joe paid for the stock was: ${purchase_amount}')
print(f'The amount of commission Joe paid his broker when he bought the stock was: ${brokr_com_befor}')
print(f'The amount for which Joe sold the stock is: ${sold_amount}')
print(f'The amount of commission Joe paid his broker when he sold the stock is: ${brokr_com_after}')
print(f'So the amount of money that Joe had left when he sold the stock and paid his broker (both times) is: ${amount_left}')
print(f"So this is a positive number and Joe has made a profit of ${amount_left}")
