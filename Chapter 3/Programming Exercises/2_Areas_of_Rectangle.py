'''
2. Areas of Rectangles
The area of a rectangle is the rectangle’s length times its width. Write a program that asks 
for the length and width of two rectangles. The program should tell the user which rectangle has the greater area, or if the areas are the same.
'''

height_rect_1 = int(input('Enter the height of the first rectangle: '))
width_rect_1  = int(input('Enter the width of first rectangle: '))

area_rect_1   = height_rect_1 * width_rect_1
print(f'The area of first rectangle is {area_rect_1}')

height_rect_2 = int(input('Enter the height of the second rectangle: '))
width_rect_2  = int(input('Enter the width of second rectangle: '))

area_rect_2   = height_rect_2 * width_rect_2
print(f'The area of the second rectangle is {area_rect_2}')
if area_rect_1 == area_rect_2:
    print('The area of both the rectangles are same')
elif area_rect_1 > area_rect_2:
    print('The area of first rectangle is greater')
else:
    print('The area of the second rectangle is greater')