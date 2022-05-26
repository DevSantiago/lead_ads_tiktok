from variants import lang_id_by_language, language_variants_by_gender_code, language_variants_by_country_code, question_variants_by_param
from flask import Flask, request
from dotenv import load_dotenv
import urllib.parse
import requests
import hashlib
import time
import os


"""We initialize the Flask application in a variable."""

app = Flask(__name__)


@app.route("/", methods=["POST"])
def process_request(self = "self"):

    """We receive the lead from our endpoint."""

    try:
        unformatted_lead = get_unformatted_lead(request.get_json())
        formatted_lead = formatter(unformatted_lead)
        result = send_to_crm(formatted_lead)

        if result.status_code == 200 and result.headers["content-type"] == "application/json":
            print("Lead successfully sent to CRM")
        else:
            print("CRM rejected the lead")

        return "200 OK"
    except:
        return "The record could not be submitted"

def get_unformatted_lead(lead_data):

    """Find the corresponding key for each question based on language variants."""

    gender_key = ""
    lang_key = ""
    countryid_key = ""


    for key, values in lead_data["data"]["lead_data"].items():
        if key in question_variants_by_param['GENDER']:
            gender_key = key
        elif key in question_variants_by_param['COUNTRYID']:
            countryid_key = key
        elif key in question_variants_by_param['LANG']:
            lang_key = key

    formatted_lead = {
        "email": lead_data["data"]["lead_data"]["email"],
        "gender": lead_data["data"]["lead_data"][gender_key],
        "language": lead_data["data"]["lead_data"][lang_key], 
        "country": lead_data["data"]["lead_data"][countryid_key],
        "campaign": lead_data["data"]["meta_data"]["campaign_name"]
    }

    return formatted_lead

def formatter(unformatted_lead):

    """We format the lead."""

    formatted_lead = {
        "email": unformatted_lead["email"],
        "campaign": unformatted_lead["campaign"]
    }

    # Default values
    country_code = "ES"
    lang_code = "EN"
    gender_code = "U"
    country_exists = False

    for key, values in language_variants_by_country_code.items(): 
        if unformatted_lead["country"].strip().capitalize() in values:
            country_code = key 
            country_exists = True
            break   

    for key, values in lang_id_by_language.items():
        if unformatted_lead["language"].strip().capitalize() in values:
            lang_code = key
            break

    for key, values in language_variants_by_gender_code.items():
        if unformatted_lead["gender"].strip().capitalize() in values:
            gender_code = key
            break

    formatted_lead.update({
        "country_exists": country_exists,
        "country_code": country_code,
        "lang_code": lang_code,
        "gender_code" : gender_code,
    })

    return formatted_lead

def send_to_crm(lead):

    """We structure the query parameters."""

    query_params = "&TOKEN=" +get_token()+"&MAIL="+urllib.parse.quote(lead["email"])+"&LANG="+ lead["lang_code"] \
        +"&COUNTRYID="+lead["country_code"]+"&GENDER="+lead["gender_code"]+"&ORIGIN=TikTok_Lead_Ads" \
        +"&CAMPAIGN="+urllib.parse.quote(lead["campaign"])+"&SOURCE_CHANNEL=tiktok"

    final_url = ""

    if lead["country_exists"]:
        url_eu_us_ca = "https://campaigns.camper.com/optiext/optiextension.dll" \
        "?ID=QtSxtXlJxNuTw7GcjZQ_klVb%2BstS4L_sQF0BAM2ZOK7GPb5QU2IJKHNxCexS7IxV0FwFVi5T26BQQn"
        final_url = url_eu_us_ca+query_params

    else: 
        ur_leftover_countries = "https://campaigns.camper.com/optiext/optiextension.dll" \
        "?ID=7YU9oH6NNvTHawdqYXu2LFrNbyXPcUMuvSFJ%2BhTTgdBF%2BKlZQONzOTFsrXIZuCH3bduH7_xKa0"
        final_url = ur_leftover_countries+query_params

    print(final_url) # Left here for debugging purposes

    return requests.post(final_url)

def get_token():

    """We initialize our environment variables to get the token."""

    load_dotenv()
    MY_USER_ENV_VAR = os.getenv("USER_CAMPER")
    MY_PWD_ENV_VAR = os.getenv("PWD_CAMPER")

    now = int(time.time())
    concat = MY_USER_ENV_VAR + MY_PWD_ENV_VAR+str(now)
    concat_hashed = hashlib.sha256(concat.encode('utf-8')).hexdigest()
    return MY_USER_ENV_VAR+":"+str(now)+":"+concat_hashed

if __name__ == "__main__":
    app.run()