from flask import request, redirect, url_for
from dotenv import load_dotenv
from flask import Flask
import urllib.parse
import requests
import hashlib
import time
import json
import os



app = Flask(__name__)


@app.route("/dispatch")
def send_to_crm(data):

    load_dotenv()

    MY_USER_ENV_VAR = os.getenv("USER_CAMPER")
    MY_PWD_ENV_VAR = os.getenv("PWD_CAMPER")
    MY_ACCESSTOKEN_ENV_VAR = os.getenv("ACCESS_TOKEN")

    now = int(time.time())

    concat = MY_USER_ENV_VAR+MY_PWD_ENV_VAR+str(now)
    concat_hashed = hashlib.sha256(concat.encode('utf-8')).hexdigest()
    token =  MY_USER_ENV_VAR+":"+str(now)+":"+concat_hashed

    lead = data

    if lead["country_exists"]:
        MAIL = urllib.parse.quote(lead["mail"])
        LANG = lead["lang_cod"]
        COUNTRYID = lead["country_cod"]
        GENDER = lead["gender_cod"]
        ORIGIN = "TikTok_Lead_Ads"
        CAMPAIGN = urllib.parse.quote(lead["campaign"])
        SOURCE_CHANEL = "tiktok"

        url_eu_us_ca = "https://campaigns.camper.com/optiext/optiextension.dll?ID=QtSxtXlJxNuTw7GcjZQ_klVb%2BstS4L_sQF0BAM2ZOK7GPb5QU2IJKHNxCexS7IxV0FwFVi5T26BQQn&TOKEN="+token+"&MAIL="+MAIL+"&LANG="+LANG+"&COUNTRYID="+COUNTRYID+"&GENDER="+GENDER+"&ORIGIN="+ORIGIN+"&CAMPAIGN="+CAMPAIGN+"&SOURCE_CHANNEL="+SOURCE_CHANEL

        return url_eu_us_ca
    else: 
        MAIL = urllib.parse.quote(lead["mail"])
        LANG = lead["lang_cod"]
        COUNTRYID = lead["country_cod"]
        GENDER = lead["gender_cod"]
        ORIGIN = "TikTok_Lead_Ads"
        CAMPAIGN = urllib.parse.quote(lead["campaign"])
        SOURCE_CHANEL = "tiktok"

        ur_leftover_countries = "https://campaigns.camper.com/optiext/optiextension.dll?ID=7YU9oH6NNvTHawdqYXu2LFrNbyXPcUMuvSFJ%2BhTTgdBF%2BKlZQONzOTFsrXIZuCH3bduH7_xKa0&TOKEN="+token+"&MAIL="+MAIL+"&LANG="+LANG+"&COUNTRYID="+COUNTRYID+"&GENDER="+GENDER+"&ORIGIN="+ORIGIN+"&CAMPAIGN="+CAMPAIGN+"&SOURCE_CHANNEL="+SOURCE_CHANEL

        return ur_leftover_countries
    

