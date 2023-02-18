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

glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    }

word = 'string'
print(f"\n{word.title()}: {glossary[word]}")

word = 'comment'
print(f"\n{word.title()}: {glossary[word]}")

word = 'list'
print(f"\n{word.title()}: {glossary[word]}")

word = 'loop'
print(f"\n{word.title()}: {glossary[word]}")

word = 'dictionary'
print(f"\n{word.title()}: {glossary[word]}")

#6-4: Glossary 2  Now that you know how to loop through a dictionary, clean
# up the code from Exercise 6-3 (page 99) by replacing your series of print()
# calls with a loop that runs through the dictionary’s keys and values.
# When you’re sure that your loop works, add five more Python terms to your glossary.
# When you run your program again, these new words and meanings should automatically be included in the output.

glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    'key': 'The first item in a key-value pair in a dictionary.',
    'value': 'An item associated with a key in a dictionary.',
    'conditional test': 'A comparison between two values.',
    'float': 'A numerical value with a decimal component.',
    'boolean expression': 'An expression that evaluates to True or False.',
    }

for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")

#6-5. Rivers: Make a dictionary containing three major rivers and the country each river runs through.
# One key-value pair might be 'nile': 'egypt'
#Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
#Use a loop to print the name of each river included in the dictionary.
#Use a loop to print the name of each country included in the dictionary.

rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'fraser': 'canada',
    'kuskokwim': 'alaska',
    'yangtze': 'china',
    }

for river, country in rivers.items():
    print(f"The {river.title()} flows through {country.title()}.")

print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print(f"- {river.title()}")

print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print(f"- {country.title()}")

#6-6: Polling
#Make a list of people who should take the favorite languages poll. Include
#some names that are already in the dictionary and some that are not.
#Loop through the list of people who should take the poll. If they have already taken the poll,
# print a message thanking them for responding. If they have not yet taken the poll,
# print a message inviting them to take the poll.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
    print("\n")

    coders = ['phil', 'josh', 'david', 'becca', 'sarah', 'matt', 'danielle']
    for coder in coders:
        if coder in favorite_languages.keys():
            print(f"Thank you for taking the poll, {coder.title()}!")
