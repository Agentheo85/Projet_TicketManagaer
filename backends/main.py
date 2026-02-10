from flask import Flask,make_response, send_file
from io import BytesIO
import cv2
from pyzbar.pyzbar import decode
import matplotlib.pyplot as plt
import barcode
from barcode.writer import ImageWriter
import random
import os
from werkzeug.utils import secure_filename
from flask_cors import CORS



eancode128 = barcode.codex.Code128("Test123",writer=ImageWriter())

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

@app.route("/createTicket")
def CreateTicket():
    title = str(random.randint(3, 9999))
    pathToImage = "./storages/"+title+".jpg"
    newfile = open(pathToImage, "x")
    with open(pathToImage, "wb") as f:

        barcode.codex.Code128(title,writer=ImageWriter()).write(f)
    try:
        filename = secure_filename(title+".jpg")  # Sanitize the filename
        file_path = os.path.join("./storages", filename)
        if os.path.isfile(file_path):
            return send_file(file_path, as_attachment=True)
        else:
            return make_response(f"File '{filename}' not found.", 404)
    except Exception as e:
        return make_response(f"Error: {str(e)}", 500)

    return title

EAN13 = barcode.get_barcode_class('ean13')
# Write to a file-like object:
"""newfile = open("myfildsdsderrr.jpg", "x")

with open("myfildsdsderrr.jpg", "wb") as f:
    EAN13("999449999991", writer=ImageWriter()).write(f)

with open("otherfile.jpeg", "wb") as f:
    barcode.codex.Code128("WehhhW",writer=ImageWriter()).write(f)"""


# Pour lire les QR CODES , pas utiles 
"""gray = cv2.cvtColor(cv2.imread("otherfile.jpeg"), cv2.COLOR_BGR2GRAY)

    # Detect barcodes in the grayscale image
barcodes = decode(gray)

    # Loop over detected barcodes
for barcodeVal in barcodes:
        # Extract barcode data and type
    barcode_data = barcodeVal.data.decode("utf-8")
    barcode_type = barcodeVal.type

        # Print barcode data and type
    print("Barcode Data:", barcode_data)
    print("Barcode Type:", barcode_type)
"""
  # start the py environement  .venv\Scripts\activate 
  # start the server flask --app main run
  # main is the file name 
  # from flask import send_file
