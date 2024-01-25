'''
9. Ocean Levels
Assuming the ocean’s level is currently rising at about 1.6 millimeters per year, create an 
application that displays the number of millimeters that the ocean will have risen each year 
for the next 25 years 
'''

rise_per_year = 1.6

print(' YEAR \t RISE \n ------------')
for year in range(1,26):
    rise = year * rise_per_year
    print(' {} \t {:.2f} millimeters'.format(year,rise))
    
    