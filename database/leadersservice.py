from database import db
from database.models import Leaders, UserAnswer


# zapis' rezultata tekushego testa
def user_end_test_db(user_id, correct_answers, level):
    exact_user_score = Leaders.query.filter_by(user_id=user_id,
                                               level=level).first()

    # check if anything in database
    if exact_user_score:
        # add to old scores new ones
        exact_user_score.score += correct_answers
        db.session.commit()


    # if no scores
    else:
        # create new leader data
        new_leader_data = Leaders(user_id=user_id,
                                  level=level,
                                  score=correct_answers)

        db.session.add(new_leader_data)
        db.session.commit()

    return True


# vivod liderov iz konkretnih urovney
def get_top_5_leaders_db(level):
    exact_level_leaders = Leaders.query.filter_by(level=level).order_by(Leaders.score.desc()).all()

    return exact_level_leaders[:6]


# zapis otvetov kajdogo polzovatelya
def add_user_answer_db(user_id, q_id, user_answer, correctness):
    new_answer = UserAnswer(user_id=user_id,
                             question_id=q_id,
                             user_answer=user_answer,
                             correctness=correctness)

    db.session.add(new_answer)
    db.session.commit()

    return True
