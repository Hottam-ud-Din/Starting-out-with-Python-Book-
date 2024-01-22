'''
5. Average Rainfall
Write a program that uses nested loops to collect data and calculate the average rainfall over 
a period of years. The program should first ask for the number of years. The outer loop will 
iterate once for each year. The inner loop will iterate twelve times, once for each month. 
Each iteration of the inner loop will ask the user for the inches of rainfall for that month. 
After all iterations, the program should display the number of months, the total inches of 
rainfall, and the average rainfall per month for the entire period.
'''

total_years = int(input('Enter the number of years: '))

total_months = 0
total_rainfall = 0

for year in range(1,total_years+1):
    print(f'\n YEAR: {year} \n')
    for month in ('January','February','March','April','May','June','July','August',
                  'September','OCtuber','November','December'):
        rainfall = float(input(f'Enter the inches of rainfall for the month of {month}: '))
        total_months += 1
        total_rainfall += rainfall
        
average = total_rainfall / total_months
print('\n Number of Months:',total_months)
print(f'Total inches of rainfall : {total_rainfall:,.2f}')
print(f'Average inches of rainfall for each month : {average:,.2f}')
