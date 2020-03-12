from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    title = 'test'
    return render_template('test.html', title=title)

if __name__ == "__main__":
    app.run(debug=True)