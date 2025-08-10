import yaml
import random
import argparse

def load_flashcards(filename="../flashcards/flashcards.yaml"):

    parser = argparse.ArgumentParser(description="Process a yaml config file from CLI")
    parser.add_argument("file", type=argparse.FileType('r'), help="Path to the input file")
    args = parser.parse_args()

    if args.file:
        print(f"Loading flashcards from {args.file.name}")
        data = yaml.safe_load(args.file)

    else:
        print(f"Loading flashcards from default {filename}")
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

def print_quiz_header(mode):

    print("==============================================================================\n")
    print(f"💡 Medical Terminology {mode} Quiz\n(Type 'exit' to quit at any time)\n")
    print("==============================================================================\n\n")

def filter_category(flashcards):

    # extract only unique category fields from flashcards
    categories = list(set([card['category'] for card in flashcards]))

    # append 'all' category to beginning
    categories.insert(0, 'All')
    
    # create dictionary from categories with index as key for each category
    categories_dict = {idx: category for idx, category in enumerate(categories)} 

    # print each category on new line with index
    for idx, category in enumerate(categories_dict):
        print(f"[{idx}] {categories_dict[category]}")
        
    user_category_input = input("Your category: ").strip()
    user_category_input = int(user_category_input)
    
    # filter flashcards based on category
    if user_category_input not in range((len(categories_dict) + 1)):

        print(f"{categories_dict[user_category_input]} is an invalid option. Defaulting to 'all'\n")
        user_category_input = 0
        
    elif user_category_input != 0:

        flashcards = [k for k in flashcards if k.get("category").strip().lower() == categories_dict[user_category_input].lower()]

    # randomize 
    random.shuffle(flashcards)

    return flashcards
