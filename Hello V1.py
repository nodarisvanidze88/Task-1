# Ask the user for their name
name = input("What is your name? ")
# remove extra spaces from start and end
name = name.strip()
# first symbol uppercase
name = name.title()
# print result with different code but as the same
print("Hello", name + ",nice to meet you")
print(f"Hello {name},nice to meet you")
# problems: what if the user will imput extra spaces between words for example "test      test"
