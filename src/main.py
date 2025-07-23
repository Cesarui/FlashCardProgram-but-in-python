from flashcard import Flashcard

def show_cards():
    for key in flashcards:
        print(flashcards[key])


def check_if_exit(string):
    # returns true or false
    return string.strip().lower() == 'exit'


def remove_question():
    print("Which question do you want to remove? "
          "\nKeep in mind that whatever question you remove, "
          "\nit's answer will be removed as well!")
    question_to_remove = input()
    if question_to_remove in flashcards:
        print(f"{flashcards[question_to_remove]}\nhas been removed.")
        del flashcards[question_to_remove]
    else:
        print("That question doesn't exist! Make sure you typed it correctly.")


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


def quiz_mode():
    right_answers = 0
    number_of_questions = len(flashcards)

    file = open('practice.txt', 'w')

    file.write("Here are the questions you should practice: ")

    for quiz_key in flashcards:
        print(flashcards[quiz_key].question)

        question_answer = input()
        try:
            if question_answer.lower().strip() == flashcards[quiz_key].answer.lower().strip():
                right_answers += 1
                print(
                    f"Correct!!, the answer to '{flashcards[quiz_key].question}' was indeed '{flashcards[quiz_key].answer}'")

            else:
                print(f"Uhh ohh, the answer was actually {flashcards[quiz_key].answer.strip()}!")
                file.write(f"\n{flashcards[quiz_key]}")
        except ValueError:
            print("Don't forget to actually type something!")

    print(f"You got {right_answers}/{number_of_questions} right!")
    file.close()


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
    try:
        option = int(input())

        if option == 1:
            add_card()

        elif option == 2:
            remove_question()

        elif option == 3:
            show_cards()

        elif option == 4:
            quiz_mode()


        elif option == 5:
            print("Have a good rest of your day! \nPlease open the txt file to see the questions\n you need to practice:)!")
            exit()

        print("""\nWhat now?

1) Add more flashcards
2) Remove question
3) View flashcards
4) Quiz yourself!
5) Quit
                      """)

    except ValueError:
        print("Don't forget to actually type something!")

