import a_bad  # noqa: F401  # 只需要觸發 import a_bad 即可示範錯誤


if __name__ == "__main__":
    print("這行其實不會被執行到，因為上面的 import 已經失敗了。")

