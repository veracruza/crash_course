# 3-1. Names: Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the list, one at a time.

friends = ['Kate', 'Alex', 'Victoria']
print(friends[0].title())
print(friends[1].title())
print(friends[2].title())

# 3-2: Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the person’s name.

friends = ['Kate', 'Alex', 'Victoria']
msg = f"Hello, {friends[0].title()}!"
print(msg)

msg = f"Hello, {friends[1].title()}!"
print(msg)

msg = f"Hello, {friends[2].title()}!"
print(msg)

# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.

guests = ['Kate', 'Alex', 'Victoria']

name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

#3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
#Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.

name = guests[1].title()
print(f"\nSorry, {name} can't make it to dinner.")

#Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
del guests[1]
guests.insert(1, 'Diana')

#Print a second set of invitation messages, one for each person who is still in your list.
name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

#3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.

print("\nWe got a bigger table!")

#Use insert() to add one new guest to the beginning of your list.
guests.insert(0, 'Eva')

#Use insert() to add one new guest to the middle of your list.
guests.insert(3, 'Sophia')

#Use append() to add one new guest to the end of your list.
guests.append('Melanie')

#Print a new set of invitation messages, one for each person in your list.
name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

name = guests[3].title()
print(f"{name}, please come to dinner.")

name = guests[4].title()
print(f"{name}, please come to dinner.")

name = guests[5].title()
print(f"{name}, please come to dinner.")

#3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.

print("\nSorry, we can only invite two people to dinner.")

#Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
eva_off = guests.pop(0)
print(f"Sorry, {eva_off.title()} there's no room at the table.")

sophia_off = guests.pop(2)
print(f"Sorry, {sophia_off.title()} there's no room at the table.")

melanie_off = guests.pop(3)
print(f"Sorry, {melanie_off.title()} there's no room at the table.")

victoria_off = guests.pop(2)
print(f"Sorry, {victoria_off.title()} there's no room at the table.")

#Print a message to each of the two people still on your list, letting them know they’re still invited.
name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

#Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.
del(guests[0])
del(guests[0])
print(guests)

#3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
#Store the locations in a list. Make sure the list is not in alphabetical order.
#Print your list in its original order. Don’t worry about printing the list neatly, just print it as a raw Python list.
locations = ['berlin', 'nederland', 'alps', 'paris', 'alicante']
print("\nHere is the original list:")
print(locations)

#Use sorted() to print your list in alphabetical order without modifying the actual list.
#Show that your list is still in its original order by printing it.
print("\nHere is the sorted list:")
print(sorted(locations))

#Use sorted() to print your list in reverse alphabetical order without chang- ing the order of the original list.
print("\nReverse alphabetical:")
print(sorted(locations, reverse=True))

#Use reverse() to change the order of your list. Print the list to show that its order has changed
print("\nReversed:")
locations.reverse()
print(locations)

#Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
print("\nOriginal order:")
locations.reverse()
print(locations)

#Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
print("\nAlphabetical")
locations.sort()
print(locations)

#Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.
print("\nReverse alphabetical")
locations.sort(reverse=True)
print(locations)

#3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 through 3-7 (page 42), use len() to print a message indicating the number of people you are inviting to dinner.

guests = ['Kate', 'Alex', 'Victoria']
inviting = len(guests)
print("\nInviting to dinner: {inviting}")

