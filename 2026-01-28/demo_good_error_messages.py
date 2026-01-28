"""
Python Error Handling - Defensive Programming
如何寫出「好的錯誤訊息」
Error Messages are UI for Developers

黃金法則 (The Golden Formula)：What → Why → How
  What：發生了什麼問題
  Why ：問題發生的原因（含實際收到的值）
  How ：如何修正

❌ Bad UX：模糊、無助益 (Vague, unhelpful)
✅ Good UX：具體、可操作、有資訊量 (Specific, actionable, informative)

🔒 Security Rule：永遠不要在錯誤訊息中包含 PII、密碼或內部路徑。
   （Never include PII, passwords, or internal paths in error messages.）
"""


# ---------------------------------------------------------------------------
# 🔒 Security Rule 示範：錯誤訊息裡「不要」出現的內容
# ---------------------------------------------------------------------------
# ❌ 不要：f"Login failed. User {user_email} with password hash {pwd_hash}"
# ❌ 不要：f"File not found: /home/ops/db/secrets.env"
# ✅ 要：  "Login failed: invalid credentials." 或 "File not found."
#          （需要除錯時用 log，不要寫進對外的錯誤訊息）


# ---------------------------------------------------------------------------
# ❌ Bad UX：只給「發生了什麼」，沒說為什麼、怎麼改
# ---------------------------------------------------------------------------
def process_transaction_bad(amount: int) -> None:
    """糟糕的錯誤訊息：像「Error 500」「Transaction failed」一樣模糊。"""
    if amount <= 0:
        raise ValueError("Transaction failed")  # 沒說原因、沒說怎麼改


# ---------------------------------------------------------------------------
# ✅ Good UX：What + Why + How 一次給齊
# ---------------------------------------------------------------------------
def process_transaction_good(amount: int) -> None:
    """良好的錯誤訊息：具體、可操作、有資訊量。"""
    if amount <= 0:
        # What: 交易失敗
        # Why: 'amount' 必須是正整數，實際收到 -50
        # How: 請輸入大於 0 的值
        raise ValueError(
            "Transaction Failed: 'amount' must be a positive integer. "
            f"Received: {amount}. Please enter a value > 0."
        )


def main():
    print("=== ❌ Bad UX ===\n")
    try:
        process_transaction_bad(-50)
    except ValueError as e:
        print(f"使用者只看到: {e}")
        print("→ 不知道為什麼錯、也不知道怎麼改\n")

    print("=== ✅ Good UX ===\n")
    try:
        process_transaction_good(-50)
    except ValueError as e:
        print(f"使用者看到: {e}")
        print("→ 知道錯在哪、收到什麼值、該怎麼改\n")

    # 成功案例
    print("=== 正常流程 ===\n")
    process_transaction_good(100)
    print("✔ 交易成功")


if __name__ == "__main__":
    main()
