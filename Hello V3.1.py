# answer to user with different text
    # import random modul
import random
    # get user name
name = input("What is your name? ")
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
