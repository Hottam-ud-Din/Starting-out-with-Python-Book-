'''
13. Population
Write a program that predicts the approximate size of a population of organisms. The application should use text boxes to allow the user to enter the starting number of organisms, the average daily population increase (as a percentage), and the number of days the organisms will be left to multiply. For example, assume the user enters the following values:

Starting number of organisms: 2

Average daily increase: 30%

Number of days to multiply: 10

The program should display the following table of data:

               Day Approximate       Population
                     1                   2
                     2                   2.6
                     3                   3.38
                     4                   4.394
                     5                   5.7122
                     6                   7.42586
                     7                   9.653619
                     8                   12.5497
                     9                   16.31462
                     10                  21.209
'''

start_number_of_organisms = int(input('Enter the starting number of organisms: '))
daily_increase = float(input('Enter the average daily increase: ')) / 100
number_of_days = int(input('Enter the number of days to multiply: '))

population = start_number_of_organisms

print("Day\tApproximate Population")
print("---------------------------")

for day in range(1, number_of_days + 1):
    print(f"{day}\t{population:.2f}")
    population += (population * daily_increase)
