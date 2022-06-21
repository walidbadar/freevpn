# coding=utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
import requests, urllib.request, tempfile, os, time

# TEMP_FILE = tempfile.NamedTemporaryFile(mode='r+', suffix='.png').name
# URL = 'https://www.vpnbook.com/password.php'
# IMAGE_DATA = requests.get(URL).content
# print(IMAGE_DATA)
# with open(TEMP_FILE, 'wb') as file: file.write(IMAGE_DATA)
# pswdImg = Image.open(TEMP_FILE)
# pswdImg = pswdImg.resize((100, 20))
# pswd = pytesseract.image_to_string(pswdImg, config='--psm 6')
# print(pswd)

vpnPswd = "https://raw.githubusercontent.com/walidbadar/freevpn/master/vpnPswd.txt"
# open('/etc/openvpn/password.txt', 'wb').write(urllib.request.urlopen(vpnPswd).read())

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get(vpnPswd)
pswd = WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.XPATH, '/html/body/pre'))).text
print(pswd)
driver.quit()
open('/etc/openvpn/password.txt', 'w').write(pswd)

vpn = 'https://www.vpnbook.com/free-openvpn-account/VPNBook.com-OpenVPN-US1.zip'
open("/etc/openvpn/openvpn.zip", "wb").write(requests.get(vpn).content)
os.system("sudo unzip -o /etc/openvpn/openvpn.zip -d /etc/openvpn")

vpnSetting = open("/etc/openvpn/vpnbook-us1-udp53.ovpn", "r")
replacement = ""
for line in vpnSetting:
    line = line.strip()
    changes = line.replace("auth-user-pass", "auth-user-pass /etc/openvpn/password.txt")
    replacement = replacement + changes + "\n"
vpnSetting.close()
vpnSetting = open("/etc/openvpn/vpnbook-us1-udp53.ovpn", "w")
vpnSetting.write(replacement)
vpnSetting.close()
