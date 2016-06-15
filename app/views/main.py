from flask import render_template, jsonify
from app import app
import random


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/addImage')
def addImage():
    return render_template('addImage.html', title='Add image')



@app.route('/map')
def map():
    return render_template('map.html', title='Map')

@app.route('/image')
def image():
    return render_template('image.html', title='image')



@app.route('/map/refresh', methods=['POST'])
def map_refresh():
    points = [(random.uniform(48.8434100, 48.8634100),
               random.uniform(2.3388000, 2.3588000))
              for _ in range(random.randint(2, 9))]
    return jsonify({'points': points})


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')
