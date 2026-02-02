"""
5. Circular Import 範例 — a_bad

說明：
- a_bad.py 在模組層級（import 當下）就 from b_bad import get_b_config
- b_bad.py 也在模組層級 from a_bad import A_CONFIG
- 兩邊互相在「載入階段」就需要對方的名稱，造成循環依賴 (circular import)

執行方式：
- 在專案根目錄或 2026-02-02 資料夾下執行：

    python 2026-02-02/05_circle_import/run_bad.py

你會看到 ImportError，錯誤訊息會提到「partially initialized module」，
代表有模組在尚未初始化完成時就被另一邊拿來用。
"""

from b_bad import get_b_config


A_CONFIG = {
    "a": {
        "name": "A_CONFIG",
        "from": "a_bad.py",
    },
    "b": get_b_config()
}


def show_a():
    """輔助函式，若沒有循環問題，本來預期可以正常呼叫。"""
    print("A_CONFIG =", A_CONFIG)
