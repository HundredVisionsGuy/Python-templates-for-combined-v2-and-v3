# LetItRoll.py
# by Chris Winikka
# Based on Let It Roll Activity

import random

BigDice = [0
    [
        "What is the most important thing you own?",
        "What is your favorite flavor of ice cream?",
        "What is your favorite subject in school?",
        "What games do you like to play?",
        "What is something you would like to buy?",
        "What is your favorite television show?"
    ],
    [
        "What are you most proud of?",
        "Who is your role model?",
        "What is your happiest memory?",
        "What is your favorite movie?",
        "What is your favorite type of food?",
        "What is your favorite song?"
    ],
    [
        "Who is the bravest person you know?",
        "What do you want to be when you are older?",
        "What is one thing you like about yourself?",
        "Who is your best friend?",
        "What is something you would like to learn?",
        "Do you have a pet? If so, what type?"
    ],
    [
        "What kind of music do you like?",
        "What is your favorite book?",
        "What makes you unique?",
        "Where would you like to travel?",
        "What is one thing you cannot live without?"
    ],
    [
        "If you were an animal, what would it be?",
        "Who is the athlete you admire the most?",
        "Describe your perfect day",
        "What superpower would you like to have?",
        "Who is your favorite actor/actress?",
        "What makes you happy?"
    ],
    [
        "What is your favorite sport?",
        "What is your favorite type of cookie?",
        "What do you like to do in cold weather?",
        "What do you like to do in warm weather?",
        "What was your favorite cereal growing up?",
        "What holiday do you like the most?"
    ]
]

while True:
    bigDie = random.randrange(6)
    littleDie = random.randrange(6)
    pick = BigDice[bigDie][littleDie]

    raw_input("Press enter to get your question: ")
    print("\n" + pick)

    another = raw_input("\nWould you like another question? ")
    if another:
        if another[0].lower() != "y":
            break
