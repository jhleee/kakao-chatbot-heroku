import os
import sys
import logging
from flask import Flask, request
from flask_json import FlaskJSON, as_json_p

from simple_kakao import *

app = Flask(__name__)
json = FlaskJSON(app)


@app.route('/keyboard/button', methods=["GET"])
@as_json_p
def keyboard_btn():
    btns = Buttons().add("A")\
                    .add("B")\
                    .add("C")
    return Keyboard(BUTTONS, btns)

@app.route('/keyboard', methods=["GET"])
@as_json_p
def keyboard_txt():
    return Keyboard(TEXT)

@app.route('/message', methods=["POST"])
@as_json_p
def msg():
    img_url = "https://dummyimage.com/600x400/000/ffffff.gif&text=Hello+World+!"
    photo = Photo(img_url, 600, 400)
    msg_btn = MessageButton("button", "https://example.com")

    return Response(
                Message("Blah...", photo, msg_btn),
                Keyboard(TEXT)
            )



# 
if 'DYNO' in os.environ:
    app.logger.addHandler(logging.StreamHandler(sys.stdout))
    app.logger.setLevel(logging.ERROR)

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True, use_reloader=True)
