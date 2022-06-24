import urllib.request, os, subprocess

WANIP = '127.0.0.1'
IPAddr = urllib.request.urlopen('https://ident.me').read().decode('utf8')

if WANIP == IPAddr:
 os.system('sudo pkill qbittorrent')
 print('Closing torrent')
else:
 subprocess.Popen(['sudo -u pi /usr/bin/qbittorrent'], shell=True)
 print('Opening torrent')