#2-3. Personal Message: Use a variable to represent a person’s name, and print a message to that person.

name = "Veronica"
text = "what is your favorite programming language"
message_for = f"{name}, {text}"
message = f"Hello, {message_for}?"
print(message)

#2-4. Name Cases: Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case.

name = "Veronica Luhova"
print(name.lower())
print(name.title())
print(name.upper())

#2-5.Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author.

print ("Volodymyr Zelensky once said: 'Light will win over darkness.''")

#2-6. Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called famous_person. Then compose your message and represent it with a new variable called message. Print your message.

famous_person = 'Volodymyr Zelensky'
message = "'I need ammunition, not a ride.'"
print("{0} once said: {1}".format(famous_person, message))
