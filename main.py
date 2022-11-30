from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def index():
    posts = [
        ['Attractor', 10000, 10000],
        ['Makers', 15000, 15000],
        ['Codify', 12000, 12000]
        ]
    return render_template('index.html', posts=posts)


@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html')


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
