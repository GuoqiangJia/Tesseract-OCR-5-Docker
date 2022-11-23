from PIL import Image
from flask import Flask, request

import pytesseract as tess

app = Flask(__name__)


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        text = tess.image_to_string(image=Image.open(f.stream), lang='chi_sim', config='--oem 1')
        return text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
