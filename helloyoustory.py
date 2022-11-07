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

#functie aanroepen
#calling partone

partone()


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
        deadendv1()
#morhdor
#part five

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
        deadendv1()



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
    lprint("do you want to play again?")
    lprint(" A: yes, B: no")
    choice = input()
    if choice == 'A':
        lprint("starting a new game...")
        partone()
    elif choice == 'B':
        lprint("closing game")


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

#arandale
#partelevenpointfive

def partelevenpointfive():
    lprint("As you run you must decide turn around too face and fight the massive snake or do you keep running towards the elves")
    lprint("maybe they will save you. ")
    lprint("A: fight the snake")
    lprint("B: keep running")

    choice = input()
    if choice == 'A':
        lprint("you idiot, the snake is far too strong… ")
        deadendv1()
    elif choice == 'B':
        lprint("in the distance you see mythical beings, THE ELVES!")
        partthirteenv1()

#arandale
#parttwelve
def parttwelve():

    lprint("As you travel you find a path")
    lprint("it looks well made and used. This might be the main road too the elves you think to yourself.")
    lprint("But in the back of your mind you know this might be the great highway of the orcs… ")
    lprint("orcs are unfriendly creatures with big wooden bats as weapons, they wonder around in groups of over a hundred")
    lprint("they dont like others or those who use their path, you there by stand before a decision")
    lprint("A: stay off the path too avoid possible orcs")
    lprint("B: get on the path and make sure that you wont get lost on your journey to find the elves")
    
    choice = input()
    if choice == 'A':
        lprint("the path turned out to be a orc highway, SMART THINKING!")
        partthirteenv1()
    elif choice == 'B':
        lprint("after a couple of hours you hear rumbling in the distance, you try to get off the path as soon as you can but it was too late.")
        lprint("The orcs came and took you to one of their labour camps. ")
        deadendv1()
#arandale
#part thirteen v1

def partthirteenv1():
    lprint("Congratulations! You have made it too the kingdom of arandale and the elves are looking forward too meeting you.")
    partfourteen()

#morhdor
#part thirteen v2
def partthirteenv2():
    lprint("Congratulations! You have made it too the kingdom of morhdor and most of the dwarves are looking forward too meeting you.")
    lprint("Your new objective is too not only survive but too also thrive in the kingdom of morhdor. ")
    parttwentyone()

#arandale
#part fourteen
def partfourteen():
    lprint("As you wake up you see tall creatures with wings, one of the elves gives you a cup of tea.")
    lprint("She says that it is good for your health.")
    lprint("Than the tribe leader shows up, you know this because they are wearing a huge crown and very expensive looking robes.")
    lprint("“welcome to Arandale” she says. ")
    lprint("Your new objective is still survive but also to thrive in the elven kingdom of arandale. ")
    partfifteen()

#arandale
#part fifteen
def partfifteen():
    lprint("After a couple of days pass, you start to realise that the elven kingdom isnt the paradise you thought it would be.")
    lprint("For one, most of them are female, the male counter parts are only seen very rarely and are mostly the hunters. ")
    lprint("The female elves want you too join the males in their hunting")
    lprint("you realise that this will get you the respect you need as a stranger and a human in this elven land. ")
    lprint("But hunting is dangerous in the jungle do you go with them? ")
    lprint("A: yes, I will help them")
    lprint("B: no, I have already been through enough, I will not risk my life again! ")
    choice = input()
    if choice == 'A':
        lprint("very nice of you, the elves will feed you and give you the respect you deserve. ")
        partsixteen()
    elif choice == 'B':
        lprint("that isnt very nice.")
        partseventeen()
    
#arandale
# part sixteen
def partsixteen():
    lprint("The elves appreciate you for helping them gather food")
    lprint("in return they have been giving you free healthcare. ")
    lprint("But there is a dangerous side too this choice. ")
    lprint("The elves have been forcing you too hunt for a certain type of bird")
    lprint("now the elves themselves have bows and arrows but you dont own any weapons apart from a sharp wooden stick…")
    lprint("after a while of this struggle you went to the tribe leader and got given the option too enrole as a healer do you take the job offer?")
    lprint("A: no I would rather hunt, hunters get more respect anyways")
    lprint("B: yes I am done hunting those stupid birds")
    choice = input()
    if choice == 'A':
        lprint("interesting choice….")
        parteightteen()
    elif choice == 'B':
        lprint("smart,  This might save your life!")
        partnineteen()
    
