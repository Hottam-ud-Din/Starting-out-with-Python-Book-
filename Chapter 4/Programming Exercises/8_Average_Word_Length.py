'''
8. Average Word Length
Write a program with a loop that repeatedly asks the user to enter a word. The user should 
enter nothing (press Enter without typing anything) to signal the end of the loop. Once the 
loop ends, the program should display the average length of the words entered, rounded to 
the nearest whole number
'''

word = input('Enter a word: ')

length = len(word)
count  = 0

while word != '':
    word = input('Enter a word: ')
    length += len(word)
    count  += 1
    
average = length / count

print()
print(f'Total words are: {count}')
print('The average lenght of the words is {:.0f} characters'.format(average))
