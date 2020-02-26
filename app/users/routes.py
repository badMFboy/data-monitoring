from flask import request

from app import db
from app.models import User

from app.users import bp

@bp.route('/newUser',methods=['GET','POST'])
def newUser():
    data = request.get_json(silent=True)
    user = User.query.filter_by(username=data["user"]).first()
    if user is None:
        user = User(username=data["user"])
        user.set_password(data["password"])
        db.session.add(user)
        db.session.commit()
        return ("OK","200")
    print("Now your have {}".format(User.query.all()))
    return ("user there is already","200")

@bp.route('/rmUser',methods=['GET','POST'])
def rmUser():
    data = request.get_json(silent=True)
    user = User.query.filter_by(username=data["user"]).first()
    if user is None:
        return ("User {} not exist".format(data["user"]),"200")
    db.session.delete(user)
    db.session.commit()
    return ("user deleted ","200")