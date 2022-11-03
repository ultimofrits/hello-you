#Importing the time module
from re import A
from secrets import choice
from time import sleep 
import time 
import sys

def lprint(s):
    for c in s: 
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.01)
    print("")
    sleep(0.01)

#partone
def partone():
    lprint("7th of december  year 1050")
    lprint("That morning you woke up and heard bombs going off")
    lprint("its nothing out of the usual")
    lprint("the land of Riverdale has been at war for countless years now. ")
    lprint("But today is different, today is your birthday, but as the sound of the explosions get closer and closer you get worried")
    lprint("not that the party would have to be cancelled (there hasnt been a party in this land for decades).")
    lprint("No no the dam near your house has been extremely vulnerable lately. ")
    lprint("You decide that it is finally time to move, but the journey will be long and dangerous. ")
    lprint("There are only 2 options since in the west and east there are oceans, the first of option is the underground kingdom of morhdor in the north")
    lprint("the dwarves are in control there,  and in the south the jungle kingdom of arandale wich is property of the elves.")
    lprint("I wish you good luck adventurer, may you travel safely")
    lprint("Do you want to travel north or south?")
    lprint("A: north, B: south")
    
    choice = input()
    if choice == 'A' :
        lprint("you have chosen morhdor, good luck with the dwarves.")
        partthree()

    elif choice == 'B' :
        lprint("so arandale it is, the elves will welcome you.")
        parttwo()


#arandale
#parttwo
def parttwo():
    lprint("You have been traveling for the past couple of days")
    lprint("arandale is far away and you start to run out of food.")
    lprint("The elves are known for their hospitality but you are probably not going to make it")
    lprint("you must decide to put some of your morals aside and start hunting and gathering")
    lprint("what do you decide to do first?")
    lprint("A: hunt wild animals? B: gather berries and other plants?")
    
    choice = input()
    if choice == 'A' :
        lprint("smart, you now have enough food for a long time!")
        partsix()
    elif choice == "B":
        lprint("that isn’t the best choice, some berries are poisonous and you get sick  OOF!")
        partseven()


#morhdor
#partthree
def partthree():
    lprint("Morhdor will be difficult and very annoying")
    lprint("the dwarves live underground in deep tunnel systems")
    lprint("but first you will have too cross the black mountain")
    lprint("there are 2 paths one is safer but takes a lot longer and the other is more dangerous but will take almost no time compared to the other")
    lprint("A: choose the easier but longer path, B: choose the dangerous but short path ")
    
    choice = input()
    if choice == 'A' :
        lprint("you are already worrying of running out of food. ")
        partfour()
    elif choice == 'B':
        lprint("are you skilled enough to pass safely. ")
        partfive()
    
#morhdor
#partfour

def partfour():
    lprint("You have been traveling for days now and there seems to be no end to the endless tunnels")
    lprint("There is nothing to eat or drink, and the stones are cold.")
    lprint("You start wandering if it was the right path")
    lprint("maybe it would be wise to return and take the faster path? ")
    lprint("A: keep going, the tunnels cant keep going forever!")
    lprint("B: return and hope that the other path is a better choice")
    
    choice = input()
    if choice == 'A' :
        lprint("a light FINNALY!")
        partten()
    elif choice == 'B' :
        deadendv5()
    
def deadendv5():
    lprint("YOU DIED")
    partone()

def partfive():
    lprint("The decision to take the shorter path was made out of fear for dying by starvation")
    lprint("but now you realise that starvation isn’t the thing that is going to kill you, these mountains are!")
    lprint("The mountain roads are narrow and twisty and you must be carefull, and then…")
    lprint("The path stops, you see the remains of a wooden bridge")
    lprint("then you think that you can maybe just jump across! What do you do?")
    lprint("A: jump across the ravine and hope that you make it")
    lprint("B: try to rebuild the wooden bridge")
    
    choice = input()
    if choice == 'A' :
        lprint("1…2….3 AND JUM- oh nooo you didnt make it but you fell on a ledge, good luck making it back up!")
        parteight()
    elif choice == 'B' :
        lprint("it took you a while but the bridge is rebuild and you can keep going on your journey!")
        partnine()

    #arandale
    #partsix
