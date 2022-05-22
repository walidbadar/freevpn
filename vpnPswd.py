# coding=utf-8
from PIL import Image
import pytesseract, requests, tempfile

TEMP_FILE = tempfile.NamedTemporaryFile(mode='r+', suffix='.png').name
URL = 'https://www.vpnbook.com/password.php'
IMAGE_DATA = requests.get(URL).content
with open(TEMP_FILE, 'wb') as file: file.write(IMAGE_DATA)

pswdImg = Image.open(TEMP_FILE)
pswdImg = pswdImg.resize((100, 20))
pswd = pytesseract.image_to_string(pswdImg, config='--psm 6')
print(pswd)
savePswd = open("/etc/openvpn/password.txt", "w")
savePswd.write("vpnbook\n"+pswd)
savePswd.close()

response = requests.get(vpn)
open("/etc/openvpn/openvpn.zip", "wb").write(response.content)
os.system("sudo unzip -o  openvpn.zip")

vpnSetting = open("vpnbook-fr1-udp53.ovpn", "r")
replacement = ""
for line in vpnSetting:
    line = line.strip()
    changes = line.replace("auth-user-pass", "auth-user-pass /etc/openvpn/password.txt")
    replacement = replacement + changes + "\n"
vpnSetting.close()
vpnSetting = open("vpnbook-fr1-udp53.ovpn", "w")
vpnSetting.write(replacement)
vpnSetting.close()