from flask import Flask
from flask import request, redirect, url_for
import requests
import json


app = Flask(__name__)


@app.route("/dispatch")
def send_to_crm(lead):

    url = "https://eo5spmb2ljndw6v.m.pipedream.net"
    data = json.dumps(lead)
    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, data, headers)

    return response

@staticmethod
@app.route("/", methods=['POST'])
def login():

    countries = [ 
        "DE",
        "AT",
        "PL",
        "CH",
        "GB",
        "IE",
        "NL",
        "DK",
        "SE",
        "FI",
        "IS",
        "NO",
        "FR",
        "MC",
        "BE",
        "IT",
        "GR",
        "ES",
        "PT",
        "AD",
        "BA",
        "BG",
        "CY",
        "HR",
        "SI",
        "EE",
        "HU",
        "IL",
        "LV",
        "LI",
        "LT",
        "LU",
        "MT",
        "CZ",
        "SK",
        "RO",
        "US",
        "CA",
        "SG",
        "HK",
        "IN",
        "ZA",
        "BR",
        "SA"
        ]

    if request.method == 'POST':

        lead_data = request.get_json() #Obtenemos el objeto de la petición en la variable lead_data.
    
        # Accedemos a los valores del objeto. Cada variable es respectiva a la información.

        name =  lead_data["data"]["lead_data"]["name"]
        email = lead_data["data"]["lead_data"]["email"]
        lead_id = lead_data["data"]["meta_data"]["lead_id"]
        page_id = lead_data["data"]["meta_data"]["page_id"]
        create_time = lead_data["data"]["meta_data"]["create_time"]
        campaign_name = lead_data["data"]["meta_data"]["campaign_name"]
        campaign_id = lead_data["data"]["meta_data"]["campaign_id"]
        ad_name = lead_data["data"]["meta_data"]["ad_name"]
        ad_id = lead_data["data"]["meta_data"]["ad_id"]

        lead_dictionary = {
            "name": name,
            "email": email,
            "lead_id": lead_id,
            "page_id": page_id,
            "create_time": create_time,
            "campaign_name": campaign_name,
            "campaign_id": campaign_id,
            "ad_name": ad_name,
            "ad_id": ad_id
        }

        send_to_crm(lead_dictionary)        

        return "200 OK"
    else:
        return "Éste método no es permitido para la URL en ejecución"


# @app.route("/")
# def main():
#     return "<p>Hola!</p>"


if __name__ == "__main__":
    app.run()
