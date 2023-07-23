import os
import urllib.request
import time

os.remove("1.p12")
os.remove("2.mobileprovision")
os.remove("all.py")
print("РЎС‚Р°СЂС‹Р№ СЃРµСЂС‚С„РёРєР°С‚ СѓРґР°Р»РµРЅ")


time.sleep(10)

urllib.request.urlretrieve("https://raw.githubusercontent.com/dsdasadasdw/111/main/all.py", "all.py")

urllib.request.urlretrieve("https://github.com/dsdasadasdw/111/releases/download/12/1.p12", "1.p12")

urllib.request.urlretrieve("https://github.com/dsdasadasdw/111/releases/download/12/2.mobileprovision", "2.mobileprovision")
print("РќРѕРІС‹Р№ СЃРµСЂС‚РёС„РёРєР°С‚ Р·Р°РіСЂСѓР¶РµРЅ")