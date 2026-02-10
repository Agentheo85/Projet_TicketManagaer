from flask import Flask,make_response, send_file,request,jsonify
from io import BytesIO
import cv2
from pyzbar.pyzbar import decode
import matplotlib.pyplot as plt 
import barcode 
from barcode.writer import ImageWriter # lib pris sur internet elle permet de creer des code bars
import random # generer des nombres aleatoires
import os
from werkzeug.utils import secure_filename #lib utiliser pour les fichiers et s'assurer d'avoir le bon PATH
from flask_cors import CORS # je pense qu'il sert a autoriser les appels api entre meme ip
import json # utiliser pour charger le fichier .json 
import uuid # generer des id aleatoire


eancode128 = barcode.codex.Code128("Test123",writer=ImageWriter())

app = Flask(__name__)
CORS(app)

# lis un fichier json et le transform en dict python
def getJsonDataIntoDir():

    data = None
    
    with open("./Stats.json", "r") as f:
        
        data = json.load(f)
    return data
    

@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"

def CreateTicket(id):
    title = str(id)
    pathToImage = "./storages/"+title+".jpg"
    newfile = open(pathToImage, "x")
    with open(pathToImage, "wb") as f:

        barcode.codex.Code128(title,writer=ImageWriter()).write(f)
   

    return title



@app.get("/api/getstats")
def getStatsFromJson():
    data = getJsonDataIntoDir()
    print("test")
#jsonify Retourn le Dict Python en json et apres return vers le client ( site web )
    return jsonify(data)

@app.post("/api/newticket")
def newTicket():
    ticketId = str(random.randint(3, 999999))
    NewUser = request.get_json()
    NewUser["id"] = str(uuid.uuid1())
    NewUser["TicketId"] = ticketId
    Data = getJsonDataIntoDir()
    Data['Stats']["Purchased_Tickets"] += 1
    Data["Clients"].append(NewUser)
    print(Data['Stats']["Purchased_Tickets"])
    CreateTicket(ticketId)

    # ecris le fichier json , aide utiliser : https://www.geeksforgeeks.org/python/reading-and-writing-json-to-a-file-in-python/
    json_str = json.dumps(Data, indent=4)
    with open("./Stats.json", "w") as f:
        f.write(json_str)
    return {"id":ticketId}


@app.get("/api/downloadticket")
def downloadTicket():
    user = str(request.args.get('ticketid'))
    try:
            filename = secure_filename(user+".jpg")  # Sanitize the filename
            file_path = os.path.join("./storages", filename)
            if os.path.isfile(file_path):
                return send_file(file_path, as_attachment=True)
            else:
                return make_response(f"File '{filename}' not found.", 404)
    except Exception as e:
            return make_response(f"Error: {str(e)}", 500)


   

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
