from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/')
def index():
    posts = [
        ['https://attractor-school.com/', 'Attractor', 18000],
        ['https://makers.kg/', 'Makers', 15000],
        ['https://www.codifylab.com/ru/courses', 'Codify', 12000]
        ]
    return render_template('index.html', posts=posts)


@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html')


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
