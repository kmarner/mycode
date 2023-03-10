#!usr/bin/env python3

import os

"""Are you just a Supernatural fan or is it an obsession? Quiz | By Keriise Griffin-Marner"""

def clear():
    # this will have the linux OS clear the screen
    os.system("clear")


def main():

    # intro
    print("I want to know if you are you a true supernatural fan or just an imposter. Get ready!")

    question1 = {"question": "What are the names of Sam and Dean's parents?",
"Samantha And Jason": False,
"Mary And John": True,
"Martha And Dean": False,
"Mary And Joe": False
}

    correct_answer = False

    while not correct_answer:
        print(question1['question'])

        items = list(question1.items())
        for index, (key, value) in enumerate(items):
            if key != 'question':
                print(f"{index+0}. {key}")

        user_answer = input("Enter the correct answer: ").title()
        clear() # clears the screen
        for key, value in question1.items():
            if key == user_answer and value:
                print("Boom! You got it right!")
                correct_answer = True
            elif key == user_answer and not value:
                print("Maybe, you're not the fan I thought you were... try again.")
            elif user_answer not in question1.keys():
                print("That was not one of the provided answers. Try again.")
                break # this will break the FOR LOOP, not the while loop
         

    question2= {"question": "What is the name of the villain also known as \"yellow eyes\"?",
 "Crowley": False,
 "Metatron": False,
 "Ezekiel": False,
 "Azazel": True
 }

    print(question2['question'])

    items = list(question2.items())
    for index, (key, value) in enumerate(items):
        if key != 'question':
            print(f"{index+0}. {key}")


            correct_answer = False
    while not correct_answer:
        user_answer = input("Enter the correct answer: ").title()
        for key, value in question2.items():
            if key == user_answer and value:
                print("Boom! You got it right!")
                correct_answer = True
            elif key == user_answer and not value:
                print("Maybe, you're not the fan I thought you were... try again.")
            else:

                continue


    question3= {"question": "What type of car was passed down to Dean from his father?",
 "Chevrolet Impala": True,
 "Mercury Monterey": False,
 "Ford Mustang": False,
 "Dodge Challenger": False
 }
 
    print(question3['question'])

    items = list(question3.items())
    for index, (key, value) in enumerate(items):
        if key != 'question':
            print(f"{index+0}. {key}")


            correct_answer = False
    while not correct_answer:
        user_answer = input("Enter the correct answer: ").title()
        for key, value in question3.items():
            if key == user_answer and value:
                print("Boom! You got it right!")
                correct_answer = True
            elif key == user_answer and not value:
                print("Maybe, you're not the fan I thought you were... try again.")
            else:

                  continue

    # outro
    print("Thanks for hanging out. Always remember, \"We know a little bit about a lot of things. Just enough to make us dangerous. -Dean Winchester\"")
main()

