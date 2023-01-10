#4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
favorite_pizzas = ['pepperoni', 'cheese', 'bbq_chicken']
for pizza in favorite_pizzas:
    print(pizza)

#Modify your for loop to print a sentence using the name of the pizza instead of printing just the name of the pizza. For each pizza you should have one line of output containing a simple statement like I like pepperoni pizza.
for pizza in favorite_pizzas:
    print(f"I really like {pizza} pizza!")

#Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!
print("\nI really love pizza!")

#4-2. Animals: Think of at least three different animals that have a common char- acteristic. Store the names of these animals in a list, and then use a for loop to print out the name of each animal.

favorite_pets = ['dog', 'bird', 'cat']
for pet in favorite_pets:
    print(pet)

#Modify your program to print a statement about each animal
for pet in favorite_pets:
    print(f"A {pet} would make a great pet")
#Add a line at the end of your program stating what these animals have in common.
print("\nAny of these animals would make a great pet!")

#4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.

numbers = list(range(1,21))
for number in numbers:
    print(number)

#4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers.

numbers = list(range(1, 1_000_001))

print(min(numbers))
print(max(numbers))
print(sum(numbers))

#4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.

odd_numbers = list(range(1, 21, 2))
for number in odd_numbers:
    print(number)

#4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.

threes = list(range(3, 31, 3))
for number in threes:
    print(number)

#4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.

cubes = []
for number in range(1, 11):
    cube = number**3
    cubes.append(cube)
for cube in cubes:
    print(cube)

#4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.

cubes = [number**3 for number in range(1, 11)]
for cube in cubes:
    print(cube)

#4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
#Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.

favorite_pizzas = ['pepperoni', 'cheese', 'bbq_chicken', 'hawaiian', 'margherita ']
print('The first three items in the list are:')
for pizza in favorite_pizzas[:3]:
    print(pizza.title())

#Use a slice to print three items from the middle of the list.
favorite_pizzas = ['pepperoni', 'cheese', 'bbq_chicken', 'hawaiian', 'margherita ']
print('Three items from the middle of the list are:')
for pizza in favorite_pizzas[1:4]:
    print(pizza.title())

#Use a slice to print the last three items in the list.
favorite_pizzas = ['pepperoni', 'cheese', 'bbq_chicken', 'hawaiian', 'margherita ']
print('The last three items in the list are:')
for pizza in favorite_pizzas[-3:]:
    print(pizza.title())

#4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas.

my_pizzas = ['pepperoni', 'cheese', 'bbq_chicken']
friend_pizzas = my_pizzas[:]
#Then, do the following:
#Add a new pizza to the original list.
my_pizzas.append('margherita')
#Add a different pizza to the list friend_pizzas.
friend_pizzas.append('hawaiian')
#Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. Print the message My friend’s favorite pizzas are:, and then use a for loop to print the sec- ond list. Make sure each new pizza is stored in the appropriate list.
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(f"- {pizza}")

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"- {pizza}")

#4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing to save space. Choose a version of foods.py, and write two for loops to print each list of foods.

my_foods = ['pizza', 'falafel', 'carrot cake']
my_foods.append('cannoli')
print("My favorite foods are:")
for foods in my_foods[:3]:
    print(foods)
print("My favorite foods are:")
for foods in my_foods[3:]:
    print(foods)
#4-13.Buffet: A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.
#Use a for loop to print each food the restaurant offers.
#Try to modify one of the items, and make sure that Python rejects the change.
#The restaurant changes its menu, replacing two of the items with different foods. Add a block of code that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.

menu_items = (
    'rockfish sandwich', 'halibut nuggets', 'smoked salmon chowder',
    'salmon burger', 'crab cakes',
    )

print("You can choose from the following menu items:")
for item in menu_items:
    print(f"- {item}")

menu_items = (
    'rockfish sandwich', 'halibut nuggets', 'smoked salmon chowder',
    'black cod tips', 'king crab legs',
    )

print("\nOur menu has been updated.")
print("You can now choose from the following items:")
for item in menu_items:
    print(f"- {item}")

#4-15. Code Review: Choose three of the programs you’ve written in this chapter and modify each one to comply with PEP 8:

#Use four spaces for each indentation level. Set your text editor to insert four spaces every time you press tab, if you haven’t already done so (see Appendix B for instructions on how to do this).
#Use less than 80 characters on each line, and set your editor to show a vertical guideline at the 80th character position.
#Don’t use blank lines excessively in your program files.




