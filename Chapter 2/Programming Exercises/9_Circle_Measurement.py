'''
9. Circle Measurements
Write a program that asks the user to enter the radius of a circle. The program should calculate and display the area and circumference of the circle using (πr-square)for the area and 2πr for the circumference.

Hint: You can either use 3.14159 as the value of pi (π), or add the statement "import math"
to the start of the program and then use "math.pi" wherever you need the value of pi in 
the program.
'''

import math

circle_radius = float(input("Enter the radius of the circle:"))

circle_area   = math.pi * circle_radius**2
circumference = 2 * math.pi * circle_radius

print(f'The area of the circle is: {circle_area:.2f}')
print(f'The circumference of the circle is: {circumference:.2f}')
