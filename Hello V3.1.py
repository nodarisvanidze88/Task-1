    # answer to user with different text
    # import random modul
import random
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
    # create different versions of answer
ver1 = (f"Hello {name}, Nice to meet you.").strip().title()
ver2 = (f"Hi {name}, thank you for invitation").strip().title()
ver3 = (f"Hello {name}, great job").strip().title()
    # create the array list of answers
list = [ver1,ver2,ver3]
    # get array length
listLength = len(list)
    # get rendom number from list length [0:listLength]
randomNum = random.randint(0,len(list)-1)
    # print result
print(list[randomNum])
