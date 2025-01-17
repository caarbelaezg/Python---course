from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank  = [Question(question["text"], question["answer"]) for question in question_data]

quiz = QuizBrain(question_bank)

while quiz.has_next_question():

    quiz.next_question()