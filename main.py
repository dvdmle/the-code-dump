def feelingsTracker():
    print("On a scale of 1 to 10, how are you feeling today?")

    feelings = 0

    while not feelings in range(1,11):
        feelings = int(input())

    if feelings < 3:
        print("What happened? Would you like to talk about it?")
    elif 3 <= feelings <= 8:
        print("Awesome! What's something interesting that happened today?")
    else: 
        print("Fantastic! Write 3 things that you are grateful today=> ")

def sleepWellness():
    sleep_hours = int(input("How many hours of sleep did you get today? "))

    if sleep_hours > 10:
        print("That's a lot of sleep hours! You could probably stand to wake up a bit sooner.")
    elif sleep_hours > 8:
        print("Good! That's a solid amount of sleep.")
    elif sleep_hours > 6:
        print("That's an alright amount. You might consider sleeping in a bit, especially if you're younger.")
    elif sleep_hours > 4:
        print("Okay, you would probably benefit from heading to sleep a bit sooner. Consider opening a window or turning a fan on!")
    else:
        print("That's a concerningly short duration to be asleep. It'd probably be a good idea to take a nap soon.")
        if sleep_hours <= 2:
            print("Additionally, I would recommend speaking to a sleep specialist about this.")

def physicalWellness():
    physical_status = int(input("moving to your physical status, on a range of 1 through 10 how do you feel?"))

    if physical_status >= 10:
        print("That is good, have a good day")
    elif 5 < physical_status < 8:
        print("that is normal, there is discofort once in a while, just remember to look over yourself")
    else:
        issue = input("What seems to be the issue?")
        if issue == "headache":
            print("Lay down for a while, if it happened for a while go to a doctor")
        elif issue == "injury":
            print("if a small bleeding injury, disinfect and cover up, if internal reach medical professional")
        elif issue == "sickness":
            print("maintain a distance and call local medical opinion")
        elif issue == "unknown":
            print("call a doctor for a medical call")
        else:
            print("I am unable to help")


def exit():
    print("Goodbye!")
    print()

print("Welcome to the mental health app!")
print()

# Guten Tag!
# It's new.

# Feelings/diary portion of the program
feelingsTracker()

# Sleep wellness portion of the program
sleepWellness()

# physical wellness portion of program
physicalWellness()

# Says goodbye and exits the program
print()
exit()