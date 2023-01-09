#!/usr/bin/env python3

import time 

def main():

    bottles= int(input("How many bottles would you like? Lets think moderation. No more than 100 bottles. I mean it.\n"))


    if bottles > 100:
        print("That's a bit excessive...")
    
    elif bottles < 100 > 0:
        print("Let\'s get this party started")
        
    else:
        print("Get it together man! How many bottles have you had???")

    #(start, stop, step)
    for num in range(bottles,-1,-1):
        
        print(num, "bottles of beer on the wall!")
        time.sleep(2)
        print(num, "bottles of beer on the wall!", num, "bottles of beer! You take one down pass it around!")
        time.sleep(2) 

    print("No more bottles of beer on the wall!")
    time.sleep(2)
    print("We should probably get you an Uber. Or do you prefer Lyft?")    


      #  print("bottles of beer on the wall!")



main ()        
