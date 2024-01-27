'''
10. Tuition Increase
At one college, the tuition for a full-time student is $8,000 per semester. It has been announced 
that the tuition will increase by 3 percent each year for the next 5 years. Write a program 
with a loop that displays the projected semester tuition amount for the next 5 years. 
'''

tuition_fee = 8000
increase = 0.03 # 3%

print('Projected semester tuition amount for the next 5 years(by 3% increase each year). \n')
print(' YEAR \t TUITION FEE \n -------------------')
for year in range(1,6):
    projected_increase = increase * tuition_fee
    
    tuition_fee += projected_increase
    print(' {} \t ${:,.2f}'.format(year,tuition_fee))
    