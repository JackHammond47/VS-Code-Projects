explanation1 = 'This is a game of choices. You will be given a scenario and options to choose from.'
explanation2 = 'Each choice will be in all CAPS, type your choice to move forward. Good luck.'
intro1 = 'It\'s nightime and your car breaks down in the middle of a tiny town.'
intro2 = 'The only buildings that are close by are a gas station to your LEFT and the police station on your RIGHT.'
intro3 = 'Where do you go? '
bad_input = 'That is not a valid response. The program will now end.'
gas1 = 'The gas station door opens easily, but no one is behind the counter. '
gas2 = 'Looking through the aisles for anyobdy else you hear a crash behind you. '
gas3 = 'You turn around and see a man with an axe jumping out of the air vent. '
gas4 = 'Quick, no time to think! RUN, HIDE, or FIGHT? '
run1 = 'You sprint out of the store and there aren\'t many places to go.'
run2 = 'Are you going to run to your CAR or run down the ROAD?'
car1 = 'You jump in and lock the doors, the man is running towards you. '
car2 = 'You shove the keys in the ignition but the engine won\'t turn over.' 
car3 = 'Suddenly hands grab you from behind, where they were hiding in the backseat.'
car4 = 'The world fades to black as you see the axe man smiling. THE END.'
road1 = 'You sprint like you never have before in your life.'
road2 = 'You look back and see the man staring at you while another man comes out of your car and watches you.'
road3 = 'Running into the night, you have escaped the danger.'
hide1 = 'You jump behind one of the shelves and hold your breath.'
hide2 = 'He starts walking closer, you can hear his axe dragging on the ground.'
hide3 = 'Will you try to CRAWL away and escape, or DUCK into the nearby locker? '
crawl1 = 'You silently creep forward on your hands and knees and then bolt out the door.'
crawl2 = 'You glance back and expect to see him right behind you, but he is staring at you from the gas station doorway.'
crawl3 = 'You sprint off down the road, you have escaped the danger.'
duck1 = 'You silently walk back to the employee locker at the back of the store and duck inside.'
duck2 = 'You hear the man walk past and let out the breath you\'ve been holding.'
duck3 = 'Suddenly the door is wrenched open and you see the axe flying towards you. THE END.'
fight1 = 'Grabbing a beefy ice scraper off the shelf, you swing hard at the man, who falls to the ground unconscious.'
fight2 = 'Breathing hard you see two figures walking towards the front door.'
fight3 = 'Will you DASH towards the back door and make a break for it or ATTACK the approaching figures? '
dash1 = 'Running out the back door you sprint off down the road into the night.'
dash2 = 'The figures stand far behind you as you keep running, you have escaped the danger.'
attack1 = 'Full of adrenaline and confidence you sprint towards the two figures, an ice scraper in each hand.'
attack2 = 'They step into the light and you see that they are not alone.'
attack3 = 'Behind the cars a group of eight armed with hatches and knives joins the pair.'
attack4 = 'Panicking to decide your next move, you feel a dart land on your chest.'
attack5 = 'The world goes fuzzy and starts to spin wildly, before you know it you are on the ground.'
attack6 = 'Trying to stay lucid, the world fades to black as the spinning faces of the strangers surround you. THE END.'
police1 = 'As you walk towards the police station, the door opens and a frightened looking man and woman tell you to run inside. '
police2 = 'The man, John, is a sheriff\'s deputy and the woman is a receptionist named Martha. '
police3 = 'They explain that people wielding axes attacked the town and they locked themselves in the police station. '
police4 = 'John says they should grab the guns and fight back, while Martha insists they stay sheltered at the station. '
police5 = 'Do you agree with JOHN or MARTHA? '
john1 = 'Despite Martha\'s protest, you side with John and choose to fight back.'
john2 = 'Just as you all get loaded up you see a group of three outside the side door, armed with hatchets and knives, through the '
john3 = 'security cameras.'
john4 = 'You open the door to start fighting when a large group jumps on you from the darkness, it was a trap!'
john5 = 'Do you try to ESCAPE or BATTLE the armed group? ' 
escape1 = 'You and Martha manage to shove off your attackers and sprint back into the station.'
escape2 = 'You run towards the front doors as you hear John fighting back.'
escape3 = 'You and Martha keep running down the road in fear and you look back towards the station.'
escape4 = 'John didn\'t make it, but as for you and Martha, you have escaped the danger.'
battle1 = 'Shoving the man off of you, you shoot his hand and he drops the kinfe in pain.'
battle2 = 'John starts shooting at the group and Martha runs back towards the station.'
battle3 = 'You raise your gun to help John when you feel a blow to the back of your head.'
battle4 = 'Falling to the ground, you slip into unconsciousness. THE END.'
martha1 = 'You agree with Martha and all three of you stay locked up at the police station.'
martha2 = 'After about half an hour you hear a bang.' 
martha3 = 'Looking at the security cameras, you see a group of six people walking into the station after breaking down a side door.'
martha4 = 'You can either bunker down in the evidence locker or grab a car from the garage and attempt to drive away.'
martha5 = 'Will you go to the LOCKER or to the GARAGE? ' 
locker1 = 'You run with John and Martha into the highly secure evidence locker and lock the door from the inside.'
locker2 = 'After a few minutes of terrifying silence, a small cylinder rolls in front of the door.'
locker3 = 'Smoke starts to escape the object and the fumes make you sleepy.'
locker4 = 'You see people climbing into the room from the air vent in the ceiling as you fight to stay awake.'
locker5 = 'Despite fighting the feeling you all drift off as the strangers surround you. THE END.'
garage1 = 'You all sprint into the police garage, John grabs the keys while Martha hits the "open door" button.'
garage2 = 'Jumping in the car, you three speed out of the garage, narrowly missing a man with a hatchet.'
garage3 = 'Driving off into the night, as far from the town as possible, you have escaped the danger.'
secret1 = 'You have bad feeling about this place, so you just keep running down the road.'
secret2 = 'Better to lose your car than your life, you have escaped the danger.'
secret3 = 'Congrats on unlocking the SECRET ENDING.'

