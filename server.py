import cv2
import numpy as np
import base64
from io import BytesIO
from PIL import Image
from flask import Flask, render_template, request, jsonify

# custom filter
from filters import filterMap


# Route for handling the login page logic
app = Flask(__name__, template_folder="public", static_folder='public/styles')
app.config['UPLOAD_FOLDER'] = "images"


@app.route('/')
def home():
    return render_template('index.html')


def readb64(base64_string):
    imgdata = base64.b64decode(base64_string)
    pimg = Image.open(BytesIO(imgdata))
    return cv2.cvtColor(np.array(pimg), cv2.COLOR_RGB2BGR)


@app.route('/filter', methods=['POST'])
def upload_file():
    reqData = request.json
    # print(len(reqData["imageFile"]))

    # converting image in base64 to image
    img = readb64(reqData["imageFile"])

    if(reqData["filter"] not in filterMap.keys()):
        return jsonify({"msg": "filter doesn't exist"})

    img2 = filterMap[reqData["filter"]](img)
    # print(img2)
    data = {
        "msg": "filter applied",
        "img": str(base64.b64encode(cv2.imencode('.jpg', img2)[1]))
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
