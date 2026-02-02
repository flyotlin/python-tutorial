"""
5. Circular Import 範例 — b_bad

說明：
- 這個模組在頂層 from a_bad import A_CONFIG
- 但 a_bad.py 也在頂層 from b_bad import get_b_config
- 兩邊互相在 import 階段就依賴對方，導致 ImportError。
"""

from a_bad import A_CONFIG  # ❶ 載入 b_bad 時，馬上嘗試從 a_bad 匯入 A_CONFIG


def get_b_config():
    """理想上想要讀到 A_CONFIG 再做一些處理。"""
    return {
        "name": "B_CONFIG",
        "from": "b_bad.py",
        "a_name": A_CONFIG["a"]["name"],
    }
