class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def __str__(self):
        return f'Q: {self.question.strip("?")}?, A: {self.answer}'
