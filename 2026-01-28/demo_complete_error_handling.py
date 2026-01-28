"""
Python Error Handling - Defensive Programming
錯誤處理的完整解剖 (The Anatomy of Defense)

展示 try-except-else-finally 四區塊的職責：
  try     → Monitor (監控): 嘗試執行可能出錯的程式碼
  except  → Recover (補救): 針對特定錯誤進行處理
  else    → Success (成功): 若無例外發生則執行此區塊
  finally → Cleanup (清理): 無論是否出錯，最後一定執行
"""


def main():
    try:
        # Monitor：嘗試執行可能出錯的程式碼
        num = int(input("輸入一個數字: "))
        result = 10 / num
    except ValueError:
        # Recover：使用者輸入非數字（如 "abc"）
        print("錯誤: 請輸入有效的數字!")
    except ZeroDivisionError:
        # Recover：使用者輸入 0，導致除零
        print("錯誤: 分母不能為 0!")
    except Exception as e:
        # Recover：其餘未預期的錯誤
        print(f"發生未預期錯誤: {e}")
    else:
        # Success：try 內完全沒出錯時才執行
        print(f"10 / {num} = {result}")
        print("✔ 計算成功")
    finally:
        # Cleanup：無論有無例外，最後一定執行
        print("程式執行結束")


if __name__ == "__main__":
    main()
