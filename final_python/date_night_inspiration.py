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
from pprint import pprint

api_key = os.environ.get("YELP_API")

def parameters(location, term, api_key): # diet, price
    print(location, term)

    headers = {'Authorization': f'Bearer {api_key}'}

    url='https://api.yelp.com/v3/businesses/search'

    # In the dictionary, term can take values like food, cafes or businesses like McDonalds
    params = {'term': term,'location':location, 'limit': 5} #, 'radius': radius}

    response=requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()

        for x in data["businesses"]:
            print(x["name"])
            print(x["url"])
            print()

    else:
        print(f'Hmmmm... I can\'t seem to find anything that fits those exact responses. Would you like to try again?')
        print(response.text)

# Main function to run the code
def main():

    # Input for API search
    location = input("location:") or "New York City"
    term = input("term: ") or "seafood"
    radius = input("radius: ") or 50
    #culture = input("culture: ") or "indian"
    #diet = input("diet: ") or ""
    #price = input("price: ") or ""
    # date = input("date: ") or ""
    parameters(location, term, api_key) # diet, price

main()
