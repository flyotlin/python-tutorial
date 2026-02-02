
# --- 文字處理功能 ---
def clean_text(text):
    return text.strip().lower()


# --- 數學計算功能 ---
def add_tax(price, rate=0.05):
    return price * (1 + rate)
