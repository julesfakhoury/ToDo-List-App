
from flask import Flask, redirect, render_template, url_for
from decorators import require_request_params
from models import db, ToDoItems


app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db.init_app(app)


@app.route('/')
def index():
    """render template with list of all to-do items"""
    items = ToDoItems.query.all()
    return render_template('index.html', items=items)


@app.route('/add/item/', methods=['POST'])
@require_request_params(['item_text'])
def add_item(item_text):
    """
    Function to add a new item with content from "item_text"

    :param (str) item_text: content of item

    :return: redirect to root page
    """
    if item_text:
        todo_item = ToDoItems(text=item_text, done=False)
        db.session.add(todo_item)
        db.session.commit()
    return redirect(url_for('index'))


@app.route('/update/item/<item_id>', methods=['POST'])
@require_request_params(['done'])
def update_item(item_id, done):
    """
    Function to mark an item as done (if "done" is True) or undone (if "done" is False)

    :param (int) item_id: id of item to update
    :param (bool or str) done: True if item completed, otherwise False

    :return: redirect to root page
    """
    todo_item = ToDoItems.query.filter_by(id=int(item_id)).first()
    todo_item.done = bool(done)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/delete/item/<item_id>')
def delete_item(item_id):
    """
    Function to delete a to-do item based on its id

    :param (int) item_id: id of item to delete

    :return: redirect to root page
    """
    todo_item = ToDoItems.query.filter_by(id=int(item_id)).first()
    db.session.delete(todo_item)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
