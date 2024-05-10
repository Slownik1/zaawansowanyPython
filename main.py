import urllib
import numpy as np
import cv2
import requests
from flask import Flask, request, jsonify
from PIL import Image

app = Flask(__name__)

image_path = 'C:/Users/remik/Desktop/image.jpg'

@app.route('/')
def hello():
    return jsonify('Hello: World')

@app.route('/countGet', methods = ['GET'])
def count_get():
    image_path = request.args.get('image_path')
    if not image_path:
        return jsonify({'error': image_path}), 400
    return jsonify(count_people(image_path))

@app.route('/countUrl', methods = ['GET'])
def count_post():
    image_url= request.args.get('image_url')

    if not image_path:
        return jsonify({'error': image_path}), 400

    try:
        urllib.request.urlretrieve(image_url, "test.png")

        count = count_people("test.png")
        return jsonify({'number_of_people': count})
    except Exception as e:
        print(e)
        return jsonify({'error': 'Failed to load image from URL. Error: ' + image_url}), 400

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    file.save('test.png')
    count = count_people("test.png")
    return jsonify({'message': count}), 200


def count_people(image_path):
    image = cv2.imread(image_path)
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    (rects, weights) = hog.detectMultiScale(image, winStride=(8, 8), padding=(8, 8), scale=1.05)
    for (x, y, w, h) in rects:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return ("Liczba wykrytych osób:", len(rects))

if __name__ == '__main__':
    app.run(debug=True)
