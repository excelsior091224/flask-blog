from flask import Flask, render_template, flash, session, redirect, url_for, request
from blog import app, db
from blog.models.accounts import Account

@app.route('/')
def index():
    title = 'Flaskブログサービストップ'
    users = Account.query.all()
    return render_template('index.html', title=title, users=users)

@app.route('/register', methods=['GET', 'POST'])
def register():
    title = '新規登録'
    if request.method == 'POST':
        if request.form['name'] == '':
            flash('名前を入力してください')
        if request.form['password'] == '':
            flash('パスワードを入力してください')
        if not request.form['name'] == '' and not request.form['password'] == '':
            account = Account(
                name=request.form['name'],
                hashed_password=request.form['password']
            )
            db.session.add(account)
            db.session.commit()
            session['logged_in'] = True
            session['name'] = request.form['name']
            flash('ユーザー名:' + session['name'] + 'で登録しました')
            return redirect(url_for('index'))
    return render_template('register.html', title=title)

@app.route('/login', methods=['GET', 'POST'])
def login():
    title = 'ログイン'
    if request.method == 'POST':
        if request.form['name'] == '':
            flash('名前を入力してください')
        if request.form['password'] == '':
            flash('パスワードを入力してください')
        if not request.form['name'] == '' and not request.form['password'] == '':
            user_name = request.form['name']
            user = Account.query.filter_by(name=user_name).first()
            if user is None:
                return redirect(url_for('login'))
            else:
                password = request.form['password']
                if password != user.hashed_password:
                    flash('パスワードが違います')
                    return redirect(url_for('login'))
                else:
                    session['logged_in'] = True
                    session['name'] = request.form['name']
                    flash('ユーザー名:' + session['name'] + 'でログインしました')
                    return redirect(url_for('index'))
    return render_template('login.html', title=title)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('name', None)
    return redirect(url_for('index'))