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
   python3 remember_word.py [FileName]
   ```
 * 將```[FileName]```裡的單字取出，以選擇題或是問答題來記憶單字
 * ```[FileName]``` 預設為 ```words```
 
---
## remember_phrase
 * Dependencies:
   + ```jp_listen```
   + ```ReuseChrome```
 * Usage:
   ```bash
   python3 remember_phrase.py           
   ```
 * 將```[phrases]```裡的片語取出，以選擇題或是問答題來記憶片語

---
## data_record
  * Usage:
    ```bash
    python3 data_record.py [FileName]
    ```
  * 輸入要儲存什麼類型（words/phases）
  * 輸入要儲存多少個
  * 儲存：
    * 儲存單字到```[FileName]```
      + 以 日文\<Tab\>中文 方式，輸入
      + ```[FileName]``` 預設為 ```words```
    * 儲存片語到```[FileName]```
      + 以 片語(無漢字)\<Tab\>片語(有漢字) 方式，輸入
      + ```[FileName]``` 預設為 ```phrases```

