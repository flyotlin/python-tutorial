"""
Logic Error（邏輯錯誤）範例

邏輯錯誤 = 程式能正常執行、不噴錯，但結果是錯的。
通常是「寫的人心裡想的和實際寫出來的不一樣」。
"""


def average(a, b):
    """本意：計算兩數平均。邏輯錯誤：寫成相加而不是平均。"""
    return a + b  # ❌ 應該是 (a + b) / 2


def is_leap_year(year):
    """本意：判斷是否為閏年。邏輯錯誤：閏年條件寫反。"""
    # 正確：能被 4 整除且不被 100 整除，或被 400 整除
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return True  # ❌ 被 100 整除應為 False（除非被 400 整除）
    return year % 4 == 0


if __name__ == "__main__":
    print("兩數平均（錯誤寫法）:", average(10, 20))  # 應得 15，實際得 30
    print("1900 是閏年？", is_leap_year(1900))  # 應 False，實際 True
    print("2000 是閏年？", is_leap_year(2000))  # 應 True，實際 True（碰巧對）
