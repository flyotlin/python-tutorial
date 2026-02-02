"""
4. 套件 (Package) 與專案架構 — Import 機制

- import X：引入整個模組，使用 X.xxx，命名空間清晰，較安全。
- from X import *：易造成命名空間汙染，難以追蹤名稱來源，應避免。
- sys.path：模組搜尋路徑順序，影響「誰先被找到」；注意同名模組遮蔽 (Shadowing)。
- 絕對引入 vs 相對引入：套件內用 from . import foo 可移植性較好。
"""

import sys


def show_sys_path():
    """顯示當前 sys.path（模組搜尋順序）"""
    print("--- sys.path（模組搜尋順序，先找到先贏）---")
    print(sys.path)
    for i, p in enumerate(sys.path):
        print(f"  [{i}] {p}")

if __name__ == "__main__":
    show_sys_path()
