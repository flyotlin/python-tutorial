"""
Python Error Handling - Defensive Programming
決策點：及時處理還是向外傳遞？(Handle or Propagate?)

原則：在有能力解決問題的地方才處理例外。
(Only handle exceptions where you have the ability to solve the problem.)

架構：
  Function A (UI Layer)     → Try/Except，能「請使用者重試」
  Function B (Business Logic) → 傳遞資料、遇到錯就 log 後再 raise
  Function C (Data Access)  → 實際出錯處 (Encountered Error!)
"""

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Function C - Data Access（資料存取層）
# 實際發生錯誤的地方，沒有能力「對使用者解釋」，所以只負責 raise
# ---------------------------------------------------------------------------
def fetch_user_data(user_id: int) -> dict:
    """模擬從資料庫 / API 讀取資料。可能因連線、權限等出錯。"""
    # 模擬：找不到該使用者或連線失敗
    raise ConnectionError("Database connection failed: timeout after 5s")


# ---------------------------------------------------------------------------
# Function B - Business Logic（業務邏輯層）
# 沒有能力「解決」問題，但可以記錄下來給除錯用，再往上傳
# ---------------------------------------------------------------------------
def get_user_profile(user_id: int) -> dict:
    """中間層：把需求傳給 Data Access，收到錯就 log 後 re-raise。"""
    try:
        return fetch_user_data(user_id)
    except Exception as err:
        logger.error("Log error: %s", err)
        raise  # Re-raise to let A handle it（不吞掉，讓 UI 層處理）


# ---------------------------------------------------------------------------
# Function A - UI Layer（介面層）
# 有能力「對人解釋」與「請使用者重試」，所以在此 handle
# ---------------------------------------------------------------------------
def show_user_screen(user_id: int) -> None:
    """UI 層：有能力決定怎麼呈現錯誤、是否重試。"""
    try:
        profile = get_user_profile(user_id)
        print(f"使用者資料: {profile}")
    except ConnectionError as e:
        print("⚠ 無法取得資料，請檢查網路後重試。")
        print(f"   （技術訊息: {e}）")
    except Exception as e:
        print(f"發生未預期錯誤: {e}")


if __name__ == "__main__":
    print("=== 錯誤由 C → B → A 傳遞，最終在 A 被處理 ===\n")
    show_user_screen(user_id=123)