def partsix():
    lprint("On your journey to find the elves you find an abanded cave with an minecart track in it, where could this lead??")
    lprint("A: jump on the minecart and see where it goes")
    lprint("B: leave it alone and keep looking for the elves")

    choice = input()
    if choice == 'A':
        lprint("as you keep riding the minecart you hear music louder and louder")
        lprint("the dwarves liked music you think to yourself….")
        partten()
    elif choice == 'B':
        lprint("after weeks of traveling you finally see the jungle in the distance!")
        parttwelve()

    #arandale
    #partseven

def partseven():
    lprint("This wasteland is endless, you ran out of food 2 days ago and are really hungy")
    lprint("luckily you brought some books along on your journey")
    lprint("maybe there is something in there that might help you?")
    lprint("A: you waste time and energy too look through your books for a solution")
    lprint("B: you forget about the idea and decide to keep traveling")
    choice = input()
    if choice == 'A' :
        lprint("you find a book about the wasteland that you are in, apparently there are snakes that you can eat. ")
        parteleven()
    elif choice == 'B' :
        lprint("since you ran out of food your energy has quickly diminished to nothing.")
        deadendv2()

def deadendv2() :
    lprint("YOU DIED")
    partone()

#morhdor
#parteight

def parteight():
    lprint("You have been stuck on this ledge for days.. ")
    lprint("there is no way to get out other than the steep climb back up or the void down… you must do something though")
    lprint("A: wait until someone rescues you")
    lprint("B: climb back up")
    choice = input()
    if choice == 'A':
        lprint("nobody came and three more weeks passed")
        deadendv1()
    elif choice == 'B':
        lprint("the climb was long and tough but you can already see the top!")
        partnine()
#deadendv1 
def deadendv1():
    lprint("YOU DIED")
    partone()

#morhdor
#partnine

def partnine():
    lprint("The journey didnt take much longer and you can already hear the drums and the music of the dwarves, you are doing great!")
    lprint("A: keep going towards the music")
    lprint("B: wait.. maybe the dwarves are not so friendly!")
    choice = input
    if choice == 'A':
            lprint("you can see them…!")
            partthirteenv2()
    elif choice == 'B':
            lprint("you waited for longer and didnt want to go back and ran out of food.")
            deadendv1()

#morhdor
#partten

def partten():
    lprint("The tunnels kept going for a lot longer then you thought but after a while you reached the end and walked back out into the sun shine")
    lprint("You see a roadsign wich says: longbeards go LEFT and shortnecks go RIGHT")
    lprint("these are the 2 different types of dwarves, the first are known for their hospitality and fun music")
    lprint("the second are known for their craftsmanship and handywork")
    lprint("You must now choose between them")
    lprint("A: choose for the longbeards")
    lprint("B: choose for the shortnecks")

    choice = input()
    if choice == 'A':
            lprint("the longbeards welcomed you into their home and you are now safe!")
            partthirteenv2()
    elif choice == 'B':
            lprint("the shortnecks dont like strangers and killed you with their sharp swords and knifes.. OUCH!")
            deadendv1()
#arandale
#parteleven

def parteleven():
    lprint("The book advices you to kill the snakes and eat their meat, but the snakes live underground")
    lprint("so you have to get them up to the surface. How do you do this?")
    lprint("A: you poke a wooden stick in the ground in hope that the snakes will surface")
    lprint("B: you jump on the ground in hope that the snakes will surface")

    choice = input()
    if choice == 'A':
        lprint("OH NO, a snake surfaced and its massive! It ate your stick and you must now run")
        partelevenpointfive()
    elif choice == 'B':
        lprint("a small snake surfaced and you easily killed it with the stick that you didnt use. Great Job!!!")
        parttwelve()

def partelevenpointfive():
    lprint("")








