#Madlibs game
#word game where you create a story by filling in blanks with random words

adjective1 = input("Enter an Adjective attributing a place :")
noun1 = input("Enter a food name in a broader spectrum like coffee, pizza, pasta etc :")
noun2 =input("Enter a particular food name based on the previous selection e.g. Irish coffee, arrabiata, Truffle and Mushroom etc. :")
adjective2 = input("Enter an adjective that characterizes a food")
time = input("Enter a time duration in minutes taken to prepare and serve the food/beverage : ")
noun3 = input("Enter a noun form of eating -> bite/sip :")
adjective3 = input("Enter an adjective to characterize the feeling after tasting! :")

print(f"Today I went to a {adjective1} cafe.")
print(f"I saw varieties of {noun1} in the menu")
print(f"I ordered a {noun2} because it seemed {adjective2}")
print(f"The order was delivered in {time} minutes and i took a {noun3} of it")
print(f"I was {adjective3} by the taste!")