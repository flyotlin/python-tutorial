"""
Python Error Handling - Defensive Programming
自定義例外 (Custom Exceptions)

讓錯誤訊息具備「業務語義」— 用你的業務語言說話，而不是只講 Python 的語法。

Why? To speak the language of your business domain, not just Python's syntax.
How? Inherit from the Exception class.
"""


# ---------------------------------------------------------------------------
# 自定義例外：繼承 Exception，命名與訊息都表達業務意義
# Self-documenting code：看類別名與錯誤訊息就懂發生什麼事
# ---------------------------------------------------------------------------
class InsufficientBalanceError(Exception):
    """當餘額不足以支付時引發"""

    pass


def withdraw(amount: int, balance: int) -> int:
    """提款：若金額大於餘額則拋出自定義例外。"""
    if amount > balance:
        raise InsufficientBalanceError(
            f"餘額不足,目前僅有: {balance}"
        )
    return balance - amount


def main():
    balance = 100

    # # 正常提款
    # print("=== 正常提款 ===")
    # try:
    #     new_balance = withdraw(50, balance)
    #     print(f"提款成功，餘額: {new_balance}")
    # except InsufficientBalanceError as e:
    #     print(f"提款失敗: {e}")

    # 餘額不足 → 觸發自定義例外
    print("\n=== 餘額不足 ===")
    try:
        withdraw(500, balance)
    except InsufficientBalanceError as e:
        print(f"提款失敗: {e}")
        print("→ 呼叫端能針對「餘額不足」做專屬處理（如引導儲值）")


if __name__ == "__main__":
    main()
