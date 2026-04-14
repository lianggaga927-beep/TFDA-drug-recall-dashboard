import requests
import json
import os

url = "https://data.fda.gov.tw/data/opendata/export/34/json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # 建立 data 資料夾存放靜態資源
    os.makedirs('data', exist_ok=True)
    with open('data/data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
else:
    print(f"API Error: {response.status_code}")
