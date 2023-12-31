'''
8. Hot Dog Cookout Calculator
Assume hot dogs come in packages of 10, and hot dog buns come in packages of 8. Write a 
program that calculates the number of packages of hot dogs and the number of packages of 
hot dog buns needed for a cookout, with the minimum amount of leftovers. The program 
should ask the user for the number of people attending the cookout and the number of hot 
dogs each person will be given. The program should display the following details:

1. The minimum number of packages of hot dogs required
2. The minimum number of packages of hot dog buns required
3. The number of hot dogs that will be left over
4. The number of hot dog buns that will be left over
'''

hotdog_per_package = 10
buns_per_package   = 8

people = int(input('Enter the number of people attending: '))
hotdog_per_person = int(input('Enter the number of hot dogs each person will be given: '))

hotdog_needed = people * hotdog_per_person
                         # the double divide(//) sign it gives the quotient only 
hotdog_required = hotdog_needed // hotdog_per_package
print(f'The minimum number of packages of hot dogs required is: {hotdog_required}')

buns_required = hotdog_needed // buns_per_package
print(f'The minimum number of packages of hot dog buns required is: {buns_required}')
                        # the % sign gives the remainder only
hotdog_left = hotdog_needed % hotdog_per_package
buns_left   = hotdog_needed % buns_per_package
print(f'The number of hot dogs that will be left over is: {hotdog_left}')
print(f'The number of  hot dog buns that will be left over is: {buns_left}')