print("Welcome to the mental health app!")
print()
print("On a scale of 1 to 10, how are you feeling today?")

feelings = 1

while feelings in range(1,11):
    feelings = int(input())

if feelings < 5:
    print("What happened? Would you like to talk about it?")
else:
    print("Awesome! What's something interesting that happened today?")


