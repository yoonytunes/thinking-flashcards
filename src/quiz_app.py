from common.quiz_utils import *
from quiz_user_fr import quiz_user_fr
from quiz_user_mc import quiz_user_mc

def main():

    # load yaml file
    flashcards = load_flashcards()

    flashcards = filter_category(flashcards)
    
    quiz_mode = input("Which mode do you want to test in, Multiple Choice or Free Response?\n[1] Multiple Choice\n[2] Free Response\n").strip().lower()

    quiz_mode_dict = {"1": "Multiple Choice", "2": "Free Response"}

    # print quiz header
    print_quiz_header(quiz_mode_dict[quiz_mode])
    
    if quiz_mode == "1":
        # run multiple choice application
        quiz_user_mc(flashcards)
        
    elif quiz_mode == "2":
        # run free response application
        quiz_user_fr(flashcards)

    else:
        print("Invalid input. Defaulting to 'Multiple Choice'\n")
       
        # run multiple choice application
        quiz_user_mc(flashcards)


# define entry point
if __name__ == "__main__":
    main()
