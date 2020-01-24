#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import os.path
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

Target =  "https://waifulabs.com/" # 指定URL
Driver_path = "chromedriver.exe"   # chromedriverの場所。windows,プログラムと同じ場所にある場合
Interval = 3 # 遅延時間設定（あまり短くしないこと）

kaisu = input("何回繰り返す？（半角数字）")
kaisu = int(kaisu)
driver = webdriver.Chrome(executable_path=Driver_path)

def main():
    driver.get(Target) # URL先に移動
    # ボタン操作
    driver.find_element_by_xpath("//*[contains(text(), 'Meet your dream waifu')]").click()
    time.sleep(Interval)
    # escキー入力（ポップアップ回避）
    webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    # 本命の操作
    for j in range(4):
        driver.find_element_by_class_name("girl").click()
        time.sleep(Interval)
    # 保存ボタン入力
    driver.find_element_by_class_name("download-button").click()
    time.sleep(Interval)
    driver.find_element_by_xpath("//*[contains(text(), 'Restart from the beginning')]").click()

if __name__ =="__main__":
    for i in range(kaisu):
        main()
    driver.quit()