#arandale
#part seventeen
def partseventeen():
    lprint("After your very dumb choice of not helping the other elves the tribe leader has kicked you out of their territory")
    lprint("You will now have to life the rest of your miserable life out in a little hut in the middle of the jungle")
    lprint("hoping one day that you might be able to return too your homeland of riverdale. ")
    endgame()

#arandale 
#endgame

def endgame():
    lprint("you have completed the game")
    lprint("do you want too play again?")
    lprint("A: yes, B: no")
    choice = input()
    if choice == 'A':
        lprint("starting game...")
        partone()
    elif choice == 'B':
        lprint("closing game")

#arandale
#parteightteen

def parteightteen():
    lprint("Since you choose to keep hunting you only caught 1 bird.")
    lprint("The tribe leader isnt very happy with your efforts and orders you too catch atleast 2 more in the next week. ")
    lprint("Do you try harder and take more risks while hunting or do you simply steal from the others to make your goal. ")
    lprint("A: you steal from the others to reach your goal")
    lprint("B: you try harder and take more risks while hunting")
    choice = input()
    if choice == 'A':
        lprint("you have succesfuly stolen 2 birds from the others")
        partnineteen()
    elif choice == 'B':
        lprint("while hunting you tried to catch a bird with your bare hands but fell out of a tree")
        deadendv1()

#arandale
#part nineteen

def partnineteen():
    lprint("The tribe leader is very happy with your efforts and has seen that you have improved")
    lprint("she now wants you to catch 3 more in the next 3 days")
    lprint("A: keep stealing and hope that they dont find out")
    lprint("B: tell the tribe leader that you stole the first 2 birds")
    choice = input()
    if choice == 'A':
        lprint("your lie held up and you are now granted some freedom in the village")
        parttwenty()
    elif choice == 'B':
        lprint("the tribe leader did not that your confession well and ordered your execution. ")
        deadendv1()
#arandale
#part twenty

def parttwenty():
    lprint("After you stole all the birds the tribe handed you some better equipment.")
    lprint("With that equipment you caught more and more birds and You are now successful in the kingdom of arandale and are allowed more freedom in the country. ")
    lprint("Good job!")
    endgame()

#morhdor
#parttwenty one

def parttwentyone():
    lprint("After you survived your dangerous journey through the mountains and caves you have made it into the land of morhdor")
    lprint("the dwarves dont like strangers but are forgiving for mistakes. ")
    lprint("The longbeards are always busy so they dont have much time for you, try to not offend them aswell…")
    lprint("The tribe leader of the dwarves wants you too go mining and collect resources for them, will you do that? ")
    lprint("A: yes I will help them collect resources")
    lprint("B: no I need to rest")
    choice = input()
    if choice == 'A':
        lprint("you go with the rest down into the mines")
        parttwentythree()
    elif choice == 'B':
        lprint("the dwarves prefer hard working people")
        parttwentytwo()

#morhdor
#part twenty two

def parttwentytwo():
    lprint("The dwarves have taken a disliking in you after you didnt want to work for them")
    lprint("but they have given you a chance to prove yourself again")
    lprint("in the way of making simple tools, do you start making the tools?")
    lprint("A: no ofcoure not I need more rest. ")
    lprint("B: yes I will help them")
    choice = input()
    if choice == 'A':
        lprint("the dwarves have kicked you out of their kingdom, you ran out of food and died")
        deadendv1()
    elif choice == 'B':
        lprint("the dwarves are happy with you again.")
        parttwentyfive()

#morhdor
#part twenty three

def parttwentythree():
    lprint("The dwarves like hard working people and are very impressed with your efforts")
    lprint("they are now giving you a job offer for more dangerous but also rewarding")
    lprint("work deeper down in the mines, do you go for it?")
    lprint("A: yes I take the job")
    lprint("B: no I would like to stay alive")
    choice = input()
    if choice == 'A':
        lprint("after an accident in the mines you got extremely wounded, you shortly died in a hospital ")
        deadendv1()
    elif choice == 'B':
        lprint("your popularity didnt increase but after an accident in the mines you realized that that was the right choice!")
        parttwentyfour()

#morhdor
#part twenty four

def parttwentyfour():
    lprint("You are successfully thriving in the dwarven economy and will live happy and prosperous.")
    endgame()

#morhdor
#part twenty five

def parttwentyfive():
    lprint("You are successfully thriving In the dwarven economy and will live happy and prosperous. ")
    endgame()