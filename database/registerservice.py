from database.models import User
from database import db


# registery function of users
def register_user_db(name, phone_number):
    # check availability of user in base
    checker = User.query.filter_by(phone_number=phone_number).first()
    if checker:
        return checker.id

    # add data to base
    new_user = User(name=name, phone_number=phone_number)
    db.session.add(new_user)
    db.session.commit()

    return new_user.id









