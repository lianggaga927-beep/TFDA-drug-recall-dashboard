import requests
import json
import os
import sys
import urllib3

# 1. 靜音化：抑制因 verify=False 產生的 InsecureRequestWarning 警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://data.fda.gov.tw/data/opendata/export/34/json"

try:
    # 2. 略過驗證：加入 verify=False 以避開台灣政府憑證不被信任的問題
    response = requests.get(url, timeout=30, verify=False)
    response.raise_for_status() 
    
    data = response.json()
    
    os.makedirs('data', exist_ok=True)
    with open('data/data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    print("資料抓取與儲存成功。")
    
except requests.exceptions.RequestException as e:
    print(f"API 請求失敗: {e}")
    sys.exit(0) 
except ValueError as e:
    print(f"JSON 解析失敗: {e}")
    sys.exit(0)
