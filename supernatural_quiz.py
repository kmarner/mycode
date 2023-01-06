#!usr/bin/env python3

"""Are you just a Supernatural fan or is it an obsession? Quiz | By Keriise Griffin-Marner"""


def main():



 

    question1 = {"question": "What are the names of Sam and Dean's parents?",
"Samantha And Jason": False,
"Mary And John": True,
"Martha And Dean": False,
"Mary And Joe": False
}

    print(question1['question'])
    
    items = list(question1.items())
    for index, (key, value) in enumerate(items):
        if key != 'question':
            print(f"{index+0}. {key}")
            
            
            correct_answer = False
    while not correct_answer:
        user_answer = input("Enter the correct answer: ").title()
        for key, value in question1.items():
            if key == user_answer and value:
                print("Boom! You got it right!")
                correct_answer = True
            elif key == user_answer and not value:
                print("Maybe, you're not the fan I thought you were... try again.")
            else:
                                  
                  continue

main()
