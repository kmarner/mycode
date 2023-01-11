#!/usr/bin/env python3


def main():

# create farms dictionary

    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

    for items in farms:
        print(f"Please come see us at the {items['name']} to visit with all the {','.join(items['agriculture'])} that call this place home!")


main()

