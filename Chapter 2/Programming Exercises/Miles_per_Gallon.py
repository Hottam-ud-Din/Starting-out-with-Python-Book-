'''
### 7. Miles-per-Gallon
A car's miles-per-gallon (MPG) can be calculated with the following formula:

                     MPG = Miles driven/Gallons of gas used

Write a program that asks the user for the number of miles driven and the gallons of gas 
used. It should calculate the car's MPG and display the result.
'''

miles_driven     = float(input("Enter the number of miles drives:"))
gallons_gas_used = float(input("Enter the number of gallons of gas used"))

MPG = miles_driven/gallons_gas_used

print(f"So the car's miles-per-gallon(MPG) is: {MPG}")