print(explanation1)
print(explanation2)
print('')
print(intro1)
print(intro2)
choice_1 = input(intro3)
print('')

if choice_1.lower() == 'left':
    print(gas1)
    print(gas2)
    print(gas3)
    choice_2a = input(gas4)
    print('')
    if choice_2a.lower() == 'run':
        print(run1)
        choice_3a = input(run2)
        print('')
        if choice_3a.lower() == 'car':
            print(car1)
            print(car2)
            print(car3)
            print(car4)
        elif choice_3a.lower() == 'road':
            print(road1)
            print(road2)
            print(road3)
        else:
            print(bad_input)    
    elif choice_2a.lower() == 'hide':
        print(hide1)
        print(hide2)
        choice_3b = input(hide3)
        print('')
        if choice_3b.lower() == 'crawl':
            print(crawl1)
            print(crawl2)
            print(crawl3)
        elif choice_3b.lower() == 'duck':
            print(duck1)
            print(duck2)
            print(duck3)
        else:
           print(bad_input) 
    elif choice_2a.lower() == 'fight':
        print(fight1)
        print(fight2)
        choice_3c = input(fight3)
        print('')
        if choice_3c.lower() == 'dash':
            print(dash1)
            print(dash2)
        elif choice_3c.lower() == 'attack':
            print(attack1)
            print(attack2)
            print(attack3)
            print(attack4)
            print(attack5)
            print(attack6)
        else:
          print(bad_input)  
    else:
       print(bad_input) 
elif  choice_1.lower() == 'right':
    print(police1)
    print(police2)
    print(police3)
    print(police4)
    choice_2b = input(police5)
    print('')
    if  choice_2b.lower() == 'john':
        print(john1)
        print(john2)
        print(john3)
        print(john4)
        choice_3d = input(john5)
        print('')
        if choice_3d.lower() == 'escape':
            print(escape1)
            print(escape2)
            print(escape3)
            print(escape4)
        elif choice_3d.lower() == 'battle':
            print(battle1)
            print(battle2)
            print(battle3)
            print(battle4)
        else:
            print(bad_input)
    elif  choice_2b.lower() == 'martha':
        print(martha1)
        print(martha2)
        print(martha3)
        print(martha4)
        choice_3e = input(martha5)
        print('')
        if choice_3e.lower() == 'locker':
            print(locker1)
            print(locker2)
            print(locker3)
            print(locker4)
            print(locker5)
        elif choice_3e.lower() == 'garage':
            print(garage1)
            print(garage2)
            print(garage3)
        else:
            print(bad_input)
    else:
        print(bad_input)
elif choice_1.lower() == 'run':
    print(secret1)
    print(secret2)
    print(secret3)
else:
    print(bad_input)







