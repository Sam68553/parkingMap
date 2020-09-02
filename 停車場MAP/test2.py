import os
import json
from flask import Flask, jsonify, request
import requests
from flask_cors import CORS



r = requests.get("https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=8b557432-1bea-4369-8029-3391fd85fe88&rid=acab92d6-361b-4c62-8aee-677dc1722965", verify=False)
print(r.json)