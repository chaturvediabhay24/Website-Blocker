import time
from datetime import datetime as dt
host_temp="hosts.txt"
host_path=r"C:\Windows\System32\drivers\etc\hosts"         #path of your host.txt file
redirect="127.0.0.1"
website_list=["www.yahoo.com","www.facebook.com","yahoo.com","facebook.com"]        #list of websites to be blocked

while True:
    if(dt(dt.now().year,dt.now().month,dt.now().day,8)<dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,20) ):
        print("working hours...")
        with open(host_temp,'r+') as file:
            content=file.read()
            print(content)
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
        
    else:
        print("fun hours..")
        
        with open(host_temp,'r+') as file:
            file.seek(0)
            content=file.readlines()
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(5)
