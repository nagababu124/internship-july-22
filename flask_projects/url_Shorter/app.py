from flask import Flask, redirect, request, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
import random
import string
import os

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Urls(db.Model):
    id_ = db.Column("id_", db.Integer, primary_key=True)
    shortUrl = db.Column("shortUrl", db.String(5))
    longUrl = db.Column("longUrl", db.String())
    

    def __init__(self, shortUrl, longUrl):
        self.shortUrl = shortUrl
        self.longUrl = longUrl

def shortenUrlUtil():
    allAlphabets = string.ascii_lowercase + string.ascii_uppercase
    while True:
        randAlphabets = random.choices(allAlphabets, k=5)
        randAlphabets = "".join(randAlphabets)
        shortUrl = Urls.query.filter_by(shortUrl=randAlphabets).first()
        if not shortUrl:
            return randAlphabets

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/<generatedUrl>')
def useShortUrl(generatedUrl):
    originalUrl = Urls.query.filter_by(shortUrl=generatedUrl).first()
    if originalUrl:
        return redirect(originalUrl.longUrl)
    else:
        return f'<h2>Url doesnt exist</h2>'


@app.route('/url/<url>')
def displayUrl(url):
    return render_template('urlDisplay.html', generatedUrl = url)
@app.route('/history')
def displayUrl1():
    return render_template('history.html', urls=Urls.query.all())

@app.route('/', methods=['POST','GET'])
def home():
    if request.method == 'POST':
        url = request.form['urlInput']
        urlExists = Urls.query.filter_by(longUrl=url).first()
        if urlExists:
            #return corresponding shortURL
            return redirect(url_for("displayUrl", url = urlExists.shortUrl))
        else:
            #create a new short url
            shortURL = shortenUrlUtil()
            newUrl = Urls(shortURL, url)
            db.session.add(newUrl)
            db.session.commit()
            urlExists = Urls.query.filter_by(longUrl=url).first()
            return redirect(url_for("displayUrl", url = urlExists.shortUrl))
    else:
        return render_template("home.html", urls = Urls.query.all())


if __name__ == '__main__':
    app.run(port=5000, debug=True)