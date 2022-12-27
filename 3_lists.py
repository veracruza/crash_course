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
