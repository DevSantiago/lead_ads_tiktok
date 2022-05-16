from flask import Flask, request
from dotenv import load_dotenv
from variants import lang_id_by_language, language_variants_by_gender_code, language_variants_by_country_code
import urllib.parse, hashlib, time, os

app = Flask(__name__)

@app.route("/", methods=["POST"])
def login(self = "self"):  
    lead_data = request.get_json()

    unformatted_lead = {
        "email": lead_data["data"]["lead_data"]["email"],
        "gender": lead_data["data"]["lead_data"]["gender"], # TODO add logic to accept any variant
        "language": lead_data["data"]["lead_data"]["language"], # TODO add logic to accept any variant
        "country": lead_data["data"]["lead_data"]["country"], # TODO add logic to accept any variant
        "campaign": lead_data["data"]["meta_data"]["campaign_name"]
    }

    formatted_lead = formatter(unformatted_lead)
    result = send_to_crm(formatted_lead)

    print(result)

    return "200 OK"

def formatter(unformatted_lead):
    formatted_lead = {
        "mail": unformatted_lead["email"],
        "campaign": unformatted_lead["campaign"]
    }

    # Default values
    country_code = "ES"
    lang_code = "EN"
    gender_code = "U"
    country_exists = False

    for key, values in language_variants_by_country_code.items(): 
        if unformatted_lead["country"] in values:
            country_code = key 
            country_exists = True
            break   

    for key, values in lang_id_by_language.items():
        if unformatted_lead["language"] in values:
            lang_code = key
            break

    for key, values in language_variants_by_gender_code.items():
        if unformatted_lead["gender"] in values:
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
    query_params = "&TOKEN=" + get_token() + "&MAIL=" + urllib.parse.quote(lead["mail"]) + "&LANG=" + lead["lang_code"] \
        + "&COUNTRYID=" + lead["country_code"] + "&GENDER=" + lead["gender_code"] + "&ORIGIN=TikTok_Lead_Ads" \
        + "&CAMPAIGN=" + urllib.parse.quote(lead["campaign"]) + "&SOURCE_CHANNEL=tiktok"

    final_url = ""

    if lead["country_exists"]:
        url_eu_us_ca = "https://campaigns.camper.com/optiext/optiextension.dll" \
        "?ID=QtSxtXlJxNuTw7GcjZQ_klVb%2BstS4L_sQF0BAM2ZOK7GPb5QU2IJKHNxCexS7IxV0FwFVi5T26BQQn"
        final_url = url_eu_us_ca + query_params

    else: 
        ur_leftover_countries = "https://campaigns.camper.com/optiext/optiextension.dll" \
        "?ID=7YU9oH6NNvTHawdqYXu2LFrNbyXPcUMuvSFJ%2BhTTgdBF%2BKlZQONzOTFsrXIZuCH3bduH7_xKa0"
        final_url = ur_leftover_countries + query_params

    # TODO make a get request to final_url and return the response

def get_token():
    load_dotenv()
    MY_USER_ENV_VAR = os.getenv("USER_CAMPER")
    MY_PWD_ENV_VAR = os.getenv("PWD_CAMPER")

    now = int(time.time())
    concat = MY_USER_ENV_VAR + MY_PWD_ENV_VAR + str(now)
    concat_hashed = hashlib.sha256(concat.encode('utf-8')).hexdigest()
    return MY_USER_ENV_VAR + ":" + str(now) + ":" + concat_hashed

if __name__ == "__main__":
    app.run()