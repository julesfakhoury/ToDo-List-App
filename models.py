
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class ToDoItems(db.Model):
    """
    Class used to represent to-do items

    Attributes:
        (int) id: id of item
        (str) text: content of item
        (bool) done: True if item completed, otherwise False
    """
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    done = db.Column(db.Boolean)
