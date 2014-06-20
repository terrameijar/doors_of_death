""" 
        A text based game that I'll be building progresively as my knowledge of 
        the Python language improves.
        @terrameijar
"""        


from sys import exit



def medussa_room():
    clear()
    print "Welcome human. You have entered Medussa's lair. Prepare to die"
    print "Medussa has heard you come in and she's slowly making her way towards you."
    print "You can hear her body slithering across the floor. What do you do?"
    
    
    action = raw_input(">  ")
    
    
    
    if "run" in action:
        print "Good thinking, you were not going to survive that anyway."
        print "Taking you back out now...."
        run_out()
    
    elif "close my eyes" in action:
        dead("yeah...close your eyes? Like that has ever worked before")
    
    elif "talk to her" in action:
        dead("Yeah like that would really work")
    
    else:
        print "Medussa is smarter than that, she looks into your eyes and turns you to stone. Way to go! "
        again = raw_input("Do you want to have another go with Medussa? :Y/N___ ")
        print again
        if "Y" or "y" in again:
            medussa_room()
            
        elif "N" or "n" in again:
            start()
        
        else:    
            dead("Medussa turns you to stone")
        
def giant_plant():
    clear()
    print "Giant plant Room"
    print "You've entered the green room. Here, in the middle of the room is a big plant with a bulb"
    print "This plant looks foreign and strange. Suddenly, its head turns toward you as you walk in"
    print "You realise that this plant has sensed you presence in the room"
    print "What will you do?"
    
    
    action = raw_input(">  ")
    
    if "run" in action or "walk" in action:
        print "Good job. You got away"
        run_out()

    elif "cut" in action:
        print "You try to cut the plant"
        dead("this is a man eating plant, it's designed to kill.")
    
    else:
        print "You have to try something else or you'll die"
        #been_here_before = true
        giant_plant()
        
        
        
    
    
    
def ghost_freak():
    clear()
    print "i'm the ghost freak room"
    print "You walk into a room and you see a white Ghost with an upside down head."
    print "You recognise this to be Ghost-Freak. Your fate is sealed."
    dead("You have been possessed")
    


# This is a text based game that presents the user with options and asks them to 
# respond.

def start():
    #print "I'm the start module"
    clear()
    print "You've walked into a dark room, with 3 doors, each door leads to your death."
    print "Decide here and now how you would like to die"
    print "Pick a door. The doors are numbered 1 through 3"
    
    #door = int(raw_input("Door number: "))
    door = ""

    # try for a non int exception
    try:
        door = int(raw_input("Door number: "))
    #I've added this try -except statement here...start working from la
    
        #action = raw_input(">  ")
        
    except:
        print "Please Enter a valid number between one and three"
        start()
    
    if door == 1:
        medussa_room()
    
    elif door == 2:
        giant_plant()
    
    elif door == 3:
        ghost_freak()
        
    #This is for numbers less than 0 or greater than 3
    else:
        print "please select a door between 1 and 3"
        print ""
        print ""
        start()
    
    print door    
    
def run_out():
    clear()
    print "Run out module"
    start()
    
    
def dead(why):
    clear()
    print "You're dead, %s" %(why)
    ans = raw_input("Do you want to go again? Y/N___")
    
    if "Y" in ans or "y" in ans:
        #print "You're in the Yes/y if statement"
        start()
    else:
        print "Goodbye!! \a"
        exit(0)    

#add more flesh to the functions 
#it would be great if i could use switch-case statements to limit the user's responses

def clear():
    print ""
    print ""

start()        
        
        
