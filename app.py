import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect, abort, jsonify
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a7a6aa1648368053ba39eeceb8b0264429ae11798bc8a0cf'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

@app.route("/positivity", methods=["GET"])
def positivity():
    # Positive affirmations list
    daily_affirmations = [
     "I am worthy of love and happiness.",
     "I am capable of achieving my goals.",
     "I am grateful for the blessings in my life.",
     "I am strong and resilient.",
     "I am surrounded by love and support.",
     "I am confident in my abilities.",
     "I am worthy of success.",
     "I am open to new possibilities and opportunities.",
     "I am becoming the best version of myself.",
     "I radiate positive energy.",
     "I make a positive difference in the world.",
     "I am in control of my thoughts and emotions.",
     "I trust the process of life.",
     "I embrace challenges as opportunities for growth.",
     "I choose peace and inner harmony."
    ]
    affirmation = random.choice(daily_affirmations)
    # Print a random affirmation for the day
    #return jsonify(affirmation)
    flash(affirmation)
    return render_template('positivity.html')

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        elif not content:
            flash('Content is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')

@app.route('/<int:id>/edit/', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')

        elif not content:
            flash('Content is required!')

        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)

@app.route('/<int:id>/delete/', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))
