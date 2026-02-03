def pay_by_credit_card(amount, card_no, expiry):
    print("--- 處理金額: {amount} ---")


def pay_by_crypto(amount, wallet_addr, network):
    print("--- 處理金額: {amount} ---")


def main():
    payments = [
        {
            'method': 'credit_card',
            'amount': 20,
            'card_no': 'xxxx',
            'expiry': '2026-02-01'
        },
        {
            'method': 'credit_card',
            'amount': 20,
            'card_no': 'xxxx',
            'expiry': '2026-02-01'
        },
        {
            'method': 'crypto',
            'amount': 20,
            'wallet_addr': 'xxxx',
            'network': 'bitcoin'
        },
    ]

    for payment in payments:
        if payment['method'] == 'credit_card':
            pay_by_credit_card()
        else if payment['method'] == 'crypto':
            pay_by_crypto()


def main():
    # refund
    for payment in payments:

