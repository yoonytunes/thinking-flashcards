from ollama import Client
from config.llm_model_config import *
from common.quiz_utils import *
import subprocess

def quiz_user_fr(flashcards):
    
    # instantiate Ollama Client
    client = Client()

    # display available models
    display_available_models(client)

    myModelIdx = int(input("Enter model index: "))

    # get model
    myModel = fetch_model(client, myModelIdx)
    myModelName = myModel['model']

    numCards = get_num_cards(flashcards)
    
    # loop through each flashcard and ask the user for definition and compare it with the model's definition
    for num, flashcard in enumerate(flashcards):

        # display term on card and print question
        myResponse = input(f"\nQuestion {num + 1} of {numCards}: What is the definition of " + flashcard['term'] + "? ")

        term = flashcard['term']
        myDefinition = flashcard['definition']
        
        # submit prompt
        # myPrompt = input("Enter prompt: ")

        print(f"The answer is {myDefinition}.\n")
        
        myPrompt = f"My definition of {term} is {myResponse}. If the overall meaning of the expression {myResponse} and {myDefinition} is the same, respond with the word 'correct'. If they are not describing the same meaning, respond with the word 'incorrect'."
        myPrompt += f"Also, explain how you came to concluding whether the two expressions ({myResponse}) and ({myDefinition}) were similar or not."
        
        response = fetch_response(client, myModelName, myPrompt)

        # print response
        print("\n" + response)

    # close ollama
    subprocess.run(["pkill", "ollama"])

