from database.models import Questions
from database import db


def add_question_db(main_text, v1, v2, v3, v4, correct_answer, level):
    new_question = Questions(main_text=main_text,
                             variant_1=v1,
                             variant_2=v2,
                             variant_3=v3,
                             variant_4=v4,
                             correct_answer=correct_answer,
                             level=level)

    db.session.add(new_question)
    db.session.commit()

    return True


def get_questions_db(level):
    questions = Questions.query.filter_by(level=level).all()

    return questions[:21]


# proverka otveta polzovatelya
def check_user_answer_db(question_id, user_answer):
    questions = Questions.query.filter_by(id=question_id).first()

    if questions.correct_answer == user_answer:
        return True

    return False