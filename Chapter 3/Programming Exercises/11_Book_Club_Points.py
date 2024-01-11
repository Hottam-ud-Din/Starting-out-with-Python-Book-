'''
11. Book Club Points
Serendipity Booksellers has a book club that awards points to its customers based on the 
number of books purchased each month. The points are awarded as follows:

•	 If a customer purchases 0 books, he or she earns 0 points.

•	 If a customer purchases 2 books, he or she earns 5 points.

•	 If a customer purchases 4 books, he or she earns 15 points.

•	 If a customer purchases 6 books, he or she earns 30 points.

•	 If a customer purchases 8 or more books, he or she earns 60 points.

Write a program that asks the user to enter the number of books that he or she has purchased this month, then displays the number of points awarded. 
'''
books_purchased = int(input('Enter the Number of books you have purchased: '))

if books_purchased == 2 or books_purchased == 3:
    print('You have earnerd 5 points')
elif books_purchased == 4 or books_purchased == 5:
    print('You have earned 15 points')
elif books_purchased == 6 or books_purchased == 7:
    print('You have earned 30 points')
elif books_purchased >= 8:
    print('You have earned 60 points')
else:
    print('You have earned 0 points')
