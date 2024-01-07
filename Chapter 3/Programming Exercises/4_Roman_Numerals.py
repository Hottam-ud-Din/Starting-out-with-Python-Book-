'''
4. Roman Numerals
Write a program that prompts the user to enter a number within the range of 1 through 10. 
The program should display the Roman numeral version of that number. If the number is 
outside the range of 1 through 10, the program should display an error message. The following table shows the Roman numerals for the numbers 1 through 10:

                         NUMBER          ROMAN NUMERAL
                         1                  I
                         2                  II
                         3                  III
                         4                  IV
                         5                  V
                         6                  VI
                         7                  VII
                         8                  VIII
                         9                  IX
                         10                 X
'''

number = int(input('Enter a number between 1 and 10: '))

if number == 1:
    print(f'{number} in Roman Numerals is "I"')
elif number == 2:
    print(f'{number} in Roman Numerals is "II"')
elif number == 3:
    print(f'{number} in Roman Numerals is "III"')
elif number == 4:
    print(f'{number} in Roman Numerals is "IV"')
elif number == 5:
    print(f'{number} in Roman Numerals is "V"')
elif number == 6:
    print(f'{number} in Roman Numerals is "VI"')
elif number == 7:
    print(f'{number} in Roman Numerals is "VII"')
elif number == 8:
    print(f'{number} in Roman Numerals is "VIII"')
elif number == 9:
    print(f'{number} in Roman Numerals is "IX"')
elif number == 10:
    print(f'{number} in Roman Numerals is "X"')
else:
    print('ERROR!\n Enter the number between 1 and 10')