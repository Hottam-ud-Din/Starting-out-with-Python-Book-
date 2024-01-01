'''
1. Personal Information
Write a program that displays the following information:
1. Your name
2. Your address, with city, state, and ZIP
3. Your telephone number
4. Your college major
'''

name = input('Enter your name:')
address = input('Enter your address:')
telephone = int(input('Enter your telephone number:'))
college_major = input('Enter your college major:')

print(f'Your name is {name}. you are a resident of {address}.\n Your telephone number is {telephone} and you are a student of {college_major}.')
