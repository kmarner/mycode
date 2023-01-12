#!/usr/bin/env python3
"""Dummy-Proof Date Night Idea Generator | Author: Keriise Griffin-Marner

   Description:
   A script to utilize user input to generate the perfect date night 
   
   documentation for the API is available at https://docs.developer.yelp.com/docs/getting-started

   date_night_inspiration.py

   """


# to choose random answer from various results based on user input
import random
import requests
import datetime



# def question():
     # Questions in different document

def main():

    name = input("Welcome to the dummy-proof date night idea genearator! What's your name?")
    print("Hey {}! I know last minute decision making can really bring down the mood of a date night. So let's take some of the stress out of preparing for your upcoming date.".format(name))

    url = "https://api.yelp.com/v3/businesses/search?sort_by=best_match&limit=20"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer tIYoNzvW_s1MIHblbcM2Zyhx6PhKsStCktqbRWLQ7_S27aOo9Y-J1WLK8I8FAo5J17BlJCXUwtI6wEFkMKwXPctOdiWOYY2h5F4S01vADA4jbKi4wYNvW87o5la-Y3Yx"
}

    response = requests.get(url, headers=headers)

    print(response.text)
   





main()
