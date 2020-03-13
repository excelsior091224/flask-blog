from flask import Flask, render_template, flash, session, redirect, url_for, request
from blog import app, db
from blog.models.entries import Entry

@app.route('/<string:name>')
def blog(name):
    title = name
    entries = Entry.query.filter_by(name=name).all()
    return render_template('blog.html', title=title, entries=entries)