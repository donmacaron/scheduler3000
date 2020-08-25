from flask_login import UserMixin
from Scheduler3K import db
from Scheduler3K import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    is_curator = db.Column(db.Boolean, default=False, nullable=False)
    group_number = db.Column(db.String(10), nullable=False, default='None')

    def __repr__(self):
        return f"User('{self.username}', '{self.is_curator}', '{self.group_number}'"


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group_number = db.Column(db.String(20), unique=True, nullable=False)

    def __repr__(self):
        return self.group_number