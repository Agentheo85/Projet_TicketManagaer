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

# function qui creer le barcode
def CreateTicket(id): # l'id qu'on veut mettre au barcode
    title = str(id) 
    pathToImage = "./storages/"+title+".jpg" # le chemin ou on veut ecrire le fichier avec le nom du fichier
    newfile = open(pathToImage, "x")  # on creer le fichier
    with open(pathToImage, "wb") as f: # et on ecris le fichier

        barcode.codex.Code128(title,writer=ImageWriter()).write(f) # on utilise la lib qui permet de creer des barcode en image
   

    return title



@app.get("/api/getstats")
def getStatsFromJson():
    data = getJsonDataIntoDir()
    print("test")
#jsonify Retourn le Dict Python en json et apres return vers le client ( site web )
    return jsonify(data)

@app.post("/api/newticket")
def newTicket():
    ticketId = str(random.randint(3, 999999)) #creer un id aleatoire de 3 a 999999 , je suis au courant du bug qu'il peut se passer si il tombe sur le meme nombre , cela faussera le client
    NewUser = request.get_json() # Prend le json qu'on a send sur le body via la function fetch en js
    NewUser["id"] = str(uuid.uuid1()) # creer un Uuid pour l'id : XXXX-XXXX-XXXX-XXXX et set la valeur id de celui ci
    NewUser["TicketId"] = ticketId # set la valeur ticketid dans le dict de lui creer en haut 
    Data = getJsonDataIntoDir() # function qui renvoie le fichier json en Objet dict donc modifiable
    Data['Stats']["Purchased_Tickets"] += 1 # on ajoute plus un au nombre de ticket acheté
    Data["Clients"].append(NewUser) # on ajout le nouveau client 
    print(Data['Stats']["Purchased_Tickets"])
    CreateTicket(ticketId) # function qui va creer le barcode 

    # ecris le fichier json , aide utiliser : https://www.geeksforgeeks.org/python/reading-and-writing-json-to-a-file-in-python/
    json_str = json.dumps(Data, indent=4) # met le format json sous un format pouvant etre ecris 
    with open("./Stats.json", "w") as f: 
        f.write(json_str) # ecris le fichier
    return {"id":ticketId} # fait un return au fetch avec l'id du ticket


# Api Get , aide utiliser : https://stackoverflow.com/questions/70555453/how-do-you-return-a-file-from-an-api-response-flask-restful
@app.get("/api/downloadticket")
def downloadTicket():
    user = str(request.args.get('ticketid')) # Met en string le parametre meme si il est censé etre string de base
    try:
            filename = secure_filename(user+".jpg")  # s'assure du bon format fichier , eviter les erreurs ( était utiliser dans l'exemple que j'ai pris)
            file_path = os.path.join("./storages", filename) # s'assure d'utiliser le bon format de path , peut etre utile pour la compatibilité entre window et linux
            print(filename,file_path)
            if os.path.isfile(file_path): # verifi que c'est bien un fichier 
                return send_file(file_path, as_attachment=True) # retourne le fichier :  
            else:
                return make_response(f"File '{filename}' not found.", 404) # retourne une reponse par exemple sur google , il aura affichier file not found 
    except Exception as e:
            return make_response(f"Error: {str(e)}", 500) # de meme mais avec un message d'erreur different


   
# Ignorer les scripts en bas c'etait pour test 
"""EAN13 = barcode.get_barcode_class('ean13')
# Write to a file-like object:
newfile = open("myfildsdsderrr.jpg", "x")

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
