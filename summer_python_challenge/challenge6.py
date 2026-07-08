feeling = input("How are you feeling?\n> ")

if feeling.lower() == "good":
    print("Glad you are feeling well!")
elif feeling.lower() == "ok":
    print("Keep going, school is almost over!")
elif feeling.lower() == "sad":
    print("Sorry you are not happy today.")
else:
    print("Sorry, I don't understand that feeling.")