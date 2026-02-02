"""
1. Call Stack 簡單範例

- Call Stack：函式呼叫時，每次呼叫會壓入一個「stack frame」
- LIFO：最後被呼叫的函式最先返回
- Stack variable：每個 frame 裡有自己的區域變數，彼此獨立、互不干擾
"""

import traceback


def a():
    """第一層：a 的 stack frame 裡有變數 x"""
    x = 1  # ← stack variable，只存在於 a 的 frame
    print("  [a] x =", x)
    b()
    print("  [a] 返回前 x 還是", x)
    return x


def b():
    """第二層：b 的 stack frame 裡有變數 y（和 a 的 x 無關）"""
    y = 2  # ← stack variable，只存在於 b 的 frame
    print("  [b] y =", y)
    c()
    return y


def c():
    """第三層：c 的 stack frame 裡有變數 z；印出當前 call stack"""
    z = 3  # ← stack variable，只存在於 c 的 frame
    print("  [c] z =", z)
    print("\n--- 當前 Call Stack（由上到下 = 由內到外）---")
    traceback.print_stack()
    return z


if __name__ == "__main__":
    print("--- Call Stack：a() -> b() -> c() ---\n")
    a()
    print("\n--- 說明：每個函式有自己的 stack frame，裡面的變數 (x, y, z) 是各自的 stack variable ---")
