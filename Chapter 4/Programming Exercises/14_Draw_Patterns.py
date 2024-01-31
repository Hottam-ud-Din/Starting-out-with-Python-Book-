'''
14.Write a program that uses nested loops to draw this pattern:

      *******
      ******
      *****
      ****
      ***
      **
      *
'''
# TWO METHODS

# # METHOD 1
rows = int(input('Enter number of rows: '))
for i in range(rows,0,-1):
    print('*' * i)
    
print()

# METHOD 2

for i in range(rows, 0, -1):  
        for j in range(i):    
            print('*', end='')
        print()
        