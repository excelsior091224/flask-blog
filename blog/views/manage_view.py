from flask import Flask, render_template, flash, session, redirect, url_for, request
from blog import app, db
from blog.models.entries import Entry

@app.route('/manage')
def manage():
    title = '管理画面'
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entries = Entry.query.filter_by(name=session['name']).all()
    return render_template('manage.html', title=title, entries=entries)

@app.route('/new_entry', methods=['GET', 'POST'])
def add_entry():
    title = '新規投稿作成'
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    if request.method == 'POST':
        if request.form['title'] == '':
            flash('タイトルを入力してください')
        elif request.form['text'] == '':
            flash('本文を入力してください')
        else:
            entry = Entry(
                name = session['name'],
                title = request.form['title'],
                text = request.form['text']
            )
            db.session.add(entry)
            db.session.commit()
            flash('新しく記事が作成されました')
            return redirect(url_for('manage'))
    return render_template('new_entry.html', title=title)
