# Learning_Japanese
## System
* macOS v10.13.6
* zsh v5.6.2
* python 3.6
* pip3.6 v18.1
* Google Chrome v70.0.3538.110 
* Chrome Extention:
    * [Keyboard Shortcuts for Google Translate v2.4.1.0](https://chrome.google.com/webstore/detail/keyboard-shortcuts-for-go/akjhnbnjanndggbcegmdggfjjclohjpo)

---
## fifty_symbol
  * Usage:
    ```bash
    python fifty_symbol.py
    ```
  * 隨機產生五個日文的五十音
  * Randomly produce 5 different symbols in Romalization
---
## time
  * Usage:
    ```bash
    python3 time.py
    ```
  * 隨機產生時間(ex: 12:12)，在按下enter後，會顯示時間的平假名
  * Randomly produce time(ex: 12:12).
  * After push ENTER, it will show the japanese of the time
---
## jp_listen
  * Dependencies:
    + selenium
      ```
      pip3 install selenium
      ```
    + chromedriver
    + 設定環境變數
      ```
      cd Learning_Japanese
      echo "export CHROME_DRIVER_PATH=\"$PWD\"" >> ~/.zshrc
      echo "export CHROME_USER_DATA=\"$OLDPWD/Library/Application Support/Google/Chrome\"" >> ~/.zshrc
      ```
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

