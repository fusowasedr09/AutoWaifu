#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import os.path
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
import uuid, os

Target =  "https://waifulabs.com/" # 指定URL
Driver_path = "chromedriver.exe"   # chromedriverの場所。windows,プログラムと同じ場所にある場合
Interval = 3 # 遅延時間設定（あまり短くしないこと）

# 動作回数の入力
kaisu = input("何回繰り返す？（半角数字）")
kaisu = int(kaisu)

# 保存フォルダの存在確認
if not os.path.exists("auto_outputs"):
    os.mkdir("auto_outputs")
driver = webdriver.Chrome(executable_path=Driver_path)

# 初回のみの動作
def Start():
        driver.get(Target)
        driver.find_element_by_xpath("//*[contains(text(), 'Meet your dream waifu')]").click()
        time.sleep(Interval)
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

def main():
    # 本命の操作
    for j in range(4):
        driver.find_element_by_class_name("girl").click()
        time.sleep(Interval)
    # 直接保存
    url = driver.find_element_by_xpath("//img[@class='my-girl-image my-girl-loaded']").get_attribute("src")
    urllib.request.urlretrieve(url, "./auto_outputs/Waifu_"+ str(uuid.uuid4()) + ".png")
    driver.find_element_by_xpath("//*[contains(text(), 'Restart from the beginning')]").click()
    time.sleep(Interval)

if __name__ =="__main__":
    Start()
    for i in range(kaisu):
        main()
    driver.quit()
