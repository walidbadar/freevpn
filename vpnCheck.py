#!/bin/bash
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
# from webdriver_manager.chrome import ChromeDriverManager
import urllib.request, os, subprocess

options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get('https://ipinfo.io/')
city = str(WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '//*[@id="city-string"]/div/span/span[2]/span'))).text)
print(city)
driver.quit()

# WANIP = '127.0.0.1'
# IPAddr = urllib.request.urlopen('https://ident.me').read().decode('utf8')

if city == 'Jamestown':
 os.system('sudo killall qbittorrent')
 print('Closing torrent')
else:
 subprocess.Popen(['sudo -u pi /usr/bin/qbittorrent'], shell=True)
 print('Opening torrent')
