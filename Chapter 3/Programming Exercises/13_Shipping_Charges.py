'''
13. Shipping Charges
The Fast Freight Shipping Company charges the following rates:

            Weight of Package             Rate per Pound
              2 pound or less                   1.50
              over 2, not more than 6           3.00
              over 6, not more than 10          4.00
              over 10 pounds                    4.75
Write a program that asks the user to enter the weight of a package then displays the shipping charges              
'''
weight = int(input('Enter the weight of the Package: '))

if weight <= 2:
    rate_per_pound = 1.50
elif weight > 2 and weight <= 6:
    rate_per_pound = 3.00
elif weight > 6 and weight <= 10:
    rate_per_pound = 4.00
else:
    rate_per_pound = 4.75

shipping_charges = weight * rate_per_pound
print(f'The shipping charges for your Package are: {shipping_charges}')
    