@app.route("/formatter")
def formatter(lead):

    data = {
        "country_cod": "ES",
        "lang_cod": "EN",
        "gender_cod": "U"
    }
    country_cod = "ES"
    lang_cod = "EN"
    gender_cod = "U"
    country_exists = False


    countries = {
        "AD": [
            "Andorra",
            "Andorre",
            "アンドラ公国",
            "Andora",
            "Андорра"
        ],
        "AE": [
            "Emirats Àrabs Units",
            "United Arab Emirates",
            "Emiratos Árabes Unidos",
            "Emir.arab.unis",
            "Emirati Arab.U.",
            "アラブ首長国連邦",
            "Ver. Arab. Emir.",
            "Zjednoczone Emiraty Arabskie",
            "Emirados Árabes Unidos",
            "Арабские эмираты",
            "Birlesik Arap Emirlikleri"
        ],
        "AF": [
            "Afganistan",
            "Afghanistan",
            "Afganistán",
            "アフガニスタン",
            "Афганистан"
        ],
        "AG": [
            "Antigua i Barbuda",
            "Antigua/Barbuda",
            "アンティグア・バーブーダ",
            "Антигуа / Барбуда",
            "Antigua ve Barbuda"
        ],
        "AI": [
            "Anguilla",
            "アンギラ",
            "Ангилья"
        ],
        "AL": [
            "Albània",
            "Albania",
            "Albanien",
            "Albanie",
            "アルバニア共和国",
            "Albanië",
            "Албания",
            "Arnavutluk"
        ],
        "AM": [
            "Armènia",
            "Armenia",
            "Armenien",
            "Arménie",
            "アルメニア共和国",
            "Armenië",
            "Армения",
            "Ermenistan"
        ],
        "AN": [
            "Antilles Holandeses",
            "Dutch Antilles",
            "Antillas hol.",
            "Niederl.Antill.",
            "Antilles néerl.",
            "Antille Oland.",
            "オランダ領アンティル",
            "Nederlandse Antillen",
            "Antyle Holenderskie",
            "Голландские Антильские острова",
            "Hollanda Antilleri"
        ],
        "AO": [
            "Angola",
            "アンゴラ共和国",
            "Ангола"
        ],
        "AQ": [
            "Antàrtida",
            "Antarctica",
            "Antártida",
            "Antarktis",
            "Antarctique",
            "Antartide",
            "南極",
            "Antarktyka",
            "Антарктида",
            "Antartika"
        ],
        "AR": [
            "Argentina",
            "Argentinien",
            "Argentine",
            "アルゼンチン共和国",
            "Argentinië",
            "Argentyna",
            "Аргентина",
            "Arjantin"
        ],
        "AS": [
            "Samoa Nord-americana",
            "Samoa, American",
            "Samoa americana",
            "Samoa, améric.",
            "Samoa, americ.",
            "サモア",
            "Amerikaans Samoa",
            "Samoa Amerykańskie",
            "Самоа, Американское",
            "Samoa"
        ],
        "AT": [
            "Àustria",
            "Austria",
            "Österreich",
            "Autriche",
            "オーストリア",
            "Oostenrijk",
            "Áustria",
            "Австрия",
            "Avusturya"
        ],
        "AU": [
            "Austràlia",
            "Australia",
            "Australien",
            "Australie",
            "オーストラリア",
            "Australië",
            "Austrália",
            "Австралия",
            "Avustralya"
        ],
        "AW": [
            "Aruba",
            "アルバ共和国",
            "Аруба"
        ],
        "AZ": [
            "Azerbaidjan",
            "Azerbaijan",
            "Azerbaiyán",
            "Aserbaidschan",
            "Azerbaïdjan",
            "Azerbajdzan",
            "アゼルバイジャン共和国",
            "Azerbeidzjan",
            "Azerbejdżan",
            "Азербайджан",
            "Azerbeycan"
        ],
        "BA": [
            "Bosnia - Herzegovina"
        ],
        "BB": [
            "Barbados",
            "Barbades",
            "バルバドス",
            "Барбадос"
        ],
        "BD": [
            "Bangla Desh",
            "Bangladesh",
            "Bangladesch",
            "バングラデシュ人民共和国",
            "Bangladesz",
            "Бангладеш",
            "Banglades"
        ],
        "BE": [
            "Bèlgica",
            "Belgium",
            "Bélgica",
            "Belgien",
            "Belgique",
            "Belgio",
            "ベルギー",
            "België",
            "Belgia",
            "Бельгия",
            "Belçika"
        ],
        "BF": [
            "Burkina Faso",
            "Burkina-Faso",
            "ブルキナファソ",
            "Буркина-Фасо"
        ],
        "BG": [
            "Bulgària",
            "Bulgaria",
            "Bulgarien",
            "Bulgarie",
            "ブルガリア共和国",
            "Bulgarije",
            "Bułgaria",
            "Bulgária",
            "Болгария",
            "Bulgaristan"
        ],
        "BH": [
            "Bahrain",
            "Bahrein",
            "Bahreïn",
            "バーレーン王国",
            "Bahrajn",
            "Бахрейн",
            "Bahreyn"
        ],
        "BI": [
            "Burundi",
            "ブルンジ共和国",
            "Бурунди"
        ],
        "BJ": [
            "República de Benín",
            "Benin",
            "Bénin",
            "ベナン共和国",
            "Бенин"
        ],
        "BM": [
            "Bermudes",
            "Bermuda",
            "Bermudas",
            "バミューダ諸島",
            "Bermudy",
            "Бермудские острова"
        ],
        "BN": [
            "Brunéi Darussalam",
            "ブルネイ・ダルサラーム国"
        ],
        "BO": [
            "Bolívia",
            "Bolivia",
            "Bolivien",
            "Bolivie",
            "ボリビア",
            "Boliwia",
            "Боливия",
            "Bolivya"
        ],
        "BR": [
            "Brasil",
            "Brazil",
            "Brasilien",
            "Brésil",
            "Brasile",
            "ブラジル",
            "Brazilië",
            "Brazylia",
            "Бразилия",
            "Brezilya"
        ],
        "BS": [
            "Bahames",
            "Bahamas",
            "バハマ",
            "Bahama's",
            "Bahamy",
            "Багамские острова",
            "Bahamalar"
        ],
        "BT": [
            "Bhutan",
            "Bután",
            "Bhoutan",
            "ブータン王国",
            "Бутан"
        ],
        "BV": [
            "Illes Bouvet",
            "Bouvet Island",
            "Islas Bouvet",
            "Bouvet Inseln",
            "Ile Bouvet",
            "Isole Bouvet",
            "ブーベ島",
            "Bouveteiland",
            "Wyspa Bouveta",
            "Буве",
            "Bouvet Adasi"
        ],
        "BW": [
            "Botswana",
            "Botsuana",
            "ボツワナ共和国",
            "Ботсвана",
            "Botsvana"
        ],
        "BY": [
            "Bielorússia",
            "White Russia",
            "Bielorrusia",
            "Weissrussland",
            "Biélorussie",
            "Bielorussia",
            "ベラルーシ共和国",
            "Wit-Rusland",
            "Białoruś",
            "Белая Россия",
            "Beyaz Rusya"
        ],
        "BZ": [
            "Belize",
            "Belice",
            "ベリーズ",
            "Белиз"
        ],
        "CA": [
            "Canadà",
            "Canada",
            "Canadá",
            "Kanada",
            "カナダ",
            "Канада"
        ],
        "CC": [
            "Illa Coconut",
            "Coconut Islands",
            "Islas Coconut",
            "Kokosinseln",
            "Iles Cocos",
            "Isole di Cocos",
            "ココナッツ島",
            "Wyspy Kokosowe",
            "Кокосовые острова",
            "Coconut Adalari"
        ],
        "CF": [
            "República Centreafricana",
            "Central Afr.Rep",
            "Rep. Centro Afr",
            "Zentralaf. Rep.",
            "Rép. centrafr.",
            "Rep. Centroafr.",
            "中央アフリカ共和国",
            "Centraal Afr. Rep.",
            "Republika Środkowoafrykańska",
            "Центральный Афр.Респ.",
            "Orta Afrika Cumhuriyeti"
        ],
        "CG": [
            "Congo",
            "Kongo",
            "コンゴ共和国",
            "Конго"
        ],
        "CH": [
            "Suïssa",
            "Switzerland",
            "Suiza",
            "Schweiz",
            "Suisse",
            "Svizzera",
            "スイス",
            "Zwitserland",
            "Szwajcaria",
            "Suíça",
            "Швейцария",
            "Isviçre"
        ],
        "CI": [
            "Costa d’Ivori",
            "Ivory Coast",
            "Costa de Marfil",
            "Elfenbeinküste",
            "Côte d'Ivoire",
            "Costa d'Avorio",
            "コートジボワール",
            "Ivoorkust",
            "Wybrzeże Kości Słoniowej",
            "Берег Слоновой Кости",
            "Fildisi Sahilleri"
        ],
        "CK": [
            "Illes Cook",
            "Cook Islands",
            "Islas Cook",
            "Cookinseln",
            "Iles Cook",
            "Isole di Cook",
            "クック諸島",
            "Cookeilanden",
            "Wyspy Cooka",
            "Острова Кука",
            "Cook Adalari"
        ],
        "CL": [
            "Xile",
            "Chile",
            "Chili",
            "Cile",
            "チリ共和国",
            "Чили",
            "Sili"
        ],
        "CM": [
            "Camerun",
            "Cameroon",
            "Camerún",
            "Kamerun",
            "Cameroun",
            "カメルーン",
            "Kameroen",
            "Камерун"
        ],
        "CN": [
            "Xina",
            "China",
            "Chine",
            "Cina",
            "中華人民共和国",
            "Chiny",
            "Китай",
            "Çin",
            "中国"
        ],
        "CO": [
            "Colòmbia",
            "Colombia",
            "Kolumbien",
            "Colombie",
            "コロンビア",
            "Kolumbia",
            "Колумбия",
            "Kolombiya"
        ],
        "CR": [
            "Costa Rica",
            "コスタリカ",
            "Kostaryka",
            "Коста-Рика",
            "Kosta Rika"
        ],
        "CU": [
            "Cuba",
            "Kuba",
            "キューバ",
            "Куба",
            "Küba"
        ],
        "CV": [
            "Cap Verd",
            "Cape Verde",
            "Cabo Verde",
            "Kap Verde",
            "Cap-Vert",
            "Capo Verde",
            "カーボベルデ共和国",
            "Kaapverdië",
            "Republika Zielonego Przylądka",
            "Кабо-Верде",
            "Yesil Burun Adalari"
        ],
        "CX": [
            "Illa Christmas",
            "Christmas Islnd",
            "Islas Christmas",
            "Weihnachtsinsel",
            "Christmas I.",
            "Isola di Natale",
            "クリスマス島",
            "Christmaseiland",
            "Wyspa Bożego Narodzenia",
            "Рождество Islnd",
            "Christmas Adasi"
        ],
        "CY": [
            "Xipre",
            "Cyprus",
            "Chipre",
            "Zypern",
            "Chypre",
            "Cipro",
            "キプロス",
            "Cypr",
            "Кипр",
            "Kibris"
        ],
        "CZ": [
            "República Txeca",
            "Czech Republic",
            "República Checa",
            "Tschechische Re",
            "Rép. tchèque",
            "Rep. Ceca",
            "チェコ共和国",
            "Tsjechische Republiek",
            "Czechy",
            "Чешская республика",
            "Çek Cumhuriyeti"
        ],
        "DE": [
            "Alemanya",
            "Germany",
            "Alemania",
            "Deutschland",
            "Allemagne",
            "Germania",
            "ドイツ",
            "Duitsland",
            "Niemcy",
            "Alemanha",
            "Германия",
            "Almanya"
        ],
        "DJ": [
            "República de Djibouti",
            "Djibouti",
            "Yibuti",
            "Dschibuti",
            "Gibuti",
            "ジブチ共和国",
            "Dżibuti",
            "Джибути",
            "Cibuti Cumhuriyeti"
        ],
        "DK": [
            "Dinamarca",
            "Denmark",
            "Dänemark",
            "Danemark",
            "Danimarca",
            "デンマーク",
            "Denemarken",
            "Dania",
            "Дания",
            "Danimarka"
        ],
        "DM": [
            "Dominica",
            "La Dominique",
            "ドミニカ国",
            "Dominika",
            "Доминика"
        ],
        "DO": [
            "República Dominicana",
            "Dominican Rep.",
            "Rep. Dominicana",
            "Dominik. Rep.",
            "Rép.Dominicaine",
            "Rep. dominicana",
            "ドミニカ共和国",
            "Dominicaanse Rep.",
            "Republika Dominikańska",
            "Доминиканская Республика",
            "Dominik Cumhuriyeti"
        ],
        "DZ": [
            "Algèria",
            "Algeria",
            "Argelia",
            "Algerien",
            "Algérie",
            "アルジェリア民主人民共和国",
            "Algerije",
            "Algieria",
            "Алжир",
            "Cezayir"
        ],
        "EC": [
            "Equador",
            "Ecuador",
            "Equateur",
            "エクアドル",
            "Ekwador",
            "Эквадор",
            "Ekvator"
        ],
        "EE": [
            "Estònia",
            "Estonia",
            "Estland",
            "Estonie",
            "エストニア",
            "Estónia",
            "Эстония",
            "Estonya"
        ],
        "EG": [
            "Egipte",
            "Egypt",
            "Egipto",
            "Ägypten",
            "Egypte",
            "Egitto",
            "エジプト",
            "Egipt",
            "Египет",
            "Misir"
        ],
        "ER": [
            "Eritrea",
            "Erythrée",
            "エリトリア",
            "Erytrea",
            "Эритрея",
            "Eritre"
        ],
        "ES": [
            "Espanya",
            "Spain",
            "España",
            "Spanien",
            "Espagne",
            "Spagna",
            "スペイン",
            "Spanje",
            "Hiszpania",
            "Espanha",
            "Испания",
            "Ispanya"
        ],
        "ET": [
            "Etiòpia",
            "Ethiopia",
            "Etiopía",
            "Äthiopien",
            "Ethiopie",
            "Etiopia",
            "エチオピア",
            "Ethiopië",
            "Эфиопия",
            "Etiyopya"
        ],
        "FI": [
            "Finlàndia",
            "Finland",
            "Finlandia",
            "Finnland",
            "Finlande",
            "フィンランド",
            "Finlândia",
            "Финляндия",
            "Finlandiya"
        ],
        "FJ": [
            "Fiji",
            "Fidschi",
            "Fidji",
            "Figi",
            "フィジー",
            "Fidżi",
            "Фиджи"
        ],
        "FK": [
            "Illes Malvines",
            "Falkland Islnds",
            "Islas Malvinas",
            "Falklandinseln",
            "Malouines",
            "Isole Falkland",
            "フォークランド諸島",
            "Falklandeilanden",
            "Falklandy",
            "о. Фолклендские",
            "Falkland Adalari"
        ],
        "FM": [
            "Micronèsia",
            "Micronesia",
            "Mikronesien",
            "Micronésie",
            "ミクロネシア連合",
            "Micronesië",
            "Mikronezja",
            "Микронезия",
            "Mikronezya"
        ],
        "FO": [
            "Illes Fèroe",
            "Faroe Islands",
            "Islas Feroé",
            "Färöer",
            "Féroé",
            "Faeröer",
            "フェロー諸島",
            "Wyspy Owcze",
            "Фарерские острова",
            "Faroe Adalari"
        ],
        "FR": [
            "França",
            "France",
            "Francia",
            "Frankreich",
            "フランス",
            "Frankrijk",
            "Francja",
            "Франция",
            "Fransa"
        ],
        "GA": [
            "Gabon",
            "Gabón",
            "Gabun",
            "ガボン共和国",
            "Габон"
        ],
        "GB": [
            "Regne Unit",
            "United Kingdom",
            "Reino Unido",
            "Royaume-Uni",
            "Regno Unito",
            "イギリス",
            "Verenigd Koninkrijk",
            "Wielka Brytania",
            "Великобритания",
            "Birlesik Krallik"
        ],
        "GD": [
            "Grenada",
            "Granada",
            "Grenade",
            "グレナダ",
            "Гренада"
        ],
        "GE": [
            "Geòrgia",
            "Georgia",
            "Georgien",
            "Géorgie",
            "グルジア",
            "Georgië",
            "Gruzja",
            "Грузия",
            "Gürcistan"
        ],
        "GF": [
            "Guaiana Francesa",
            "French Guayana",
            "Guayana Franc.",
            "Französ.Guayana",
            "Guinée",
            "Guinea franc.",
            "フランス領ギアナ",
            "Frans-Guyana",
            "Gujana Francuska",
            "Французская Гуаяна",
            "Fransiz Guyanasi"
        ],
        "GH": [
            "Ghana",
            "ガーナ",
            "Гана",
            "Gana"
        ],
        "GI": [
            "Gibraltar",
            "Gibilterra",
            "ジブラルタル",
            "Гибралтар"
        ],
        "GJ": [
            "(Ch.) Illes - Regne Unit",
            "Ch. Islands -UK"
        ],
        "GL": [
            "Groenlàndia",
            "Greenland",
            "Groenlandia",
            "Grönland",
            "Groenland",
            "グリーンランド",
            "Grenlandia",
            "Гренландия"
        ],
        "GM": [
            "Gàmbia",
            "Gambia",
            "Gambie",
            "ガンビア共和国",
            "Гамбия",
            "Gambiya"
        ],
        "GN": [
            "Guinea",
            "Guinée",
            "ギニア共和国",
            "Gwinea",
            "Гвинея"
        ],
        "GP": [
            "Guadalupe",
            "Guadeloupe",
            "Guadalupa",
            "グアドループ",
            "Gwadelupa",
            "Гваделупа",
            "Guadelup"
        ],
        "GQ": [
            "Guinea Equatorial",
            "Equatorial Gui.",
            "Guinea Ecuator.",
            "Äquatorialguine",
            "Guinée Equator.",
            "Gui. Equator.",
            "赤道ギニア共和国",
            "Equatoriaal Gui.",
            "Gwinea Równikowa",
            "Экваториальная Гвинея",
            "Ekvator Ginesi"
        ],
        "GR": [
            "Grècia",
            "Greece",
            "Grecia",
            "Griechenland",
            "Grèce",
            "ギリシャ",
            "Griekenland",
            "Grecja",
            "Grécia",
            "Греция",
            "Yunanistan"
        ],
        "GS": [
            "Illes Sandwich del Sud",
            "S. Sandwich Ins",
            "Isl.S.Sandwich",
            "Îles Sandwich",
            "Isole SandwichS",
            "サウスサンドウィッチ諸島",
            "Z. Sandwich Eil.",
            "  Sandwich Południowy",
            "С. Сэндвич Инс",
            "Güney Sandwich Adalari"
        ],
        "GT": [
            "Guatemala",
            "Guatémala",
            "グアテマラ共和国",
            "Gwatemala",
            "Гватемала"
        ],
        "GU": [
            "Guam",
            "グアム",
            "Гуам"
        ],
        "GW": [
            "Guinea Bissau",
            "Guinea-Bissau",
            "Guinée-Bissao",
            "ギニアビサウ共和国",
            "Guinee-Bissau",
            "Gwinea Bissau",
            "Гвинея-Бисау"
        ],
        "GY": [
            "Guyana",
            "Guyane",
            "ガイアナ共和国",
            "Gujana",
            "Гайана"
        ],
        "HK": [
            "Hong Kong",
            "Hongkong",
            "香港",
            "Гонконг"
        ],
        "HM": [
            "Illes Heard i McDonald",
            "Heard/McDon.Isl",
            "Heard/Is.McDon",
            "Heard/McDon.Ins",
            "Il.Heard/McDon.",
            "Heard/is. McDon",
            "ハード島とマクドナルド諸島",
            "Heard/McDon. Eil.",
            "Wyspy Heard i McDonalda",
            "Херд / о. Макдональд",
            "Heard ve McDon.Adalari"
        ],
        "HN": [
            "Hondures",
            "Honduras",
            "ホンジュラス共和国",
            "Гондурас"
        ],
        "HR": [
            "Croàcia",
            "Croatia",
            "Croacia",
            "Kroatien",
            "Croatie",
            "Croazia",
            "クロアチア",
            "Kroatië",
            "Chorwacja",
            "Croácia",
            "Хорватия",
            "Hirvatistan"
        ],
        "HT": [
            "Haití",
            "Haiti",
            "Haïti",
            "ハイチ",
            "Гаити"
        ],
        "HU": [
            "Hongria",
            "Hungary",
            "Hungría",
            "Ungarn",
            "Hongrie",
            "Ungheria",
            "ハンガリー",
            "Hongarije",
            "Węgry",
            "Hungria",
            "Венгрия",
            "Macaristan"
        ],
        "ID": [
            "Indonèsia",
            "Indonesia",
            "Indonesien",
            "Indonésie",
            "インドネシア",
            "Indonesië",
            "Indonezja",
            "Индонезия",
            "Endonezya"
        ],
        "IE": [
            "Irlanda",
            "Ireland",
            "Irland",
            "Irlande",
            "アイルランド",
            "Ierland",
            "Irlandia",
            "Ирландия"
        ],
        "IL": [
            "Israel",
            "Israël",
            "Israele",
            "イスラエル",
            "Izrael",
            "Израиль",
            "Israil"
        ],
        "IN": [
            "Índia",
            "India",
            "Indien",
            "Inde",
            "インド",
            "Indie",
            "Индия",
            "Hindistan"
        ],
        "IO": [
            "Territori Britànic de l’Oceà Índic",
            "Brit.Ind.Oc.Ter",
            "Terr.br.Oc.Ind.",
            "Brit.Geb.Ind.Oz",
            "TerBritOcéanInd",
            "イギリス領インド洋地域",
            "Brit. Ind. Oc. Ter",
            "Brytyjskie Terytorium Oceanu Indyjskiego",
            "Британия",
            "Britanya Hint Oky. Topr."
        ],
        "IQ": [
            "Iraq",
            "Irak",
            "イラク",
            "Ирак"
        ],
        "IR": [
            "Iran",
            "Irán",
            "イラン",
            "Иран"
        ],
        "IS": [
            "Islàndia",
            "Iceland",
            "Islandia",
            "Island",
            "Islande",
            "Islanda",
            "アイスランド",
            "IJsland",
            "Islândia",
            "Исландия",
            "Izlanda"
        ],
        "IT": [
            "Itàlia",
            "Italy",
            "Italia",
            "Italien",
            "Italie",
            "イタリア",
            "Italië",
            "Włochy",
            "Itália",
            "Италия",
            "Italya"
        ],
        "JM": [
            "Jamaica",
            "Jamaika",
            "Jamaïque",
            "Giamaica",
            "ジャマイカ",
            "Jamajka",
            "Ямайка",
            "Jameika"
        ],
        "JO": [
            "Jordània",
            "Jordan",
            "Jordania",
            "Jordanien",
            "Jordanie",
            "Giordania",
            "ヨルダン",
            "Jordanië",
            "Иордания",
            "Ürdün"
        ],
        "JP": [
            "Japó",
            "Japan",
            "Japón",
            "Japon",
            "Giappone",
            "日本",
            "Japonia",
            "Japão",
            "Япония",
            "Japonya"
        ],
        "KE": [
            "Kènia",
            "Kenya",
            "Kenia",
            "ケニア",
            "Кения"
        ],
        "KG": [
            "Kirguizistan",
            "Kyrgyzstan",
            "Kirguizistán",
            "Kirgisistan",
            "Kirghiztan",
            "Chirghisistan",
            "キルギス共和国",
            "Kirgizië",
            "Kirgistan",
            "Киргизия",
            "Kirgizistan"
        ],
        "KH": [
            "Cambodja",
            "Cambodia",
            "Camboya",
            "Kambodscha",
            "Cambodge",
            "Cambogia",
            "カンボジア",
            "Kambodża",
            "Камбоджа",
            "Kamboçya"
        ],
        "KI": [
            "Kiribati",
            "キリバス共和国",
            "Кирибати"
        ],
        "KM": [
            "Comores",
            "Comoros",
            "Comoras",
            "Komoren",
            "Comore",
            "コモロ連合",
            "Comoren",
            "Komory",
            "Коморские острова",
            "Komoros"
        ],
        "KN": [
            "Saint Christopher i Nevis",
            "St Kitts&Nevis",
            "St.Chr.,Nevis",
            "St.Kitts&Nevis",
            "セントクリストファー・ネイビス連邦",
            "Saint Kitts i Nevis",
            "Сент-Китс и Невис"
        ],
        "KP": [
            "Corea del Nord",
            "North Korea",
            "Corea del Norte",
            "Nordkorea",
            "Corée du Sud",
            "朝鮮民主主義人民共和国",
            "Noord-Korea",
            "Korea Północna",
            "Северная Корея",
            "Kuzey Kore"
        ],
        "KR": [
            "Corea del Sud",
            "South Korea",
            "Corea del Sur",
            "Südkorea",
            "Corée du Sud",
            "大韓民国",
            "Zuid-Korea",
            "Korea Południowa",
            "Coreia do Sul",
            "Южная Корея",
            "Güney Kore"
        ],
        "KW": [
            "Kuwait",
            "Koweït",
            "クウェート国",
            "Koeweit",
            "Kuwejt",
            "Кувейт",
            "Küveyt"
        ],
        "KY": [
            "Illes Caiman",
            "Cayman Islands",
            "Islas Caimán",
            "Kaimaninseln",
            "Iles caïmans",
            "Isole Cayman",
            "ケイマン諸島",
            "Kaaimaneilanden",
            "Kajmany",
            "Каймановы острова",
            "Kayman Adalari"
        ],
        "KZ": [
            "Kazakhstan",
            "Kazajistán",
            "Kasachstan",
            "Kazakistan",
            "カザフスタン",
            "Kazachstan",
            "Казахстан"
        ],
        "LA": [
            "Laos",
            "ラオス",
            "Лаос"
        ],
        "LB": [
            "Líban",
            "Lebanon",
            "Líbano",
            "Libanon",
            "Liban",
            "Libano",
            "レバノン",
            "Ливан",
            "Lübnan"
        ],
        "LC": [
            "Saint Lucia",
            "St. Lucia",
            "Santa Lucía",
            "St. Lucie",
            "Santa Lucia",
            "セントルシア",
            "Сент-Люсия"
        ],
        "LI": [
            "Liechtenstein",
            "リヒテンシュタイン公国",
            "Listenstaine",
            "Лихтенштейн"
        ],
        "LK": [
            "Sri Lanka",
            "スリランカ",
            "Шри Ланка"
        ],
        "LR": [
            "Libèria",
            "Liberia",
            "リベリア共和国",
            "Либерия",
            "Liberya"
        ],
        "LS": [
            "Lesotho",
            "レソト王国",
            "Лесото"
        ],
        "LT": [
            "Lituània",
            "Lithuania",
            "Lituania",
            "Litauen",
            "Lituanie",
            "リトアニア共和国",
            "Litouwen",
            "Litwa",
            "Lituânia",
            "Литва",
            "Litvanya"
        ],
        "LU": [
            "Luxemburg",
            "Luxembourg",
            "Luxemburgo",
            "Lussemburgo",
            "ルクセンブルク",
            "Luksemburg",
            "Люксембург",
            "Lüksemburg"
        ],
        "LV": [
            "Letònia",
            "Latvia",
            "Letonia",
            "Lettland",
            "Lettonie",
            "Lettonia",
            "ラトビア共和国",
            "Letland",
            "Łotwa",
            "Letónia",
            "Латвия",
            "Letonya"
        ],
        "LY": [
            "Líbia",
            "Libya",
            "Libia",
            "Libyen",
            "Libye",
            "リビア共和国",
            "Libië",
            "Ливия"
        ],
        "MA": [
            "Marroc",
            "Morocco",
            "Marruecos",
            "Marokko",
            "Maroc",
            "Marocco",
            "モロッコ",
            "Maroko",
            "Марокко",
            "Fas"
        ],
        "MC": [
            "Mònaco",
            "Monaco",
            "Mónaco",
            "モナコ共和国",
            "Monako",
            "Монако"
        ],
        "MD": [
            "Moldàvia",
            "Moldavia",
            "Moldau",
            "Moldavie",
            "モルダヴィア",
            "Moldavië",
            "Mołdawia",
            "Молдавия",
            "Moldovya"
        ],
        "ME": [
            "Montenegro",
            "Czarnogóra"
        ],
        "MG": [
            "Madagascar",
            "Madagaskar",
            "マダガスカル共和国",
            "Мадагаскар"
        ],
        "MH": [
            "Illes Marshall",
            "Marshall Islnds",
            "Islas Marshall",
            "Marshall-Insel",
            "Iles Marshall",
            "Isola Marshall",
            "マーシャル諸島共和国",
            "Marshalleilanden",
            "Wyspy Marshalla",
            "Маршалл остр.",
            "Marsal Adalari"
        ],
        "MK": [
            "Macedònia",
            "Macedonia",
            "Mazedonien",
            "Macédoine",
            "マケドニア共和国",
            "Macedonië",
            "Македонии",
            "Makedonya"
        ],
        "ML": [
            "Mali",
            "マリ",
            "Мали"
        ],
        "MM": [
            "Birmània",
            "Myanmar",
            "ミャンマー",
            "Mjanma",
            "Мьянма"
        ],
        "MN": [
            "Mongòlia",
            "Mongolia",
            "Mongolei",
            "Mongolie",
            "モンゴル",
            "Mongolië",
            "Монголия",
            "Mogolistan"
        ],
        "MO": [
            "Macau",
            "Macao",
            "マカオ",
            "Makao",
            "Макао",
            "Makau"
        ],
        "MP": [
            "Illes Mariannes del Nord",
            "N.Mariana Islnd",
            "Isla N.Mariana",
            "Nördl. Marianen",
            "I. Mariannes N.",
            "Isola N.Mariana",
            "北マリアナ諸島",
            "Noordelijke Marianen",
            "Mariany Północne",
            "Н. Мариана остров",
            "Kuzey Mariana Adalari"
        ],
        "MQ": [
            "Martinica",
            "Martinique",
            "マルティニーク",
            "Martynika",
            "Мартиника",
            "Martinik"
        ],
        "MR": [
            "Mauritània",
            "Mauretania",
            "Mauritania",
            "Mauretanien",
            "Mauritanie",
            "モーリタニア",
            "Mauritanië",
            "Мавритания",
            "Moritanya"
        ],
        "MS": [
            "Montserrat",
            "モントセラト",
            "Монтсеррат"
        ],
        "MT": [
            "Malta",
            "Malte",
            "マルタ共和国",
            "Мальта"
        ],
        "MU": [
            "Illa Maurici",
            "Mauritius",
            "Mauricio (Isl.)",
            "Ile Maurice",
            "モーリシャス共和国",
            "Маврикий",
            "Moritus"
        ],
        "MV": [
            "Illes Maldives",
            "Maldives",
            "Islas Maldivas",
            "Malediven",
            "Maldive",
            "モルディブ共和国",
            "Malediwy",
            "Мальдивы",
            "Maldivler"
        ],
        "MW": [
            "Malawi",
            "Malaui",
            "マラウイ共和国",
            "Малави",
            "Malavi"
        ],
        "MX": [
            "Mèxic",
            "Mexico",
            "México",
            "Mexiko",
            "Mexique",
            "Messico",
            "メキシコ",
            "Meksyk",
            "Мексика",
            "Meksika"
        ],
        "MY": [
            "Malàisia",
            "Malaysia",
            "Malasia",
            "Malaisie",
            "マレーシア",
            "Maleisië",
            "Malezja",
            "Малайзия",
            "Malezya"
        ],
        "MZ": [
            "Moçambic",
            "Mozambique",
            "Mosambik",
            "Mozambico",
            "モザンビーク共和国",
            "Mozambik",
            "Мозамбик"
        ],
        "NA": [
            "Namíbia",
            "Namibia",
            "Namibie",
            "ナミビア共和国",
            "Namibië",
            "Намибия",
            "Namibya"
        ],
        "NC": [
            "Nova Caledònia",
            "New Caledonia",
            "Nueva Caledonia",
            "Neukaledonien",
            "N.Calédonie",
            "Nuova Caledonia",
            "ニューカレドニア",
            "Nieuw-Caledonië",
            "Nowa Kaledonia",
            "Новая Каледония",
            "Yeni Kaledonya"
        ],
        "NE": [
            "Nigèria",
            "Niger",
            "Nigeria",
            "ニジェール共和国",
            "Нигер",
            "Nijer"
        ],
        "NF": [
            "Illa Norfolk",
            "Norfolk Island",
            "Islas Norfolk",
            "Norfolkinseln",
            "Iles Norfolk",
            "Isole Norfolk",
            "ノーフォーク島",
            "Norfolk",
            "Wyspa Norfolk",
            "Остров Норфолк",
            "Norfolk Adasi"
        ],
        "NG": [
            "Nigèria",
            "Nigeria",
            "Nigéria",
            "ナイジェリア",
            "Нигерия",
            "Nijerya"
        ],
        "NI": [
            "Nicaragua",
            "ニカラグア共和国",
            "Nikaragua",
            "Никарагуа"
        ],
        "NL": [
            "Països Baixos",
            "Netherlands",
            "Países Bajos",
            "Niederlande",
            "Pays-Bas",
            "Paesi Bassi",
            "オランダ",
            "Nederland",
            "Holandia",
            "Países Baixos",
            "Нидерланды",
            "Hollanda"
        ],
        "NO": [
            "Noruega",
            "Norway",
            "Norwegen",
            "Norvège",
            "Norvegia",
            "ノルウェー",
            "Noorwegen",
            "Norwegia",
            "Норвегия",
            "Norveç"
        ],
        "NP": [
            "Nepal",
            "Népal",
            "ネパール",
            "Непал"
        ],
        "NR": [
            "Nauru",
            "ナウル共和国",
            "Науру"
        ],
        "NU": [
            "Niue",
            "Niue Islands",
            "Islas Niue",
            "Niue-Inseln",
            "Iles Niue",
            "Isole Niue",
            "ニウエ島",
            "Ниуэ Острова",
            "Niue Adalari"
        ],
        "NZ": [
            "Nova Zelanda",
            "New Zealand",
            "Nueva Zelanda",
            "Neuseeland",
            "N. Zélande",
            "Nuova Zelanda",
            "ニュージーランド",
            "Nieuw-Zeeland",
            "Nowa Zelandia",
            "Nova Zelândia",
            "Новая Зеландия",
            "Yeni Zelanda"
        ],
        "OM": [
            "Oman",
            "Omán",
            "オマーン国",
            "Оман",
            "Ümman"
        ],
        "PA": [
            "Panamà",
            "Panama",
            "Panamá",
            "パナマ共和国",
            "Панама"
        ],
        "PE": [
            "Perú",
            "Peru",
            "Pérou",
            "Perù",
            "ペルー",
            "Перу"
        ],
        "PF": [
            "Polinèsia Francesa",
            "Frenc.Polynesia",
            "Polinesia Fran.",
            "FranzPolynesien",
            "Polynésie fran.",
            "Polinesia fran.",
            "ポリネシア",
            "Frans-Polynesië",
            "Polinezja Francuska",
            "Французская Полинезия",
            "Fransiz Polinezyasi"
        ],
        "PG": [
            "Papua Nova Guinea",
            "Papua Nw Guinea",
            "PapuaNvaGuinea",
            "Papua-Neuguinea",
            "Pap.Nouv.Guinée",
            "Papua-Nuova Gu.",
            "パプワニューギニア",
            "Papoea-Nieuw-Guinea",
            "Papua-Nowa Gwinea",
            "Папуа Гвинея Nw",
            "Papua Yeni Gine"
        ],
        "PH": [
            "Filipines",
            "Philippines",
            "Filipinas",
            "Philippinen",
            "Filippine",
            "フィリピン",
            "Filipijnen",
            "Filipiny",
            "Филиппины",
            "Filipinler"
        ],
        "PK": [
            "Pakistan",
            "Pakistán",
            "パキスタン",
            "Пакистан"
        ],
        "PL": [
            "Polònia",
            "Poland",
            "Polonia",
            "Polen",
            "Pologne",
            "ポーランド",
            "Polska",
            "Polónia",
            "Польша",
            "Polonya"
        ],
        "PM": [
            "Saint-Pierre-et-Miquelon",
            "St.Pier,Miquel.",
            "St.Pier,Miquel",
            "StPier.,Miquel.",
            "St.Pierre,Miqu.",
            "サンピエール島とミクロン島",
            "Saint-Pierre en Miquelon",
            "Saint-Pierre i Miquelon",
            "Ст. Пьер, Микел.",
            "Saint Pierre ve Miquelon"
        ],
        "PN": [
            "Illes Pitcairn",
            "Pitcairn Islnds",
            "Islas Pitcairn",
            "Pitcairn Inseln",
            "Iles Pitcairn",
            "Isole Pitcairn",
            "ピトケアン諸島",
            "Pitcairneilanden",
            "Wyspy Pitcairn",
            "Питкэрн Islnds",
            "Pitcairn Adalari"
        ],
        "PR": [
            "Puerto Rico",
            "Porto Rico",
            "Portorico",
            "プエルトリコ",
            "Portoryko",
            "Пуэрто-Рико",
            "Porto Riko"
        ],
        "PT": [
            "Portugal",
            "Portogallo",
            "ポルトガル",
            "Portugalia",
            "Португалия",
            "Portekiz"
        ],
        "PW": [
            "Palau",
            "Palauan",
            "パラオ共和国",
            "Палау"
        ],
        "PY": [
            "Paraguai",
            "Paraguay",
            "パラグアイ",
            "Paragwaj",
            "Парагвай"
        ],
        "QA": [
            "Qatar",
            "Katar",
            "カタール",
            "Катар"
        ],
        "RE": [
            "Illa de la Reunió",
            "Reunion",
            "Réunion",
            "レユニオン",
            "Воссоединение"
        ],
        "RO": [
            "Romania",
            "Rumanía",
            "Rumänien",
            "Roumanie",
            "ルーマニア",
            "Roemenië",
            "Rumunia",
            "Roménia",
            "Румыния",
            "Romanya"
        ],
        "RS": [
            "Sèrbia",
            "Serbia",
            "Servië"
        ],
        "RU": [
            "Rússia",
            "Russia",
            "Rusia",
            "ロシア",
            "Rusland",
            "Rosja",
            "Россия"
        ],
        "RW": [
            "Ruanda",
            "Rwanda",
            "ルワンダ共和国",
            "Руанда"
        ],
        "SA": [
            "Aràbia Saudita",
            "Saudi Arabia",
            "Arabia Saudí",
            "Saudi-Arabien",
            "Arabie saoudite",
            "Arabia Saudita",
            "サウジアラビア",
            "Saoedi-Arabië",
            "Arabia Saudyjska",
            "Саудовская Аравия",
            "Suudi Arabistan"
        ],
        "SB": [
            "Salomó",
            "Solomon Islands",
            "Islas Salomón",
            "Salomonen",
            "Salomon",
            "Salomone",
            "ソルモン島",
            "Salomonseilanden",
            "Wyspy Salomona",
            "Соломоновы Острова",
            "Solomon Adalari"
        ],
        "SC": [
            "Seychelles",
            "Seychellen",
            "セーシェル共和国",
            "Seszele",
            "Сейшельские острова",
            "Seyseller"
        ],
        "SD": [
            "Sudan",
            "Sudán",
            "Soudan",
            "スーダン共和国",
            "Soedan",
            "Судан"
        ],
        "SE": [
            "Suècia",
            "Sweden",
            "Suecia",
            "Schweden",
            "Suède",
            "Svezia",
            "スウェーデン",
            "Zweden",
            "Szwecja",
            "Suécia",
            "Швеция",
            "Isveç"
        ],
        "SG": [
            "Singapur",
            "Singapore",
            "Singapour",
            "シンガポール",
            "Singapura",
            "Сингапур"
        ],
        "SH": [
            "Santa Helena",
            "St. Helena",
            "Sainte-Hélène",
            "Sant'Elena",
            "セントヘレナ",
            "Sint-Helena",
            "Wyspa Św. Heleny",
            "Остров Святой Елены"
        ],
        "SI": [
            "Eslovènia",
            "Slovenia",
            "Eslovenia",
            "Slowenien",
            "Slovénie",
            "スロベニア",
            "Slovenië",
            "Słowenia",
            "Eslovénia",
            "Словения",
            "Slovenya"
        ],
        "SJ": [
            "Svalbard",
            "Iles Svalbard",
            "スヴァールバル諸島",
            "Spitsbergen",
            "Шпицберген"
        ],
        "SK": [
            "Eslovàquia",
            "Slovakia",
            "Eslovaquia",
            "Slowakei",
            "Slovaquie",
            "Repubbl. Slov.",
            "スロバキア",
            "Slowakije",
            "Słowacja",
            "Eslováquia",
            "Словакия",
            "Slovakya"
        ],
        "SL": [
            "Sierra Leone",
            "Sierra Leona",
            "シエラレオネ共和国",
            "Сьерра-Леоне"
        ],
        "SM": [
            "República de San Marino",
            "San Marino",
            "Saint-Marin",
            "サンマリノ共和国",
            "Сан - Марино"
        ],
        "SN": [
            "Senegal",
            "Sénégal",
            "セネガル共和国",
            "Сенегал"
        ],
        "SO": [
            "Somàlia",
            "Somalia",
            "Somalie",
            "ソマリア",
            "Somalië",
            "Сомали",
            "Somali"
        ],
        "SR": [
            "Surinam",
            "Suriname",
            "Surinám",
            "スリナム共和国",
            "Суринам"
        ],
        "ST": [
            "Sao Tomé i Príncipe",
            "S.Tome,Principe",
            "S.Tomé,Príncipe",
            "S.Tomé-et-princ",
            "サントメ・プリンシペ",
            "Sao Tomé en Principe",
            "Wyspy Świętego Tomasza i Książęca",
            "С.-Томе, Принсипи",
            "Sao Tome ve Principe"
        ],
        "SV": [
            "República del Salvador",
            "El Salvador",
            "エルサルバドル共和国",
            "Salwador",
            "Сальвадор"
        ],
        "SY": [
            "Síria",
            "Syria",
            "Siria",
            "Syrien",
            "Syrie",
            "シリア",
            "Syrië",
            "Сирия",
            "Suriye"
        ],
        "SZ": [
            "Swazilàndia",
            "Swaziland",
            "Suazilandia",
            "Swasiland",
            "スワジランド",
            "Suazi",
            "Свазиленд",
            "Svaziland"
        ],
        "TC": [
            "Illes Turks i Caicos",
            "Turksh Caicosin",
            "Turks-,Caicosin",
            "Turks & Caicos",
            "タークス・カイコス諸島",
            "Turks- en Caicoseilanden",
            "Turks i Caicos",
            "Острова Теркс и Кайкос",
            "Turks ve Caicos Adalari"
        ],
        "TD": [
            "Txad",
            "Chad",
            "Tschad",
            "Tchad",
            "Ciad",
            "チャド共和国",
            "Tsjaad",
            "Czad",
            "Чад",
            "Çad"
        ],
        "TG": [
            "Togo",
            "トーゴ共和国",
            "Того"
        ],
        "TH": [
            "Tailàndia",
            "Thailand",
            "Tailandia",
            "Thaïland",
            "タイ",
            "Tajlandia",
            "Таиланд",
            "ประเทศไทย",
            "Tayland"
        ],
        "TJ": [
            "Tadjikistan",
            "Tajikstan",
            "Tadjikistán",
            "Tadschikistan",
            "Tagikistan",
            "タジキスタン共和国",
            "Tadzjikistan",
            "Tadżykistan",
            "Таджикистане",
            "Tacikistan"
        ],
        "TK": [
            "Tokelau",
            "Tokelau Islands",
            "Islas Tokelau",
            "Tokelau-Inseln",
            "Iles Tokelau",
            "Isole Tokelau",
            "トケラウ",
            "Островов Токелау",
            "Tokelau Adalari"
        ],
        "TM": [
            "Turkmenistan",
            "Turkmenistán",
            "Turkménistan",
            "トルクメニスタン",
            "Туркменистан",
            "Türkmenistan"
        ],
        "TN": [
            "Tunísia",
            "Tunisia",
            "Túnez",
            "Tunesien",
            "Tunisie",
            "チュニジア居和国",
            "Tunesië",
            "Tunezja",
            "Тунис",
            "Tunus"
        ],
        "TO": [
            "Tonga",
            "Isole Tonga",
            "トンガ王国",
            "Тонга"
        ],
        "TP": [
            "Timor Oriental",
            "East Timor",
            "Timor oriental",
            "Ost Timor",
            "Timor orient.",
            "Timor orientale",
            "東ティモール",
            "Oost-Timor",
            "Timor Wschodni",
            "Восточный Тимор",
            "Dogu Timor"
        ],
        "TR": [
            "Turquia",
            "Turkey",
            "Turquía",
            "Türkei",
            "Turquie",
            "Turchia",
            "トルコ",
            "Turkije",
            "Turcja",
            "Турция",
            "TÜRKİYE"
        ],
        "TT": [
            "Trinidad i Tobago",
            "Trinidad,Tobago",
            "トリニダード・トバゴ共和国",
            "Trinidad en Tobago",
            "Trynidad i Tobago",
            "Тринидад, Тобаго",
            "Trinidad ve Tobago"
        ],
        "TV": [
            "Tuvalu",
            "Tuvalú",
            "ツバル",
            "Тувалу"
        ],
        "TW": [
            "Taiwan",
            "台湾",
            "Tajwan",
            "Тайвань",
            "Tayvan"
        ],
        "TZ": [
            "Tanzània",
            "Tanzania",
            "Tansania",
            "Tanzanie",
            "タンザニア",
            "Танзания",
            "Tanzanya"
        ],
        "UA": [
            "Ucraïna",
            "Ukraine",
            "Ucrania",
            "Ucraina",
            "ウクライナ",
            "Oekraïne",
            "Ukraina",
            "Украина",
            "Ukrayna"
        ],
        "UG": [
            "Uganda",
            "Ouganda",
            "ウガンダ共和国",
            "Oeganda",
            "Уганда"
        ],
        "UM": [
            "Illes Perifèriques Menors dels EUA",
            "Minor Outl.Ins.",
            "Isl.Minor Outl.",
            "Iles Minor Outl",
            "Is. Minor Outl.",
            "合衆国領有小離島",
            "Kl. afg. eil. van de VS",
            "Dalekie Wyspy Mniejsze Stanów Zjednoczonych",
            "Малые Окл. Остр."
        ],
        "US": [
            "Estats Units",
            "USA",
            "Estados Unidos",
            "アメリカ合衆国",
            "VS",
            "США",
            "ABD"
        ],
        "UY": [
            "Uruguai",
            "Uruguay",
            "ウルグアイ",
            "Urugwaj",
            "Уругвай"
        ],
        "UZ": [
            "Uzbekistan",
            "Uzbekistán",
            "Usbekistan",
            "Ouzbékistan",
            "ウズベキスタン",
            "Oezbekistan",
            "Узбекистан",
            "Özbekistan"
        ],
        "VA": [
            "Vaticà",
            "Vatican City",
            "Ciudad Vaticano",
            "Vatikanstadt",
            "Vatican",
            "C. del Vaticano",
            "バチカン市国",
            "Vaticaanstad",
            "Watykan",
            "Ватикан",
            "Vatikan"
        ],
        "VC": [
            "Saint Vincent i les Grenadines",
            "St. Vincent",
            "San Vicente",
            "S. Vincenzo",
            "セントビンセント",
            "Saint Vincent",
            "Сент-Винсент"
        ],
        "VE": [
            "Veneçuela",
            "Venezuela",
            "Vénézuéla",
            "ベネズエラ",
            "Wenezuela",
            "Венесуэла",
            "Venezüela"
        ],
        "VG": [
            "Illes Verges Britàniques",
            "Brit.Virgin Is.",
            "Islas Virgen Br",
            "Brit.Jungferni.",
            "I. vierges brit",
            "Isole Verg. Br.",
            "英領ヴァージン諸島",
            "Br. Maagdeneil.",
            "Brytyjskie Wyspy Dziewicze",
            "Британские Виргинские остр.",
            "Ing. Virjin Adalari"
        ],
        "VI": [
            "Illes Verges Americanes",
            "Amer.Virgin Is.",
            "Islas Virgen Am",
            "Amer.Jungferni.",
            "I. vierges amér",
            "Isole Verg. Am.",
            "アメリカ領ヴァージン諸島",
            "Am. Maagdeneil.",
            "Wyspy Dziewicze Stanów Zjednoczonych",
            "Виргинские острова",
            "ABD Virjin Adalari"
        ],
        "VN": [
            "Vietnam",
            "Viêt Nam",
            "ベトナム",
            "Wietnam",
            "Вьетнам"
        ],
        "VU": [
            "Vanuatu",
            "バヌアツ共和国",
            "Вануату"
        ],
        "WF": [
            "Wallis i Futuna",
            "Wallis,Futuna",
            "ウォリス・フツナ諸島",
            "Wallis en Futuna",
            "Уоллис, Футуна",
            "Wallis ve Futuna Adalari"
        ],
        "WS": [
            "Samoa",
            "Western Samoa",
            "Samoa Occident.",
            "Westsamoa",
            "Samoa occident.",
            "Samoa occid.",
            "西サモア",
            "Западное Самоа",
            "Bati Samoa"
        ],
        "XI": [
            "United Kingdom (Northern Ireland)"
        ],
        "YE": [
            "Iemen",
            "Yemen",
            "Jemen",
            "Yémen du Nord",
            "イエメン共和国",
            "Йемен"
        ],
        "YT": [
            "Mayotte",
            "マヨット",
            "Majotta",
            "Майотта"
        ],
        "ZA": [
            "República de Sud-àfrica",
            "South Africa",
            "Sudáfrica",
            "Südafrika",
            "Afrique du Sud",
            "Sudafrica",
            "南アフリカ共和国",
            "Zuid-Afrika",
            "RPA",
            "ЮАР",
            "Güney Afrika"
        ],
        "ZM": [
            "Zàmbia",
            "Zambia",
            "Sambia",
            "Zambie",
            "ザンビア共和国",
            "Замбия"
        ],
        "ZW": [
            "Zimbàbue",
            "Zimbabwe",
            "Simbabwe",
            "ジンバブエ共和国",
            "Зимбабве",
            "Zimbabve"
        ]
    }

    langIdByLanguage = {
        "CA": "Català",
        "CO": "Español",
        "DE": "Deutsch",
        "EL": "ελληνικά",
        "EN": "English",
        "ES": "Español",
        "FR": "Français",
        "IT": "Italiano",
        "JA": "日本語",
        "KO": "한국어",
        "MX": "Español",
        "NL": "Nederlands",
        "PL": "Polski",
        "PT": "Português",
        "RU": "Россия",
        "TH": "ภาษาไทย",
        "TR": "Türkçe",
        "ZH": "中文",
        "SR": "sr"
    }


    languageVariantsByGenderCode = {
        "W": ["Mujer", "Woman", "Dona", "Mujer", "Damen", "Dona", "Women", "Mujer", "Femme", "Donna", "レディース", "Dona", "Mujer", "Dona", "Dona", "Mulher", "Женщины", "Dona", "Kadın", "女鞋", "Žene"],
        "M": ["Hombre", "Men", "Home", "Hombre", "Herren", "Home", "Men", "Hombre", "Homme", "Uomo", "メンズ", "Home", "Hombre", "Home", "Home", "Homem", "Мужчины", "หน้าแรก", "ERKEK", "男鞋", "Muškarci"],
        "U": ["No especificado", "Not specified", "Sense especificar", "Micca specificatu", "Unbestimmt", "Δεν διευκρινίζεται", "Not specified", "No especificado", "Non précisé", "Non specificato", "指定されていない", "명시되지 않은", "Not specified", "Niet gespecificeerd", "Nieokreślony", "Não especificado", "Не определено", "ไม่ได้ระบุ", "Belirtilmemiş", "未指定", "Није прецизирано"]
    }


    for key, values in countries.items(): 
        if lead["country"] in values:
            country_cod = key 
            country_exists = True
            break   

    for key, values in langIdByLanguage.items():
        if lead["language"] in values:
            lang_cod = key
            break

    for key, values in languageVariantsByGenderCode.items():
        if lead["gender"] in values:
            gender_cod = key
            break

    data.update({
        "country_exists": country_exists,
        "country_cod": country_cod,
        "lang_cod": lang_cod,
        "gender_cod" : gender_cod,
        "mail": lead["email"],
        "campaign": lead["campaign"]
    })

    send_to_crm(data)


@app.route("/", methods=["POST"])
def login(test="test"):

    
    lead_data = request.get_json() #Obtenemos el objeto de la petición en la variable lead_data.

    # Accedemos a los valores del objeto. Cada variable es respectiva a la información.


    email = lead_data["data"]["lead_data"]["email"]
    gender = lead_data["data"]["lead_data"]["Género"]
    language = lead_data["data"]["lead_data"]["Idioma"]
    country = lead_data["data"]["lead_data"]["País"]
    campaign = lead_data["data"]["meta_data"]["campaign_name"]

    lead_dictionary = {
        "email": email,
        "gender": gender,
        "language": language,
        "country": country,
        "campaign": campaign
    }

    formatter(lead_dictionary)      

    return "200 OK"


if __name__ == "__main__":
    app.run()