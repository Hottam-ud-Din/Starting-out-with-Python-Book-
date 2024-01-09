'''
7. Grade Calculator
A class has two tests worth 25 points each along with a main exam worth 50 points. For a student to pass the class, they must obtain an overall score of at least 50 points, and must obtain at least 25 points in the main exam. If a student’s total score is less than 50 or they obtain less than 25 points in the main exam, they receive a grade of “Fail”. Otherwise, their grade is as follows: 

1. If they get more than 80, they get a grade of “Distinction”. 50–59 = “Pass”.
2. If they get less than 80 but more than 60, they get a “Credit” grade.
3. If they get less than 60, they get a ”Pass” grade.

Write a program that prompts the user to enter their points for both tests and the exam and 
converts the values to integers. The program should first check if the points entered for the 
tests and exam are valid. If any of the test scores are not between 0 and 25, or the exam 
score is not between 0 and 50, the program should display an error message. Otherwise, 
the program should display the total points and the grade.
'''

test_1    = int(input('Enter your points of first test (between 0-25): '))
test_2    = int(input('Enter your points of second test (between 0-25): '))
main_test = int(input('Enter your points of main test (between 0-50): '))

if test_1 < 0 or test_1 > 25 or test_2 < 0 or test_2 > 25 or main_test < 0 or main_test > 50:
    print('Invalid input \n Enter points between 0 and 25 for test_1 and test_2 \n'
          'Enter marks between 0 and 50 for main test')
else:
    total_points = test_1 + test_2 + main_test
    
    if total_points < 50 or main_test < 25:
        grade = 'Fail'
    elif total_points >= 80:
        grade = 'Distinction'
    elif total_points >= 60 and total_points < 80:
        grade = 'Credit grade'
    else:
        grade = 'Pass'
    
    print(f'Total Points: {total_points}')
    print(f'Grade: {grade}')