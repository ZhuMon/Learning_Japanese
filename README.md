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
  
---
## remember_word
 * Dependencies:
   + ```jp_listen```
   + ```ReuseChrome```
 * Usage:
   ```bash
   python3 remember_word.py
   ```
 * 將```words```裡的單字取出，以選擇題或是問答題來記憶單字
 
---
## data_record
  * Usage:
    ```bash
    python3 data_record.py
    ```
  * 儲存單字到```words```
    1. 輸入要儲存什麼類型（words/phases）
    2. 輸入要儲存多少個
    3. 以 日文\<Tab\>中文 方式，輸入
    
 
