# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# chrome_options.binary_location = '../downloads/chromedriver'

browser = webdriver.Chrome('../downloads/chromedriver', chrome_options=chrome_options)

browser.get('https://www.baidu.com')

search_input = browser.find_element(By.ID, 'kw')
search_input.send_keys('周杰伦')

submit_button = browser.find_element(By.ID, 'su')
submit_button.click()

js_bottom = 'document.documentElement.scrollTop=100000'
browser.execute_script(js_bottom)

# next_button = browser.find_element(By.XPATH, '//a[@class="n"]')
# next_button.click()
#
# browser.execute_script(js_bottom)

browser.save_screenshot('../downloads/baidu.png')

print(browser.page_source)
