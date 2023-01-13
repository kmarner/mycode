#!/usr/bin/env python3
"""Dummy-Proof Date Night Idea Generator | Author: Keriise Griffin-Marner

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

api_key = os.environ.get("YELP_API")

def parameters(location, term, radius, culture, diet, price, api_key):
    # API endpoint
    endpoint = "https://api.yelp.com/v3/businesses/search"
    
    # API request URL
    url = endpoint + "?location=" + location + "&term=" + term + "&radius=" + radius + "&categories=" + culture + "&categories2=" + diet + "&price=" + price + "&open_now=true&attributes=&sort_by=best_match&limit=20"

    # ASK & DELETE
    headers = {
    "Authorization": f"Bearer {api_key}"
    }    
    ### Unix time to check for a different date instead of "open now"

    # API request and handle the response
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
    
        # Print response
        print(data)

    else:
        print(f'Hmmmm... I can\'t seem to find anything that fits those exact responses. Would you like to try again?')
        print(response.text)

# Main function to run the code
def main():

    # ??? DO I NEED A TRY/EXCEPT FUNCTION FOR EACH QUESTION TO ENSURE NO OTHER INPUT IS ACCEPTED -- TO BE REPLACED WITH QUESTIONS--OPTIONS WILL BE GIVEN INSTEAD OF MULTIPLE CHOICE--
    location = input("location:")
    term = input("term: ")
    radius = input("radius: ")
    culture = input("culture: ")
    diet = input("diet: ")
    price = input("price: ")
    # date = input("date: ")
    parameters(location, term, radius, culture, diet, price, api_key)

main()
