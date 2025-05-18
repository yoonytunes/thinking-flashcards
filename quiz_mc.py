import yaml
import random

def load_flashcards(filename="flashcards.yaml"):
    with open(filename, "r") as file:
        data = yaml.safe_load(file)
    return data['flashcards']

def generate_choices(flashcards, correct_card, num_choices=4):
    # Get all incorrect definitions
    other_definitions = [card['definition'] for card in flashcards if card != correct_card]
    choices = random.sample(other_definitions, num_choices - 1)
    choices.append(correct_card['definition'])
    random.shuffle(choices)
    return choices

def get_num_cards(flashcards):

    return len(flashcards)

def print_quiz_header():

    print("==============================================================================\n")
    print("💡 Medical Terminology Multiple Choice Quiz\n(Type 'exit' to quit at any time)\n")
    print("==============================================================================\n\n")

def quiz_user(flashcards):

    print_quiz_header()

    # determine test category
    print(f"Which category to test?\n")

    categories = ['all', 'respiratory', 'cardiovascular', 'gastrointestinal', 'genitourinary', 'musculoskeletal', 'integumentary', 'neurological', 'psychological', 'miscellaneous']

    print(f"{categories} \n")
    user_category_input = input("Your category: ").strip().lower()
    print("\n")
    
    # filter flashcards based on category
    if user_category_input not in categories:

        print(f"{user_category_input} is an invalid option. Defaulting to 'all'\n")
        user_category_input = 'all'
        
    elif user_category_input != 'all':

        flashcards = [k for k in flashcards if k.get("category").strip().lower() == user_category_input]

    # randomize 
    random.shuffle(flashcards)

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
            if user_input == "EXIT":
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

        if user_input == "EXIT":
            break


    # calculate percentage
    quizPercentage = score / len(flashcards) * 100
    print(f"🎯 Quiz complete! Your score: {score}/{len(flashcards)} ({quizPercentage} %)")



def main():

    # load yaml file
    flashcards = load_flashcards()

    # run application
    quiz_user(flashcards)



# define entry point
if __name__ == "__main__":
    main()
