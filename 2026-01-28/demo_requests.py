"""
Python Error Handling - Defensive Programming
Practical Case: psf/requests Library

Excellent packages hide underlying complexity.
（優秀的套件把底層複雜度藏起來）

三層結構：
  Bottom：socket.error、urllib3.exceptions.ConnectionRefused 等底層錯誤
  Middle：Requests Adapter 捕捉並包裝成統一的例外
  Top   ：使用者只看得到 requests.exceptions.ConnectionError

User Experience: Simple, Unified Interface.
（使用者體驗：簡單、統一的介面）

執行前請先安裝：pip install requests
"""

import requests
from requests.exceptions import ConnectionError, Timeout


def fetch_url(url: str, timeout: int = 3) -> None:
    """
    示範：不論底層是 socket 超時、連線被拒、DNS 失敗等，
    對呼叫端而言都是統一的 requests.exceptions.ConnectionError / Timeout。
    """
    try:
        r = requests.get(url, timeout=timeout)
        r.raise_for_status()
        print(f"✔ 成功：{url} → 狀態碼 {r.status_code}")
    except ConnectionError as e:
        # 底層可能是 socket.error、ConnectionRefused 等，你只需處理這一種
        print(f"⚠ 連線失敗 (ConnectionError)：{e}")
        print("  → 使用者只需面對「連線失敗」，不用關心 socket/urllib3 細節")
    except Timeout:
        print(f"⚠ 逾時 (Timeout)：{url} 在 {timeout} 秒內無回應")
    except requests.exceptions.HTTPError as e:
        print(f"⚠ HTTP 錯誤：{e}")


def main():
    print("=== Practical Case: requests 的錯誤包裝 ===\n")

    # # 成功案例：可達的網址
    # print("1. 正常連線：")
    # fetch_url("https://httpbin.org/get")

    # 觸發 ConnectionError：無法連到的網址（如不存在的 host 或本機未開的 port）
    print("\n2. 連線失敗（示範使用者只看得到 ConnectionError）：")
    fetch_url("http://this-domain-does-not-exist-12345.example/")

    # print("\n→ Excellent packages hide underlying complexity.")
    # print("→ User Experience: Simple, Unified Interface.")


if __name__ == "__main__":
    main()
