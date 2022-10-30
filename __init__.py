# pylint: disable=missing-module-docstring
from flask import Flask,Response
from flask_restful import Api
from flask_cors import CORS
from src.controllers.amazon import set_price_list
from dotenv import load_dotenv,find_dotenv
# import os
load_dotenv(find_dotenv())
app = Flask(__name__)
CORS(app)
# print(os.environ.get("SECRET_KEY"))
api=Api(app)

def get_server_status():
    """returns the status of the server"""
    return Response({"message":"success"}),200

app.add_url_rule("/status",'status',get_server_status)
app.add_url_rule("/pricealert",'priceAlert',set_price_list,methods=["POST"])
app.run(port=3100, debug=True)
