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
