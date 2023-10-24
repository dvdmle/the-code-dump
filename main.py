print("Welcome to the mental health app!")
print()
print("On a scale of 1 to 10, how are you feeling today?")

feelings = 1

while feelings in range(1,11):
    feelings = int(input())

if feelings < 3:
    print("What happened? Would you like to talk about it?")
elif 3 <= feelings <= 8:
    print("Awesome! What's something interesting that happened today?")
else: 
    print("Fantstic! Write 3 things that you are grateful today=> ")

# Guten Tag!
# It's new. 
