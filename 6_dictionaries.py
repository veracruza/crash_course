#6-1. Person: Use a dictionary to store information about a person you know.
#Store their first name, last name, age, and the city in which they live. You
#should have keys such as first_name, last_name, age, and city. Print each
#piece of information stored in your dictionary.

person = {
    'first_name': 'kate',
    'last_name': 'miller',
    'age': 28,
    'city': 'Kyiv',
    }

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

#6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your dictionary. Think of a favorite
# number for each person, and store each as a value in your dictionary.
# Print each person’s name and their favorite number. For even more fun, poll a few friends
# and get some actual data for your program.

favorite_numbers = {
    'kate': 13,
    'eva': 23,
    'alex': 77,
    'vera': 19,
    'maxim': 6,
    }

num = favorite_numbers['kate']
print(f"Kate's favorite number is {num}.")

num = favorite_numbers['eva']
print(f"Eva's favorite number is {num}.")

num = favorite_numbers['alex']
print(f"Alex's favorite number is {num}.")

num = favorite_numbers['vera']
print(f"Vera's favorite number is {num}.")

num = favorite_numbers['maxim']
print(f"Maxim's favorite number is {num}.")

#6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
# Think of five programming words you’ve learned about in the previous chapters.
#  Use these words as the keys in your glossary, and store their meanings as values.
#Print each word and its meaning as neatly formatted output. You might print the word followed by
# a colon and then its meaning, or print the word on one line and then print its meaning indented on
# a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.