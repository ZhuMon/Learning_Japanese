# Learning_Japanese
## fifty_symbol
  * Usage:
    ```bash
    python fifty_symbol.py
    ```
  * 隨機產生五個日文的五十音
  * Randomly produce 5 different symbols in Romalization

---
## jp_listen
  * Dependencies:
    + selenium
    ```
    pip install selenium
    ```
     > 若是將selenium安裝到python2，可以將/usr/bin/local/python2.x裡的dependency複製到python3.x
    + chromedriver
     > 記得在jp_listen.py裡，更改chromedriver存放的位置（改成你自己的資料夾）
  * Usage:
    ```bash
    python3 jp_listen.py
    ```
  * 將片假名的單字存入list，以Google翻譯來充當聽力播放，按一次Enter會換一個單字
  * 若輸入a，則會重複播放同個單字（最多再重複播放兩次）
  * 按<ctrl + c>結束

