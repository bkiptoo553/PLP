"""
1. Write a program that accepts user input to create a list of integers. 
Then, compute the sum of all the integers in the list 
"""

def challenge_1():
    UserInput = input("Enter an integer: ")
    IntegerList = [7, 8 ,2]

    try:
        UserInput = int(UserInput)
        IntegerList.append(UserInput)
    except ValueError:
        print("That is not a valid integer.")

    print(IntegerList)

challenge_1()

"""
2. Create a tuple containing the names of five of your favorite books. 
Then, use a for loop to print each book name on a separate line
"""

def challenge_2():
    MyTuble = ("book 1", "book 2", "book 3", "book 4", "book 5")

    for i in MyTuble:
        print(i)

challenge_2()

"""
3. Write a program that uses a dictionary to store information about a person, 
such as their name, age, and favorite color. 
Ask the user for input and store the information in the dictionary. 
Then, print the dictionary to the console
"""

def challenge_3():
    person = {}

    person["name"] = input("Enter your name: ")
    person["age"] = input("Enter your age: ")
    person["favoriteColor"] = input("Enter your favorite color: ")


    print("\nUserInformation:")
    print(person)

challenge_3()

"""
4.Write a program that accepts user input to create two sets of integers. 
Then, create a new set that contains only the elements that are common to both sets.
"""

def challenge_4():
    inputString_1 = input("Enter integers for Set 1: ")
    inputString_2 = input("Enter integers for Set 2: ")

    inputList_1 = inputString_1.split()
    inputList_2 = inputString_2.split()

    intList_1 = []
    for numStr in inputList_1:
        intList_1.append(int(numStr))

    intList_2 = []
    for numStr in inputList_2:
        intList_2.append(int(numStr))

    set1 = set(intList_1)
    set2 = set(intList_2)


    commonSet = set1 & set2

    print("\nCommon elements:")
    print(commonSet)

challenge_4()

"""
5. Create a program that stores a list of words. 
Then, use list comprehension to create a new list 
that contains only the words that have an odd number of characters.
"""

def challenge_5():
    words = ["apple", "banana", "cat", "dog", "elephant", "sun"]
    
    oddWords = []

    for w in words:
       length = len(w)
       if length % 2 != 0:
         oddWords.append(w)


    print("Words with odd number of characters:")
    print(oddWords)

challenge_5()
