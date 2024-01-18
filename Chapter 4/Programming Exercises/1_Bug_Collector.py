'''
1. Bug Collector 
A bug collector collects bugs every day for five days. Write a program that keeps a running 
total of the number of bugs collected during the five days. The loop should ask for the 
number of bugs collected for each day, and when the loop is finished, the program should 
display the total number of bugs collected.
'''

# By for loop
total_bugs = 0

num_of_bugs_collected = int(input('Enter the number of bugs collected each day: '))

for i in range(5):
    total_bugs += num_of_bugs_collected
print(f'So the total number of bugs collected in five days is: {total_bugs}')


# By while loop
num_of_bugs = int(input('Enter the number of bugs collected each day: '))

bugs_collected = 0
day = 0
while day < 5:
    bugs_collected += num_of_bugs
    day += 1

print(f'So the total number of bugs collected in five days is: {bugs_collected}')