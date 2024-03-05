import requests
from bs4 import BeautifulSoup
import json

url = "https://www.russianatom.ru/data_source/last_indications.php"
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

resp = requests.get(url, headers=headers)
soup = BeautifulSoup(resp.text, 'lxml')
a = resp.text.count('sensor id')
all_sens = []

all_sensors = soup.find_all("sensor")
for item in all_sensors:
    id = item.get("id")
    lat = item.get("lat")
    lng = item.get("lng")
    value = item.get("value")
    if value is None:
        print("Номер датчика (name) =",id,"не работает")
    else:
        all_sens.append(
            {
                "name" : id,
                "x" : lat,
                "y" : lng,
                "value" : value
            }
        )
with open("all_sens.json", "w") as file:
    json.dump(all_sens, file, indent=4, ensure_ascii=False)