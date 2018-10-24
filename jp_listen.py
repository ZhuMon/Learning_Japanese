from selenium import webdriver
import random
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

chromedriver = "/Users/linyuxiang/Desktop/code/Learning_Japanese/chromedriver"
driver = webdriver.Chrome(chromedriver)
driver.get("https://translate.google.com.tw/")

#input data
katakana = [
	
	"コーヒー", "スーツ", "スカート","ユーロ" 
	, "ソファー", "フィルム", "チェック", "フォード", "ファミリ"  
	, "ボディー", "ファン", "ノルウェー", "ディスコ", "ジェット"  
	, "ウィスキー", "ウォーター"
	, "ウィ", "ウェ", "ウォ"  
	, "ヴァ", "ヴィ", "ヴェ", "ヴォ", "グァ"  
	, "ジェ", "シェ", "チェ", "ティ", "ディ"  
	, "ツェ", "ファ", "フィ", "フェ", "フォ"  
	
	, "タクシー", "ウーロン", "ホテル", "ソース", "エアコン"
	, "ドア", "スーツ", "ノート", "コンピューター"

	,
	
	"アイス", "インスタント", "ウール", "エンジン", "オレンジ", "カメラ"
	, "キー", "クーラー", "レーボー", "カレンダー", "ラジオ"
	, "テレビ", "スポーツカー", "アパート"
	
	, "ノート", "カーテン"
	, "ジュース", "ラーメン", "セーター", "スカート", "アイスクリーム", "ケーキ"
	, "コップ", "サンドイッチ", "ワイシャツ", "チョコレート"
	, "ポケット", "ニュース", "ジャーナリスト", "キャッシュ・カード"

	, "アニメ", "マスク", "チーム", "クレヨン", "リモコン"
	, "ガム", "ズボン", "ボール", "ゲーム", "ゴルフ"
	, "ボタン", "チャンネル", "ジーンズ", "ニューヨーク", "ヨーグルト"
	, "ヨーロッパ", "パイロット", "ロッカー"]


# for many time

#random get data

#input to "text"
for i in range(0, len(katakana)-1):
    la_ja = driver.find_element_by_id("sugg-item-ja")
    la_ja.click()
    word = driver.find_element_by_name("text") ##輸入要翻譯的
    word.send_keys(katakana[random.randint(0, len(katakana))]);
    #word.send_keys(katakana[i]);
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    time.sleep(1)
    element = driver.find_element_by_id("gt-src-listen")
    element.click()
    for i in range(0,3):
        a = input("input a to listen again:")
        if a == "a":
            element.click()
            a = " "
        else:
            break


    clear = driver.find_element_by_id("gt-clear")
    clear.click()
    
#ActionChain for input


#clean
close()
quit()
#goto for
