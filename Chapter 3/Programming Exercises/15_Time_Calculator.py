'''
15. Time Calculator
Write a program that asks the user to enter a number of seconds and works as follows:

•	 There are 60 seconds in a minute. If the number of seconds entered by the user is greater
than or equal to 60, the program should convert the number of seconds to minutes and seconds.

•	 There are 3,600 seconds in an hour. If the number of seconds entered by the user is greater than or equal to 3,600, the program should convert the number of seconds to hours, minutes, and seconds.

•	 There are 86,400 seconds in a day. If the number of seconds entered by the user is greater than or equal to 86,400, the program should convert the number of seconds to days, hours, minutes, and seconds.
'''

number_of_seconds = int(input("Enter the number of seconds: "))

if number_of_seconds < 60 and number_of_seconds >=0:
    seconds = number_of_seconds
    print(f'Seconds: {seconds}')
    
elif number_of_seconds >= 60 and number_of_seconds < 3600:
    minutes = number_of_seconds // 60
    seconds = number_of_seconds % 60
    print(f'Minutes: {minutes}')
    print(f'Seconds: {seconds}')      

elif number_of_seconds >= 3600 and number_of_seconds < 86400:
    hours   = number_of_seconds // 3600
    minutes = (number_of_seconds % 3600) // 60
    seconds = (number_of_seconds % 3600) % 60
    print(f'Hours: {hours}')
    print(f'Minutes: {minutes}')
    print(f'Seconds: {seconds}')
        
elif number_of_seconds >= 86400:
    days    = number_of_seconds // 86400
    
    hours   = (number_of_seconds % 86400) // 3600
    
    minutes = ((number_of_seconds % 86400) % 3600) // 60
    
    seconds = (((number_of_seconds % 86400) % 3600) % 60) % 60

    print(f'Days: {days}')
    print(f'Hours: {hours}')
    print(f'Minutes: {minutes}')
    print(f'Seconds: {seconds}')
    
else:
    print("Invalid input: Number of seconds should be non-negative.")
        