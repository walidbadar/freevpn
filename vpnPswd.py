# coding=utf-8
from PIL import Image
import pytesseract, requests, tempfile

# TEMP_FILE = tempfile.NamedTemporaryFile(mode='r+', suffix='.png').name
# URL = 'https://www.vpnbook.com/password.php'
# IMAGE_DATA = requests.get(URL).content
# print(IMAGE_DATA)
# with open(TEMP_FILE, 'wb') as file: file.write(IMAGE_DATA)
# pswdImg = Image.open(TEMP_FILE)
# pswdImg = pswdImg.resize((100, 20))
# pswd = pytesseract.image_to_string(pswdImg, config='--psm 6')
# print(pswd)

URL = 'https://raw.githubusercontent.com/walidbadar/freevpn/master/vpnPswd.txt'
open('password.txt', 'wb').write(requests.get(URL).content)

vpn = 'https://www.vpnbook.com/free-openvpn-account/VPNBook.com-OpenVPN-US1.zip'
response = requests.get(vpn)
open("/etc/openvpn/openvpn.zip", "wb").write(response.content)
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
