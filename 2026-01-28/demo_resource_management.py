"""
Python Error Handling - Defensive Programming
資源管理與清理 (Resource Management)
Preventing Resource Leaks with Context Managers

對比兩種寫法：
  The Old Way：手動 try...finally + f.close()，容易忘記關閉
  The Pythonic Way：with 語句，離開縮排區塊時自動關閉，即使發生錯誤也不例外
"""

import os

# 本腳本所在目錄，方便用相對路徑 data.txt
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(SCRIPT_DIR, "data.txt")


def ensure_data_file():
    """確保 data.txt 存在，供後續範例讀取。"""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            f.write("Hello, Resource Management!\n")


# ---------------------------------------------------------------------------
# The Old Way (Explicit Finally)
# 容易忘記寫 finally / f.close()，且程式一長就難維護
# ---------------------------------------------------------------------------
def read_file_old_way(filepath: str) -> str:
    f = open(filepath, encoding="utf-8")
    try:
        content = f.read()
        return content
    finally:
        f.close()  # Easy to forget!


# ---------------------------------------------------------------------------
# The Pythonic Way (With Statement)
# 離開 with 區塊時自動關閉，即使區塊內發生例外也會關
# ---------------------------------------------------------------------------
def read_file_pythonic(filepath: str) -> str:
    with open(filepath, encoding="utf-8") as f:
        content = f.read()
        # Automatically closed here（離開縮排區塊時關閉）
    return content


def main():
    ensure_data_file()

    print("=== The Old Way (try...finally) ===\n")
    content1 = read_file_old_way(DATA_FILE)
    print(content1)

    print("=== The Pythonic Way (with) ===\n")
    content2 = read_file_pythonic(DATA_FILE)
    print(content2)

    print("→ 離開 with 縮排區塊時，檔案自動關閉，即使發生錯誤也不例外。")


if __name__ == "__main__":
    main()
