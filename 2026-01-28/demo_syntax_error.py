"""
Syntax Error（語法錯誤）範例

語法錯誤 = 程式碼違反 Python 的「文法規則」，
在執行的第一步（解析階段）就會被攔下，整支程式不會開始跑。
常見：少打冒號、縮排錯、括號沒成對、錯用關鍵字。
"""

# ❌ 少了 if 後面的冒號
def check_age(age):
    if age >= 18
        return "成年"
    return "未成年"


# 底下這行永遠跑不到，因為上面已經語法錯誤
if __name__ == "__main__":
    print(check_age(20))
