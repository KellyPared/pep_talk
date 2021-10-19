import random

first_part = [
    "Fact:",
    "Everybody says",
    "Check it,",
    "Just saying",
    "Superstar",
    "Self,",
    "Know this,",
    "News alert",
    "Ace,",
    "Excuse me but",
    "Experts agree",
    "In my opinion",
    "Hear ye, hear ye",
    "Okay, listen up:",
]

second_part = [
    "the mere idea of you",
    "your soul",
    "your hair today",
    "everything you do",
    "your personal style",
    "every thought you have",
    "the sparkle in your eye",
    "your presence here",
    "your life's journey",
    "that saucy personality",
    "your DNA",
    "the way you roll",
    "whatever your secret is,",
    "all of ya'll",
]

third_part = [
    "has serious game",
    "rains magic,",
    "deserves the Nobel Prize",
    "raises the roof,",
    "breeds miracles",
    "is paying off big time",
    "shows mad skills",
    "just shimmers",
    "is a national treasure",
    "gets the party hopping",
    "is the next big thing",
    "roars like a lion",
    "is a rainbow factory",
    "is made of diamonds",
    "makes birds sings",
    "should be taught in school",
    "makes my world go around",
    "is 100% legit,",
]

fourth_part = [
    "24/7.",
    "and that's a fact.",
    "so treat yourself.",
    "that's just science.",
    "would I lie?",
    "for reals.",
    "mic drop.",
    "you hidden gem.",
    "- period.",
    "now let's dance.",
    "high five.",
    "say it again.",
    "according to CNN.",
    "so get use to it.",
]

print("Are you feeling under the weather?")
while True:
    intro_ques = input("Do you need a little pep talk?").lower()
    if intro_ques == "yes":
        p1 = random.choice(first_part)
        p2 = random.choice(second_part)
        p3 = random.choice(third_part)
        p4 = random.choice(fourth_part)
        print("*".center(30, "*"))
        print(p1, p2, p3, p4)
        print("😀".center(10, "😀"))
        input()
        more_ques = input("Feel better?").lower()
        if more_ques == "no":
            continue
        else:
            break
    else:
        break
