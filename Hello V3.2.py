 # answer to user with different text
    # get user name
name = input("What is your name? ")
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
name = ver2(name)
    # print different answers by length of the name
if len(name) > 2 and len(name) < 4:
    # create different versions of answer
    print((f"Hello {name}, Nice to meet you.").strip().title())
elif len(name) > 5 and len(name) < 8:
    print((f"Hi {name}, thank you for invitation").strip().title())
else:
    print((f"Hello {name}, great job").strip().title())
