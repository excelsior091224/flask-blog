from flask import Flask, render_template, flash, session, redirect, url_for, request
from blog import app, db
from blog.models.entries import Entry

@app.route('/<string:name>')
def blog(name):
    title = name
    entries = Entry.query.filter_by(name=name).all()
    return render_template('blog.html', title=title, entries=entries)

@app.route('/<string:name>/<int:id>')
def entry(name, id):
    entry = Entry.query.filter_by(name=name, id=id).first()
    title = entry.title
    return render_template('entry.html', title=title, entry=entry)