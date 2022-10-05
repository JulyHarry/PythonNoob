# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome('../downloads/chromedriver')
browser.get('https://www.baidu.com')

search_input = browser.find_element(By.ID, 'kw')
search_input.send_keys('周杰伦')
time.sleep(2)

submit_button = browser.find_element(By.ID, 'su')
submit_button.click()
time.sleep(2)

js_bottom = 'document.documentElement.scrollTop=100000'
browser.execute_script(js_bottom)
time.sleep(2)

next_button = browser.find_element(By.XPATH, '//a[@class="n"]')
next_button.click()
time.sleep(2)

browser.execute_script(js_bottom)
time.sleep(2)

browser.back()
time.sleep(2)
browser.forward()
time.sleep(2)
browser.quit()
