import random
from quiz_common import *

def quiz_user_mc(flashcards):

    # initialize scoreboard
    score = 0

    # get number of flashcards
    numCards = get_num_cards(flashcards)

    for idx, flashcard in enumerate(flashcards):
        term = flashcard['term']
        correct_def = flashcard['definition']
        choices = generate_choices(flashcards, flashcard)

        # check if answer given is valid
        isValidAnswer = False

        # Assess question until valid answer choice is given
        while (not isValidAnswer):
            # Display the question and choices
            print(f"{idx + 1} of {numCards}. What is the definition of '{term}'?\n")
            options = ['A', 'B', 'C', 'D']
            for i in range(4):
                print(f"  {options[i]}. {choices[i]}")

            # Get and validate user input
            user_input = input("\nYour answer (A/B/C/D): ").strip().upper()
            if user_input == "QUIT":
                isValidAnswer = True
                break
            if user_input not in options:
                print("⚠️  Invalid choice. Re-assessing question.\n")
                isValidAnswer = False

            else:

                selected_def = choices[options.index(user_input)]
                if selected_def == correct_def:
                    print("✅ Correct!\n")
                    score += 1
                else:
                    print(f"❌ Incorrect. The correct answer was: {correct_def}\n")

                isValidAnswer = True

        if user_input == "QUIT":
            break


    # calculate percentage
    quizPercentage = score / len(flashcards) * 100
    print(f"🎯 Quiz complete! Your score: {score}/{len(flashcards)} ({quizPercentage} %)")
