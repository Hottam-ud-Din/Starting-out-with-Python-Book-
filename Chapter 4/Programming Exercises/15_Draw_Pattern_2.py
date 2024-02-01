'''
15. Write a program that uses nested loops to draw this pattern
    ##
    # #
    #  #
    #   #
    #    #
    #     #         
'''

no_rows = int(input('Enter number of rows: '))

for i in range(no_rows):
    print('#',end='')
    for j in range(i):
        print(' ',end = '')
    print('#')