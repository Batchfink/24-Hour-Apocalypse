""" The story line for an adult. """

import os
import random
from Utils import *
import time
import datetime
import Player

def weekend(player):
    os.system("cls")
    print ("As your eyes slowly open, you drift in and out of consciousness, wishing for yourself to fall back asleep.")
    input()
    os.system("cls")
    print ("You look towards your clock, it reads 8:30. 8:30 is not your usual awakening time.")
    input()
    os.system("cls")
    print ("Upon further inspection, you notice that it's the weekend. You slept all through Friday. Wierd.")
    input()
    os.system("cls")
    print ("You vaguely remember the smashing party you had, and how drunk you'd gotten.")
    input()
    os.system("cls")
    print ("After sliding out of bed, you put on a shirt and walk into the kitchen.")
    input()
    os.system("cls")
    print ("Here, it comes to your attention that somebody is knocking on the door. And has been for the last 4 minutes.")
    input()
    os.system("cls")
    print ("You decide to answer them, but at 8:30 in the morning, they could just be someone drunk.")
    input()
    os.system("cls")
    print ("You peer through your peep hole. You see a tall male, with a... deformed face.")
    input()
    os.system("cls")
    print ("\"Nice makeup!\" You shout through the door. No response.")
    input()
    os.system("cls")
    print ("You turn around after locking the door. The banging resumes.")
    input()
    os.system("cls")
    if player.gender == "f":
        print ("You decide to get changed, so you take off your shirt and put on a bra, a jacket and a skirt.")
    elif player.gender == "m":
        print ("You decide to get changed, so you take off your shirt and put on some underwear, a jumper and a pair of jeans.")
    else:
        print ("You decide to get changed, so you take off your shirt and put on a bra, some underwear, a skirt and a pair of jeans.")  # xD   if this is possible I s'pose
    input()
    os.system("cls")
    print ("")
