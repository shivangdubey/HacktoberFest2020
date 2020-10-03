import time
from datetime import datetime as dt


hosts_temp = "hosts"
hosts_path =r"C:\Windows\System32\drivers\\etc\\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com" , "facebook.com"]

while True:
    if dt(dt.now(). year , dt.now().month , dt.now().day , 8) < dt.now() <   dt(dt.now(). year , dt.now().month , dt.now().day ,16):
        print("working hours..")
        with open(hosts_path ,'r+') as file: # r+ read and write 
            content =file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write("\n" +redirect + " " + website+"\n")
    else:
        print("fun hours..")
        with open(hosts_path ,'r+') as file: # r+ read and write 
            content =file.readlines()
            file.seek(0)                      # point the cursor at 0th position
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()               # TRUNCATE METHOD : delete all the content after 0.0.0.1	mssplus.mcafee.com
             
    time.sleep(5)  