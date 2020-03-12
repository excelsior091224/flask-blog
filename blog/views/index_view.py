from flask import Flask, render_template, flash, session, redirect, url_for, request
from blog import app, db
from blog.models.accounts import Account

@app.route('/')
def index():
    title = 'Flaskブログサービストップ'
    return render_template('index.html', title=title)

@app.route('/register', methods=['GET', 'POST'])
def register():
    title = '新規登録'
    if request.method == 'POST':
        if request.form['name'] == '':
            print('名前を入力してください')
        elif request.form['password'] == '':
            print('パスワードを入力してください')
        else:
            account = Account(
                name=request.form['name'],
                hashed_password=request.form['password']
            )
            db.session.add(account)
            db.session.commit()
            session['logged_in'] = True
            return redirect(url_for('index'))
    return render_template('register.html', title=title)

@app.route('/login', methods=['GET', 'POST'])
def login():
    title = 'ログイン'
    if request.method == 'POST':
        if request.form['name'] == '':
            print('名前を入力してください')
        elif request.form['password'] == '':
            print('パスワードを入力してください')
        else:
            user_name = request.form['name']
            user = Account.query.filter_by(name=user_name).first()
            if user is None:
                return redirect(url_for('login'))
            else:
                password = request.form['password']
                if password != user.hashed_password:
                    return redirect(url_for('login'))
                else:
                    session['logged_in'] = True
                    return redirect(url_for('index'))
    return render_template('login.html', title=title)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('index'))