class Payment:
    def pay(self, amount):
        raise NotImplementedError("Subclasses must implement pay()")


class CreditCardPayment(Payment):
    def __init__(self, card_no, expiry):
        self.card_no = card_no
        self.expiry = expiry

    def pay(self, amount):
        print(f"--- 處理金額: {amount} ---")
        if not self.card_no or not self.expiry:
            raise ValueError("信用卡資訊不完整")
        print(f"驗證卡片 {self.card_no}，到期日 {self.expiry}...")
        print("刷卡成功！")


class CryptoPayment(Payment):
    def __init__(self, wallet_addr, network):
        self.wallet_addr = wallet_addr
        self.network = network

    def pay(self, amount):
        print(f"--- 處理金額: {amount} ---")
        if not self.wallet_addr or not self.network:
            raise ValueError("加密錢包資訊不完整")
        print(f"連線至 {self.network} 網路...")
        print(f"發送交易至 {self.wallet_addr}...")
        print("轉帳發送成功！")


if __name__ == "__main__":
    my_methods = [
        CreditCardPayment("4444-1234", "12/28"),
        CryptoPayment("0xABC123", "Ethereum"),
    ]

    for method in my_methods:
        method.pay(500)
