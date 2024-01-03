'''
10.Ingredient Adjuster
A cookie recipe calls for the following ingredients:
1. 1.5 cups of sugar
2. 1 cup of butter
3. 2.75 cups of flour

The recipe produces 48 cookies with this amount of the ingredients. Write a program that 
asks the user how many cookies he or she wants to make, then displays the number of cups 
of each ingredient needed for the specified number of cookies. 
'''

sugar_per_cookie  = 1.5 / 48
butter_per_cookie = 1 / 48
flour_per_cookie  = 2.75 / 48

cookies = int(input("Enter the number of cookies you want to make:"))

sugar_needed  = sugar_per_cookie  * cookies
buuter_needed = butter_per_cookie * cookies
flour_needed  = flour_per_cookie  * cookies

print(f"So for {cookies} number of cookies, You will need:\n SUGAR: {sugar_needed:.2f} cups",
f"\n BUTTER: {buuter_needed:.2f} cups \n FLOUR: {flour_needed:.2f} cups")
