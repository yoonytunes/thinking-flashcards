# Thinking Flashcards

This project aims to empower users to create and exercise their custom flashcard decksthat can be used to help them learn new words and phrases The user can then use the deck to practice their new words through traditional flashcard method or quiz mode.

The motivation of this project was to bypass the subscription model of currently existing flashcard apps that charge users to use the quiz feature, such as Quizlet or Anki.

### Intelligent Features

- The free response quiz feature is also a good way to practice new words and gives user to actively recall the new word from inherent understanding of it. An open-source large language model, i.e. Llama3.1 (8b, distilled) will evaluate the response and give a score to the response. The prompt is configured to give a detailed explanation of the thought process behind the evaluation.

### Dependencies
Users will need to have the following dependencies installed before using the app:
- Ollama installation (Llama3.1:8b model or any supported model from website)
- Python3 PIP installer

### Build & Run Instructions
To build and run the app, follow the steps below:
1. Clone the repository
2. Source the ```setup_instructions.sh``` script to install package dependencies, i.e. ```source setup_instructions.sh```
3. Define a flashcard deck in the flashcard directory as a yaml file (example provided)
4. Run the application in src folder, i.e. ```python3 quiz_app.py <path/to/flashcard/deck.yaml>```