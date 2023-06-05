print("Hi! Welcome to the MadLibs game developed by UNSW Computer Science student Wilson Ji z5417102 \nTo start off, please choose one of the following: ocean, forest \nPlease note that all answers in this game are case-sensitive.")

#repeat = False

#while repeat == False
location = input("Enter a location: ")

while location != "ocean" and location != "forest":
    print('You did not enter one of the given choices. Please try again.')
    location = input()

print("Great! Now let's choose a celebrity out of: Kanye West, Kim Kardashian")

celebrity = input("Enter a celebrity: ")

while celebrity != "Kanye West" and celebrity != "Kim Kardashian":
    print("You did not enter a valid celebrity name! Please try again.")
    celebrity = input()

print("Okay, now finally, choose a verb from the following: shopping, gossiping")

verb = input("Enter a verb: ")

while verb != "shopping" and verb != "gossiping":
    print("You did not enter a valid verb! Please try again.")
    verb = input()

print("You're done! Here we go...")

if location == "ocean":
    if celebrity == "Kanye West":
        if verb == "shopping":
            print("One day, " + celebrity + " woke up and was like, 'Wow! I need to go " + verb + " for some milk!' and so he went swimming in the " + location + " and never came back.")
        if verb == "gossiping":
            print("BREAKING NEWS! " + celebrity + " caught " + verb + " about Frank " + location + ".")
    if celebrity == "Kim Kardashian":
        if verb == "shopping":
            print(celebrity + " woke up one day and chose violence. So she out " + verb + " for a whole damn " + location + ".")
        if verb == "gossiping":
            print("Once again, " + celebrity + " is caught " + verb + " about her new baby daddy while vacationing in the Pacific " + location + ".")
if location == "forest":
    if celebrity == "Kanye West":
        if verb == "shopping":
            print("For some reason " + celebrity + " thought it would be funny to go " + verb + " in the " + location + ". He never returned.")
        if verb == "gossiping":
            print("After hearing that " + celebrity + " likes to go to the bathroom in " + location + "s, people started " + verb + " about his behaviour.")
    if celebrity == "Kim Kardashian":
        if verb == "shopping":
            print(celebrity + " has stated that she never plans to go " + verb + " in the " + location + ", as lots of disappearances occur there.")
        if verb == "gossiping":
            print("Whenever " + celebrity + " is bored, her favourite activity to do is gather her friends in the " + location + " and go " + verb + " about Kanye West's disappearance.")

#repeatq = input("Would you like to play again? Yes/No")

#if repeatq == "Yes":
#    repeat == True



