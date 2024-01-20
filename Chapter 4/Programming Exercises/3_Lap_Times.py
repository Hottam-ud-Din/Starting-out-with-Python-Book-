'''
3. Lap Times
Write a program that asks the user to enter the number of times that they have run around 
a racetrack, and then uses a loop to prompt them to enter the lap time for each of their laps. 
When the loop finishes, the program should display the time of their fastest lap, the time of 
their slowest lap, and their average lap time.
'''

num_of_laps = int(input('Enter the number of times you run around a racetrack: '))

fastest_time = None
slowest_time = None

average = 0

for lap in range(1,num_of_laps+1):
    time = float(input(f'Enter the time of lap {lap} in seconds: '))
    
    if fastest_time == None:
        fastest_lap = lap
        fastest_time = time
        
    elif time < fastest_time:
        fastest_lap = lap
        fastest_time = time
#     fastest_lap += time
    
    if slowest_time == None:
        slowest_lap = lap
        slowest_time = time
    elif time > slowest_time:
        slowest_lap = lap
        slowest_time = time
#     slowest_lap += time
    
    average += time
    
average /= num_of_laps  
    
print(f'So the fastest lap is lap {fastest_lap}')
print(f'So the slowest lap is lap {slowest_lap}')
print(f'The average time of all the laps is {average:,.2f}')
