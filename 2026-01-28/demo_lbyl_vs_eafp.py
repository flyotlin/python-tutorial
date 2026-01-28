"""
一、程式設計哲學：LBYL vs EAFP

LBYL (Look Before You Leap)：「三思而後行」
- 邏輯：在做事之前，先寫一堆 if 檢查所有可能的錯誤
- 缺點：檢查完到執行前的瞬間，狀態可能改變（Race Condition），且代碼會變得很臃腫

EAFP (Easier to Ask for Forgiveness than Permission)：「先斬後奏」
- 邏輯：直接做，出錯了再處理（Python 的核心哲學）
- 優點：程式碼乾淨、可讀性高，且能捕捉所有非預期的例外
"""

import os


# ❌ LBYL (不太 Pythonic)
def lbyl_read(filename):
    if os.path.exists(filename):  # 檢查檔案存在
        if os.access(filename, os.R_OK):  # 檢查權限
            with open(filename, "r") as f:
                return f.read()
    return "無法讀取檔案"


# ✅ EAFP (Python 推薦)
def eafp_read(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except (FileNotFoundError, PermissionError) as e:
        return f"讀取失敗：{e}"


if __name__ == "__main__":
    # 測試：用不存在的檔案名稱
    print("LBYL 結果:", lbyl_read("不存在的檔案.txt"))
    print("EAFP 結果:", eafp_read("不存在的檔案.txt"))
