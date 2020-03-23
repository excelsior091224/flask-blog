from flask import Flask, render_template, flash, session, redirect, url_for, request
from blog import app, db
from blog.models.entries import Entry
from datetime import datetime

@app.route('/manage')
def manage():
    title = '管理画面'
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entries = Entry.query.filter_by(name=session['name']).order_by(Entry.updated_at.desc()).all()
    return render_template('manage.html', title=title, entries=entries)

@app.route('/new_entry', methods=['GET', 'POST'])
def add_entry():
    title = '新規投稿作成'
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    if request.method == 'POST':
        if request.form['title'] == '':
            flash('タイトルを入力してください')
        if request.form['text'] == '':
            flash('本文を入力してください')
        if not request.form['title'] == '' and not request.form['text'] == '':
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

@app.route('/<string:name>/<int:id>/edit_entry', methods=['GET', 'POST'])
def edit_entry(name, id):
    title = '投稿編集'
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entry = Entry.query.filter_by(name=name, id=id).first()
    return render_template('edit_entry.html', title=title, entry=entry)

@app.route('/<string:name>/<int:id>/update_entry', methods=['POST'])
def update_entry(name, id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entry = Entry.query.filter_by(name=name, id=id).first()
    entry.title = request.form['title']
    entry.text = request.form['text']
    entry.updated_at = datetime.utcnow()
    db.session.merge(entry)
    db.session.commit()
    flash('記事が更新されました')
    return redirect(url_for('entry', name=name, id=id))

@app.route('/<string:name>/<int:id>/delete_entry', methods=['POST'])
def delete_entry(name, id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entry = Entry.query.filter_by(name=name, id=id).first()
    db.session.delete(entry)
    db.session.commit()
    flash('記事が削除されました')
    return redirect(url_for('manage'))