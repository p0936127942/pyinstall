import os

def menu():

    print(""" 
全自動安裝環境 By 孫孫
1. py3
2. PY2
""")

loop = True

while loop:
    menu()
    what = input("請輸入您所需要的選項@:")
    if what == "1":
        print("========================================")
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y python3")
        os.system("pkg install -y nodejs-current")
        os.system("pkg install -y nodejs-current-dev")
        os.system("pkg install -y coreutils")
        os.system("pkg install -y ruby")
        os.system("python3 -m pip install --upgrade pip")
        os.system("pip3 install rsa")
        os.system("pip3 install thrift")
        os.system("pip3 install requests")
        os.system("pip3 install linepy")
        os.system("pip3 install bs4")
        os.system("pip3 install gtts")
        os.system("pip3 install beautifulsoup")
        os.system("pip3 install html5lib")
        os.system("pip3 install wikipedia")
        os.system("pip3 install pytz")
        os.system("pip3 install goslate")
        os.system("pip3 install googletrans")
        os.system("pip3 install akad")		
        os.system("pip3 install thrift==0.11.0")		
        print("基楚PY3環境已安裝完成 :)")
        print("========================================")
        rmenu = input("是否返回主選單 (y/n): ")
        if rmenu == "y":
            menu()
    if what == "2":
        print("========================================")
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y python3")
        os.system("pkg install -y nodejs-current")
        os.system("pkg install -y nodejs-current-dev")
        os.system("pkg install -y coreutils")
        os.system("pkg install -y ruby")
        os.system("python2 -m pip install --upgrade pip")
        os.system("pip2 install rsa")
        os.system("pip2 install thrift")
        os.system("pip2 install requests")
        os.system("pip2 install linepy")
        os.system("pip2 install bs4")
        os.system("pip2 install gtts")
        os.system("pip2 install beautifulsoup")
        os.system("pip2 install html5lib")
        os.system("pip2 install wikipedia")
        os.system("pip2 install pytz")
        os.system("pip2 install goslate")
        os.system("pip2 install googletrans")
        os.system("pip2 install akad")			
        print("基楚PY2環境已安裝完成 :)")
        print("========================================")
        rmenu = input("是否返回主選單 (y/n): ")
        if rmenu == "y":
            menu()			
        else:
            break
