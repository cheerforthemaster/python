import cv2
import os
from datetime import timedelta
from flask import Flask, render_template, request, make_response, Response
from networkx.release import basedir

from m_flask.data_pretreatment import getDataPretreatment
from m_flask.__init__ import m_init
from flask_cors import *

# from m_flask.sift import getSift

app = Flask(__name__)
# 热更新
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT '] = timedelta(seconds=1)
CORS(app)
isRight = True


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze')
def analyze():
    return render_template('analyze.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    data = "error"
    response = Response(data)
    response.headers['Access-Control-Allow-Origin'] = '*'
    f = request.files['file']
    if request.method == 'POST':
        file = 'm_flask/views/1.jpg'
        f.save(file)
        # getSift(file)
        data = getDataPretreatment(file)
        response = Response(data)
        response.headers['Access-Control-Allow-Origin'] = '*'
    if data == "图片不符合要求":
        cv2.imwrite("m_flask/views/3.jpg", None)
    f.close()
    return response

# @app.route('/upload', methods=['GET', 'POST'])
# def upload():
#     data = "error"
#     response = Response(data)
#     response.headers['Access-Control-Allow-Origin'] = '*'
#     if request.method == 'POST':
#         file = 'm_flask/views/1.jpg'
#         f = request.files['file']
#         f.save(file)
#         f.close()
#         # getSift(file)
#         data = getDataPretreatment(file)
#         response = Response(data)
#         response.headers['Access-Control-Allow-Origin'] = '*'
#     return response



# show photo
@app.route('/show')
def show_photo():
    filename = "m_flask/views/1.jpg"
    image_data = open(filename, "rb")
    response = Response(image_data, mimetype="image/jpeg")
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


# @app.route('/showTwo')
# def show_photo_Two():
#     filename = "m_flask/views/2.jpg"
#     image_data = open(filename, "rb")
#     response = Response(image_data, mimetype="image/jpeg")
#     return response


@app.route('/showThree')
def show_photo_Three():
    filename = "m_flask/views/3.jpg"
    image_data = open(filename, "rb")
    response = Response(image_data, mimetype="image/jpeg")
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


# 0 对应中性表情  5500张
# 1 对应高兴表情   5500张
# 2 对应沮丧表情   5500张
# 3 对应惊喜表情  5500张
# 4 对应恐惧表情  4000张
# 5 对应厌恶表情  4000张
# 6 对应愤怒表情  5500张
# 7 对应蔑视表情  4000张
if __name__ == '__main__':
    m_init()
    app.run(host='0.0.0.0', port=80)
