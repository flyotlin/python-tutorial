# tools.py

import json


# --- 檔案處理功能 ---
def save_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)
    print(f"檔案 {filename} 已儲存")


# --- 文字處理功能 ---
def clean_text(text):
    return text.strip().lower()


# --- 數學計算功能 ---
def add_tax(price, rate=0.05):
    return price * (1 + rate)