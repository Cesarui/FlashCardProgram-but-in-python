# FlashCard Project: I need to finish before Sunday!

class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    def __str__(self):
        return f'Q: {self.question.strip("?")}?, A: {self.answer}'

def show_cards():
    for key in flashcards:
        print(flashcards[key])

def check_if_exit(string):
    # returns true or false
    return string.strip().lower() == 'exit'

def add_card():
    # Each question is the key.
    # The value is a Flashcard object.
    # This lets me access both the
    # question and answer later.
    while input_on:
        print("What's your question? ")
        current_question = input()

        while current_question.strip() == "":
            print("Your question is empty...if you have no more questions\nto add, just type exit!")
            current_question = input()

        if check_if_exit(current_question):
            break

        print("What's your answer? ")
        current_answer = input()

        while current_answer.strip() == "":
            print("Your answer is empty...please type something!")
            current_answer = input()

        if check_if_exit(current_answer):
            break

        new_card = Flashcard(current_question, current_answer)
        flashcards[current_question] = new_card

print("""
Welcome to Study Buddy!

A flashcard-like quiz program to help you memorize
anything you want:)

""")
flashcards = {}

input_on = True

print("To start, just go ahead and add your question/answer pairs.\nIf you're finished adding, just type EXIT")

add_card()

print("""Now that you have some flashcards, what would you like to do?
(Type the number next to the option you'd like to do)

1) Add more flashcards
2) Remove question
3) View flashcards
4) Quiz yourself!
5) Quit

      """)

while input_on:

    option = int(input())

    if option == 1:
        add_card()

    elif option == 2:
        print("Which question do you want to remove? "
            "\nKeep in mind that whatever question you remove, "
            "\nit's answer will be removed as well!")

        questionToRemove = input()

        if questionToRemove in flashcards:
            del flashcards[questionToRemove]
        else:
            print("That question doesn't exist! Make sure you typed it correctly.")

    elif option == 3:
        show_cards()
    elif option == 4:
        right_answers = 0
        number_of_questions = len(flashcards)
        question_answer = None

        file = open('practice.txt', 'w')
        file.write("Here are the questions you should practice: ")
        # Under Construction...
        for quiz_key in flashcards:
            print(flashcards[quiz_key].question)

            question_answer = input()

            if question_answer.lower().strip() == flashcards[quiz_key].answer.lower().strip():
                right_answers += 1
                print(f"Correct!!, the answer to '{flashcards[quiz_key].question}' was indeed '{flashcards[quiz_key].answer}'")

            else:
                print(f"Uhh ohh, the answer was actually {flashcards[quiz_key].answer.strip()}!")
                file.write(f"{flashcards[quiz_key]}")

        print(f"You got {right_answers}/{number_of_questions} right!")
        file.close()


    elif option == 5:
        print("Have a good rest of your day! Here are the questions you should practice!")
        exit()

    print("""\nWhat now?

1) Add more flashcards
2) Remove question
3) View flashcards
4) Quiz yourself!
5) Quit
              """)
