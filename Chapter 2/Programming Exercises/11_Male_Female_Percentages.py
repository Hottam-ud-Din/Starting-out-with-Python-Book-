'''
11.Male and Female Percentages
Write a program that asks the user for the number of males and the number of females registered in a class. The program should display the percentage of males and females in the class.

Hint: Suppose there are 8 males and 12 females in a class. There are 20 students in the 
class. The percentage of males can be calculated as 8 ÷ 20 = 0.4, or 40%. The percentage 
of females can be calculated as 12 ÷ 20 = 0.6, or 60%.
'''

male_std   = int(input("Enter the number of male students:"))
female_std = int(input("Enter the number of female students:"))
total_std  = male_std + female_std

per_male   = male_std/total_std * 100
per_female = female_std/total_std * 100

print(f'The total students in class are: {total_std}')
print(f'The percentage of male students in class is: {per_male: .0f}%')
print(f'The percentage of female students in class is: {per_female: .0f}%')
