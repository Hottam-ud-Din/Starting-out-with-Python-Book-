'''
13.Planting Grapevines
A vineyard owner is planting several new rows of grapevines, and needs to know how many 
grapevines to plant in each row. She has determined that after measuring the length of a 
future row, she can use the following formula to calculate the number of vines that will fit 
in the row, along with the trellis end-post assemblies that will need to be constructed at 
each end of the row:
                    V = (R-2E)/S 
The terms in the formula are:
1. V is the number of grapevines that will fit in the row.
2. R is the length of the row, in feet.
3. E is the amount of space, in feet, used by an end-post assembly.
4. S is the space between vines, in feet.

Write a program that makes the calculation for the vineyard owner. The program should ask the user to input the following:
1. The length of the row, in feet
2. The amount of space used by an end-post assembly, in feet
3. The amount of space between the vines, in feet

Once the input data has been entered, the program should calculate and display the number of grapevines that will fit in the row.
'''

row_length     = float(input("Enter the length of the row in feet:"))
end_post_space = float(input("Enter the amount of space used by an end-post assembly in feet:"))
vine_space     = float(input("Enter the amount os space between the vines in feet:"))

vines_per_row = (row_length-2*end_post_space)/vine_space

print(f'So the number of grapevines that will fit in the row is: {int(vines_per_row)}')