"""
5. 絕對匯入 (absolute import) 與 相對匯入 (relative import)

- 絕對匯入：從「專案根目錄」或某個在 sys.path 上的起點，一路寫到目標模組。
- 相對匯入：在套件 (package) 內，用 from .xxx import foo / from ..subpkg import bar，
  不硬編專案根路徑，模組搬家時較不容易壞掉。
"""


# === 絕對匯入範例 ===
# 假設你目前的工作目錄是 04_module_to_package/，就可以這樣寫：
#
# from tools_package.file_utils import save_json
# from tools_package.text_utils import clean_text
#
# 優點：
# - 一看就知道從哪個套件來 (tools_package)
# - 在整個專案裡搜尋 import 路徑，較容易追蹤依賴


# === 相對匯入範例（寫在 package 內部，例如 tools_package/__init__.py）===
#
# 正確的相對匯入寫法 (Python 3)：
#
# from .file_utils import save_json
# from .text_utils import clean_text
#
# 這裡的「.」代表「目前這個套件 (tools_package)」，所以就算整個套件被搬到別的地方，
# 只要套件內部結構沒變，這兩行匯入通常都還是會正常。
#
# 錯誤但常見的寫法（Python 2 時代遺留，Python 3 不建議）：
#
# from file_utils import save_json
#
# 在 Python 3 裡，這一行會被視為「絕對匯入」，而不是「相對匯入」，如果 sys.path 上沒有
# 找到名為 file_utils 的頂層模組，就會 ImportError。


def main():
    """印出說明與示範程式碼，方便直接執行觀看。"""
    from textwrap import dedent

    print(dedent(
        """\
        絕對匯入 (absolute import) 與 相對匯入 (relative import) 示範：

        [1] 絕對匯入 — 在 04_module_to_package/ 資料夾裡：

            from tools_package.file_utils import save_json
            from tools_package.text_utils import clean_text

        [2] 相對匯入 — 寫在 tools_package/__init__.py 裡：

            from .file_utils import save_json
            from .text_utils import clean_text

        你可以打開 04_module_to_package/tools_package/__init__.py，
        嘗試把「from file_utils import save_json」改成上面的相對匯入寫法，
        觀察行為上的差異。
        """
    ))


if __name__ == "__main__":
    main()

