import os
import json
from flask import Flask, jsonify, request
import requests
from flask_cors import CORS


# print(list_of_dicts["parkingLots"])
#print(list_of_dicts['parkingLots'][0])
#print(data)
app = Flask(__name__)
CORS(app)
@app.route('/getdata', methods = ['GET'])
def getdata():
    r = requests.get("https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=f4cc0b12-86ac-40f9-8745-885bddc18f79&rid=0daad6e6-0632-44f5-bd25-5e1de1e9146f", verify=False)

    list_of_dicts = r.json()
    data =[]

    response = list_of_dicts['parkingLots']
    return jsonify(response), 201

# Running the app
app.run(host = '0.0.0.0', port = 5001)