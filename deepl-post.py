
import requests
import json
import time

AUTH_KEY = "617cfdd7-a960-48fa-a947-9735f8d4a1b8:fx"

path = "/home/daniel/Documents/Projects/translator/output/dreams-xie-anshuo.txt"

translate_url = "https://api-free.deepl.com/v2/document"
#translate_status_url = "https://api-free.deepl.com/v2/document/{0}"
#translate_download_url = "https://api-free.deepl.com/v2/document/{0}/result"

# a function would start here

with open(path, "rb") as up_file:
    _params = {
        "source_lang" : "EN",
        "auth_key" : AUTH_KEY,
        "target_lang" : "ES"
    }

    response = requests.post(translate_url, params=_params, files={"file":up_file})
    print(response.text)
    jdata = json.loads(response.text)

_params["document_key"] = jdata["document_key"]

time.sleep(60)

response = requests.get("https://api-free.deepl.com/v2/document/{0}/result".format(jdata["document_id"]), params=_params,allow_redirects=True)
with open("translatedkirilov.txt", "wb") as f:
    f.write(response.content)