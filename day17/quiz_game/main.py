from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    t = question["text"]
    a = question["answer"]
    question_bank.append(Question(t, a))

game = QuizBrain(question_bank)
while(game.is_finished()):
    game.next_question();

print(f"Your score is: {game.score}")
