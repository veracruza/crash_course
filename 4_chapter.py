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







