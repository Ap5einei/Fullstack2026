import json
import requests

url = "https://stat.hel.fi:443/api/v1/fi/Hyvinvointitilastot/Lasten_ja_nuorten_hyvinvointi/1_Vaesto_ja_elinolot/VE01_lastenmaara.px"

myobj = {
  "query": [
    {
      "code": "Ikä",
      "selection": {
        "filter": "item",
        "values": [
          "0-2-VUOTIAAT"
        ]
      }
    },
    {
      "code": "Vuosi",
      "selection": {
        "filter": "item",
        "values": [
          "23"
        ]
      }
    }
  ],
  "response": {
    "format": "json-stat"
  }
}

# https://requests.readthedocs.io

x = requests.get(url)
print(x.status_code)
result = x.json()
print(result)
loppu_string = json.dumps(result,indent=4)
print(loppu_string)


try:
    # mode is w+ because we want to create new file if necessary
    # if no file is present, file is created
    # w+ overwrites existing content
    fileobject = open("hesa.json","w+")

    # write 3 lines of material
    fileobject.writelines(loppu_string)

finally:
    fileobject.close()



