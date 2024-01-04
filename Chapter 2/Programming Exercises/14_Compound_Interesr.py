'''
14.Compound Interest
When a bank account pays compound interest, it pays interest not only on the principal 
amount that was deposited into the account, but also on the interest that has accumulated 
over time. Suppose you want to deposit some money into a savings account, and let the 
account earn compound interest for a certain number of years. The formula for calculating 
the balance of the account after a specified number of years is:

                            A = P * ((1 + r/n)**nt)
                            
The terms in the formula are:
1. A is the amount of money in the account after the specified number of years.
2. P is the principal amount that was originally deposited into the account.
3. r is the annual interest rate.
4. n is the number of times per year that the interest is compounded.
5. t is the specified number of years.

Write a program that makes the calculation for you. The program should ask the user to input the following:
1. The amount of principal originally deposited into the account
2. The annual interest rate paid by the account
3. The number of times per year that the interest is compounded (For example, if interest is compounded monthly, enter 12   If interest is compounded quarterly, enter 4.)
4. The number of years the account will be left to earn interest

Once the input data has been entered, the program should calculate and display the amount 
of money that will be in the account after the specified number of years.
NOTE:
The user should enter the interest rate as a percentage. For example, 2 percent 
would be entered as 2, not as .02. The program will then have to divide the input by 
100 to move the decimal point to the correct position.
'''

principal_amount        = int(input("Enter the amount that was originally deposited into the account:"))
annual_interest_rate    = int(input("Enter the amount of annual interest rate(in percentage) paid by the account:"))
interest_compound_times = int(input("Enter the number of times per year the interest is compounded:"))
number_of_years         = int(input("Enter the specified number of yrears:"))

annual_interest_rate   /= 100

amount_left_after_years = principal_amount * ((1+annual_interest_rate/interest_compound_times) ** (interest_compound_times*number_of_years))
print(f'The amount of money that will be left after {number_of_years}-years is: {amount_left_after_years:.2f}')