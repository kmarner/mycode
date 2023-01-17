#!/usr/bin/env python3
"""Dinner Date Night Idea Generator | Author: Keriise Griffin-Marner

   Description:
   A script to utilize user input to generate the perfect date night 
   
   documentation for the API is available at https://docs.developer.yelp.com/docs/getting-started

   date_night_inspiration.py

   """


# to choose random answer from various results based on user input
import os
import random
import requests
import datetime
from pprint import pprint

# Welcome

def intro ():
    name = input("Welcome to the date night dinner idea generator! What's your name?\n")
    print("Hey {}! I know trying to make a last minute decision for dinner ccan really bring down the mood of a date night. So let's take some of the stress out of preparing for your upcoming date.\n".format(name))

# API Authorization
api_key = os.environ.get("YELP_API")

def parameters(location, term, api_key): # diet, price
    print(location, term)

    headers = {'Authorization': f'Bearer {api_key}'}
    
   
    url='https://api.yelp.com/v3/businesses/search'


    # In the dictionary, term can take values like food, cafes or businesses like McDonalds
    params = {'term': term,'location':location, 'limit': 50}

    response=requests.get(url, params=params, headers=headers)

    # Response verification
    if response.status_code == 200:
        data = response.json()
        businesses = data["businesses"]
        random.shuffle(businesses) # Shuffle API call results
       
        # Choose 6 businesses from shuffled results to display
        for i in range(6):
            business = businesses[i]
            for x in data["businesses"]:
                # Format output: Name/Address/Phone Number/URL
                display_address = " ".join(x["location"]["display_address"])
                display_address = display_address.replace(",","").replace(".","")
                print("Business Name: {} \nAddress: {} \nPhone Number: {} \nUrl: {}".format(x["name"], display_address, x["phone"], x["url"]))
                print()



    # If no business matches are found
    else:
        print(f'Hmmmm... I can\'t seem to find anything that fits those exact responses. Would you like to try again?')
        print(response.text)


    # Provide user option to have selection made for them

    while True:

        print ("These seem like some amazing places. If you're still having strouble making a selection, I can make it for you. Would you like me to? (y/n)")

        user_input = input()


        if user_input == "y":

            # Format output
            random_item = random.choice(data["businesses"])
            display_address = " ".join(random_item["location"]["display_address"])
            display_address = display_address.replace(",","").replace(".","")
            print("\nBusiness Name: {} \nAddress: {} \nPhone Number: {} \nUrl: {}".format(random_item["name"], display_address, random_item["phone"], random_item["url"]))
            print()
            print("This is going to be great! Now all you have to do is make a wardrobe selections and you're ready to go!")

            break

        elif user_input == "n":
            print("Perfect! Now all you need to do is make a few wardrobe selections and you're ready to go!")

            break

        else:
            print("That's not working. Let's keep it simple, please enter y or n")

# Main function to run the code/Request user input
def main():

    # Input for API search
    
    location = input("Let's start by telling me where you are. You can give me a zip code or a city & state. Which ever works best for you.\n")
    term = input("What is a type of food you've always wanted to try, but never went for?\n")
    parameters(location, term, api_key) 

intro()
main()

