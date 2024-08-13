# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define playa = Character("[playaname]" who_color="#683485")
python:
    playaname = renpy.input("Who are you, little cat?", length=20)
    playaname = playaname.strip()

    if not playaname:
        playaname = "Blep"

playa "I'm [playaname], nyaa!"

define z = Character("Prince Zuko", who_color="#aa3321") #red, "terracotta"
define j = Character("J Neilsen", who_color="#834B32") #brown, "nutmeg"
define c = Character("Charlie", who_color="#557D2A") #green, "crete"?
define b = Character("Blur", who_color="#46ADBB") # blue, "pelorous" ?? wtf are these color names



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room # scene bg paddys_front

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    playa "Wow, it smells delicious in there! And it looks like the door is cracked open too..."

    menu:
        "Should I go in and see what's cooking?"

        "Nyaassss I'm hungie!!":
            $ go_in = True
            "You paw carefully at the door, and it slowly creaks open just wide enough for you to squeeze in. Sweet!"
        "Nyoooo it sounds scawy...":
            $ go_in = False
            "You do not sneak into Paddy's Pub, and therefore go on other kitty adventures not portrayed in this work. Try again, be brave kibbo!"
            return

    # scene bg paddys_forge
    show zuko
    show charlie
    z "Hey, this sword is coming along pretty well! Thanks again for renting your in-house forge to us, Charlie."
    c "Yeah man! Uhhh looks great so far! Hey can you put some of that seasoning on my burger while you're over there?"
    z "Seasoning? Dude, this is flux, it's not for human consu-"
    c "Look Zuk, whatever you call it, that stuff's delicious, put some on my burger for me, it's the one in the back."
    z "Sigh...wait why are you cooking burgers in a steel forge anyway?! Don't you have a grill?"
    c "It's in the shop! And the forge is already hot...man, look, hurry up and put the seasoning on it before it burns!"
    z "It's not seasoning oh my GO-"
    c "JUST HURRY UP AND DO IT MAN DON'T MESS UP MY BURGER!!"
    z "OKAY FINE JUST CALM DOWN WHILE I--"
    "CLAAAAANG!!! BANGBANGbangbangbangbaaaaanggg..."
    c "...uh oh."
    z "Oh NO!! The steel is so burnt, it broke it half when I dropped it..."
    c "Well THAT'S not good...hey you didn't burn the food though did you!?"
    z "Ugh, no your stupid burgers are fine, but I'm gonna be dead meat myself if I don't fix this before-"
    show jay
    j "Hello boys."
    z "Master Neilsen..."
    j "We having fun in here?"
    c "OH YEAH, great time, hey man you want a burger?"
    z "Well..."
    j "Let me guess: you got distracted, burnt your steel, and then broke it, huh?"
    z "...yes sir..."
    j "Eh that's alright, shit happens, nobody got hurt right?"
    c "No we're okay but--HEY WHADDAYA DOING?! Paws off the goods, buddy!"
    "Uh-oh. In all the chaos, you had just managed to sneak up onto the bar next to Charlie's plate, unnoticed before now."
    z "I didn't know you guys had a bar cat."
    c "We don't! I've never seen this cat before in my life! And now it's trying to steal my cheeseburger!" 
    c "Cute lil fella though. Maybe we DO need a bar cat! Do better numbers on some of the rats around here, good for morale..."
    z "That's great, Charlie, but what about my ste-"
    c "Now you can't just be any ol' cat if you want to be the official Paddy's bar cat, you gotta like...go on a quest, prove you're up for the job kind of thing."
    z "Wait a sec...Charlie, I think you're onto something!"
    c "Oh yeah?"
    z "Yeah! Cats are clever and resourceful, but they're also small and agile, excellent at hiding and getting into small spaces."
    c "Well yeah that's why they're always outpacing me at rat catching, but what's your point?"
    z "I need new steel for a billet if I'm gonna make this sword..."
    "You have been munching on Charlie's cheeseburger when Zuko comes over and squats so his face is level with you."
    z "I think we'll call you [playaname] for now. Hey, lil [playaname], you think you can find me some quality steel in this town?"
    z "If you do, we'll adopt you and you can live here, and have all the cheeseburgers you want!"
    c "You gotta put in work here too though, rat catching is a serious job okay?"
    z "Well, if [playaname] can find steel, which doesn't squeak or move or smell like rats do, then surely they'd be an excellent rat catcher!"
    c "Oh yeah Zuk, you got a point! Alright I'm down, let's see what you got [playaname]!"
    j "Well, I'm now VERY certain you're both completely insane, but whatever you gotta do to get that sword made."
    
    menu:
        "Accept the quest to hunt for steel and become the Paddy's bar cat?"
            
        "Nyaaaaas, I loves beezchurger and these humans seem nice!":
            $ accept = True
            "Zuko carefully hangs a small leather bag around your neck."
        "Nyoooooo, these humans are too crazy!!":
            $ accept = False
            "Charlie, mouth covered in flux and ranting about thieves and freeloaders, picks you up and sets you down outside Paddy's before shutting the door tightly."
            return 
   
   
    z "Put what you find in this bag, and if it gets too heavy, you can bring it back here and we'll hang onto it while you hunt for more."
    z "I'm counting on you, [playaname]. Who's a good kitty?"
    "Zuko scritches your head gently, and you purr a little, for you are indeed a good kitty."
    c "Hey you be careful out there, you gotta watch out for dogs and cars and Azula and Gail the Snail..."
    z "Stay safe, [playaname]! We believe in you!"
    "Of course you'll watch out for danger, Philly is dangerous even if you're not a cat."
    "But you're an adventure cat, and you know these streets like the back of your paw."
    "With a flick of your tail, you scurry out the door to begin the hunt."
    # These display lines of dialogue.

   

    # This ends the game.

    return
