# Ask the user for their name
name = input("What is your name? ")
# remove extra spaces from start and end
name = name.strip()
# first symbol uppercase
name = name.title()

# function for remove extra spaces inside the text
def ver2(inputedText):
    # split text by separator " "
    text = inputedText.split(" ")
    # create empty list
    result = []
    # run loop to create new list without spaces
    for item in text:
        if item != "":
            result.append(item)
    return " ".join(result)
#put in function user's input value
name = ver2(name)

# print result with different code but as the same
print("Hello", name + ",nice to meet you")
print(f"Hello {name},nice to meet you")
