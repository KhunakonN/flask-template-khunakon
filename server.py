from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title='My Home Page', msg='This is my Message')

@app.route('/user/info')
def info():
    return render_template('info.html',
                           title='Info Page',
                           name='khunakon wongburi',
                           email='khunakon@gmail.com',
                           moblie='063-325-5272',
                           age=19)

@app.route('/favorite/sports')
def fav_sport():
    sports = ['Golf','Baseball','Basketball','Football',]
    title='Favorite Sports Page'
    return render_template('favorite_sports.html',
                           title=title,
                           sports=sports)

@app.route('/favorite/food')
def fav_food():
    foods = ['Steak A5','Pad Krapow','Noodie',]
    title='Favorite Foods Page'
    return render_template('favorite_foods.html',
                           title=title,
                           foods=foods)