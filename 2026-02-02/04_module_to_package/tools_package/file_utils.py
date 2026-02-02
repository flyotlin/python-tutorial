import json


# --- 檔案處理功能 ---
def save_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)
    print(f"檔案 {filename} 已儲存")
