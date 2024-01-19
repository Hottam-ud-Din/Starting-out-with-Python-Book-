'''
2. Calories Burned
Running on a particular treadmill you burn 4.2 calories per minute. Write a program that 
uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes.
'''

CALORIES_BURN_PER_MINUTE = 4.2

print('MINUTES \t CALORIES BURNED')
for i in range(10,31,5):
    burned_calories = i * CALORIES_BURN_PER_MINUTE
    print(i, '\t\t' ,burned_calories)