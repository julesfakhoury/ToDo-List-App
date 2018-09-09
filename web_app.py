
from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)


class ToDoItems(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    done = db.Column(db.Boolean)


@app.route('/')
def index():
    items = ToDoItems.query.all()
    return render_template('index.html', items=items)


@app.route('/add/item/', methods=['POST'])
def add_item():
    item_text = request.form.get('item')
    if item_text:
        todo_item = ToDoItems(text=item_text, done=False)
        db.session.add(todo_item)
        db.session.commit()
    return redirect(url_for('index'))


@app.route('/update/item/<item_id>', methods=['POST'])
def update_item(item_id):
    todo_item = ToDoItems.query.filter_by(id=int(item_id)).first()
    todo_item.done = bool(request.form.get('done'))
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/delete/item/<item_id>')
def delete_item(item_id):
    todo_item = ToDoItems.query.filter_by(id=int(item_id)).first()
    db.session.delete(todo_item)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
