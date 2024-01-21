'''
4. Distance Traveled
The distance a vehicle travels can be calculated as follows:
                                 
                           distance = speed * time
For example, if a train travels 40 miles per hour for three hours, the distance traveled is 
120 miles. Write a program that asks the user for the speed of a vehicle (in miles per hour) 
and the number of hours it has traveled. It should then use a loop to display the distance 
the vehicle has traveled for each hour of that time period. Here is an example of the desired 
output:

What is the speed of the vehicle in mph? 40 Enter
How many hours has it traveled? 3 Enter

                  Hour                 DIstance traveled
                  1                         40
                  2                         80
                  3                         120
'''

speed = int(input('Enter the speed of the vahicel in mph: '))
hours = int(input('Enter how many hours has it traveled: '))


print('\n Hour \t Distance Traveled')
print('----------------------------')

for i in range(1,hours+1):
    distance = speed * i
    print(i,'\t\t',distance)