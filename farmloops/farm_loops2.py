# !/usr/bin/env python3


def main():

# create farms dictionary

    farms = [{"name": "North East Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "West Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "South East Farm", "agriculture": ["chickens", "carrots", "celery"]}]

    for farm in farms:
        print("-", farm["name"])
    choice= input("Pick a farm!\n").title()
    if choice == "North East Farm":
        print(', '.join(farms[0]["agriculture"]))
    elif choice == "West Farm":
        print(', '.join(farms[1]["agriculture"]))
    elif choice == "South East Farm":
        print(', '.join(farms[2]["agriculture"]))
    else:
        print("Hmmm... That doesn't seem to be part of our portfolio, but we hope to expand soon. Follow us on social media to keep up with our expansion.")


main()

