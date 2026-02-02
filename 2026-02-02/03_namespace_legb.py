"""
2. 命名空間 (Namespace) 與作用域

思維轉換：從「物理檔案」轉向「名稱到物件的對映」(Mapping names to objects)。
同一名稱在不同命名空間可以指向不同物件。

LEGB 規則：名稱解析順序
  L - Local：函式內部
  E - Enclosing：外層函式（closure）
  G - Global：模組層級
  B - Built-in：Python 內建（如 len, print）
"""

# ========== Global 層級 ==========
GLOBAL_VAR = "我是 Global"


def enclosing_demo():
    """Enclosing：外層函式"""
    enclosing_var = "我是 Enclosing"

    def inner():
        """Local：內層函式"""
        local_var = "我是 Local"
        print("  [inner] Local:", local_var)
        print("  [inner] Enclosing:", enclosing_var)  # E
        print("  [inner] Global:", GLOBAL_VAR)        # G
        print("  [inner] Built-in len:", len([1, 2])) # B

    inner()
    # print(local_var)  # 錯誤：local_var 只在 inner 內可見


def shadowing_demo():
    """名稱遮蔽：內層同名變數會遮蔽外層"""
    GLOBAL_VAR = "Local 層級的 GLOBAL_VAR"
    print("  外層 GLOBAL_VAR:", GLOBAL_VAR)

    def inner():
        GLOBAL_VAR = "Inner 的 x（遮蔽外層）"
        print("  內層 GLOBAL_VAR:", GLOBAL_VAR)

    inner()
    print("  外層 GLOBAL_VAR 不變:", GLOBAL_VAR)


def global_keyword_demo():
    """global 關鍵字：在函式內改寫「模組層級」名稱（慎用）"""
    global GLOBAL_VAR
    print("  修改前 GLOBAL_VAR:", GLOBAL_VAR)
    GLOBAL_VAR = "已被函式改寫"
    print("  修改後 GLOBAL_VAR:", GLOBAL_VAR)


if __name__ == "__main__":
    print("--- LEGB：Local → Enclosing → Global → Built-in ---")
    enclosing_demo()

    print("\n--- 名稱遮蔽 (Shadowing) ---")
    shadowing_demo()

    print("\n--- global 關鍵字 ---")
    global_keyword_demo()
    print("  模組層級現在:", GLOBAL_VAR)
