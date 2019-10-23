from selenium import webdriver
import random
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os

user_data_dir = os.environ['CHROME_USER_DATA']
driver_path = os.environ['CHROME_DRIVER_PATH']

def openweb():
    dri_Opt = webdriver.ChromeOptions()
    dri_Opt.add_extension('Keyboard-Shortcuts-for-Google-Translate_v2.4.4.0.crx')
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    dri_Opt.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome(driver_path, 0, dri_Opt)
    driver.get("https://translate.google.com.tw/#view=home&op=translate&sl=ja&tl=zh-TW")
    return driver

def inputdata():
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
    return katakana

def speak(driver, data, again, sleep_time):
    #la_ja = driver.find_element_by_id("sugg-item-ja")
    #la_ja.click()
    #ActionChains(driver).key_down(Keys.LEFT_CONTROL).send_keys('4').perform()
    #ActionChains(driver).key_up(Keys.LEFT_CONTROL).perform()
    
    word = driver.find_element_by_id("source") ##輸入要翻譯的
    #word.clear()
    ActionChains(driver).key_down(Keys.LEFT_CONTROL).send_keys('d').perform()
    ActionChains(driver).key_up(Keys.LEFT_CONTROL).perform()

    word.send_keys(data)

    #word.send_keys(katakana[i]);
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    time.sleep(1)
    #element = driver.find_element_by_id("btnPlay")
    #element.click()
    ActionChains(driver).key_down(Keys.LEFT_CONTROL).key_down(Keys.SHIFT).send_keys('l').perform()
    ActionChains(driver).key_up(Keys.LEFT_CONTROL).key_up(Keys.SHIFT).perform()

    time.sleep(sleep_time)

    if again:
        for i in range(0,3):
            a = input("input a to listen again:")
            if a == "a":
                ActionChains(driver).key_down(Keys.LEFT_CONTROL).key_down(Keys.SHIFT).send_keys('l').perform()
                ActionChains(driver).key_up(Keys.LEFT_CONTROL).key_up(Keys.SHIFT).perform()

                a = " "
            else:
                break

if __name__ == '__main__':
    driver = openweb()
    data = inputdata()
    for i in range(0, len(data)-1):
        data_to_speak = data[random.randint(0, len(data))]
        speak(driver, data_to_speak, True, 1)

#ActionChain for input


#clean
#close()
#quit()
#goto for
