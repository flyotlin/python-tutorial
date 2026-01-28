"""
Exception（例外／執行時期錯誤）範例

例外 = 程式在「執行當下」發生無法繼續的狀況，
Python 會拋出一個異常物件，若沒被 try/except 接住，程式就崩潰。
常見：除零、索引越界、型別錯誤、檔案不存在。
"""


def divide(a, b):
    """除零會觸發 ZeroDivisionError"""
    return a / b


def get_third_item(items):
    """串列太短會觸發 IndexError"""
    return items[2]


def parse_number(s):
    """無法轉成數字會觸發 ValueError"""
    return int(s)


if __name__ == "__main__":
    # 選一個取消註解來觀察不同例外：

    # ZeroDivisionError: division by zero
    print(divide(10, 0))

    # IndexError: list index out of range
    # print(get_third_item([1, 2]))

    # ValueError: invalid literal for int()
    # print(parse_number("abc"))
