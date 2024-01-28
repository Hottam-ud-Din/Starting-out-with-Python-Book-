'''
11. Sleep Debt
A “sleep debt” represents the difference between a person’s desirable and actual amount 
of sleep. Write a program that prompts the user to enter how many hours they slept each 
day over a period of seven days. Using 8 hours per day as the desirable amount of sleep, 
determine their sleep debt by calculating the total hours of sleep they got over the seven-day 
period and subtracting that from the total hours of sleep they should have got. If the user 
does not have a sleep debt, display a message expressing your jealousy. 
'''

desirable_sleep = 8*7
total_sleep = 0

for sleep in ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'):
    your_sleep = float(input(f'Enter how many hours you slept on {sleep}: '))
    total_sleep += your_sleep
    
sleep_debt = (desirable_sleep) - total_sleep

if sleep_debt > 0:
    print(f"\n Your sleep debt is {sleep_debt} hours.")
else:
    print("No sleep debt! I'm jealous of your well-rested state!")

