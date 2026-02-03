def process_payment(
    method, amount, card_no=None, expiry=None, wallet_addr=None, network=None
):
    print(f"--- 處理金額: {amount} ---")
    if method == "credit_card":
        if not card_no or not expiry:
            raise ValueError("信用卡資訊不完整")
        print(f"驗證卡片 {card_no}，到期日 {expiry}...")
        print("刷卡成功！")

    elif method == "crypto":
        if not wallet_addr or not network:
            raise ValueError("加密錢包資訊不完整")
        print(f"連線至 {network} 網路...")
        print(f"發送交易至 {wallet_addr}...")
        print("轉帳發送成功！")


if __name__ == "__main__":
    process_payment("credit_card", 100, card_no="4444-1234", expiry="12/28")
    process_payment("crypto", 0.5, wallet_addr="0xABC123", network="Ethereum")
