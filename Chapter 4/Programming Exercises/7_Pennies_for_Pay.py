'''
7. Pennies for Pay
Write a program that calculates the amount of money a person would earn over a period of time if his or her salary is one penny the first day, two pennies the second day, and continues to double each day. The program should ask the user for the number of days. Display a table showing what the salary was for each day, then show the total pay at the end of the 
period. The output should be displayed in a dollar amount, not the number of pennies. 
'''

days = int(input('Enter the number of days: '))
penny = 0.01
total = 0

print(' DAY \t SALARY(in Dollars) \n ------------------------')
for i in range(1,days+1):
    print(f' {i} \t\t ${penny}')
    
    total += penny
    penny *= 2
print('-------------------------')
print('Total Pay after {} days is: ${:,.2f}'.format(days,total))