import time
time.sleep(120)
import datetime 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os
from plyer import notification

def messanger():
    try:
        url ="https://web.whatsapp.com/send?phone=+91xxxxxxxxxx"

        message_content = "Good morning!"
        path = r"D:\All_code\chrome_driver\chromedriver.exe"


        options = webdriver.ChromeOptions()
        options.add_argument("user-data-dir=C:\\Users\\srk\\AppData\\Local\\Google\\Chrome\\User Data")

        
        driver = webdriver.Chrome(executable_path=path, options=options)
        driver.minimize_window()
        driver.get(url)
        time.sleep(20)

        type_it = driver.find_elements_by_class_name('_13NKt')
        time.sleep(20)
        try:
            type_it[1].send_keys(message_content + Keys.ENTER)
        except IndexError as e:
            type_it = driver.find_elements_by_class_name('_13NKt')
            type_it[1].send_keys(message_content + Keys.ENTER)
            print(e)

        time.sleep(10)

        driver.quit()
    except Exception as e:
        notification.notify(
            title = "Whatsapp message not sent",
            message = "Error while sending!",
    	    app_icon = r"D:\All_code\srk_pyt\python_whatsaap\8cAbMBAMi.ico",
            app_name = "Whatsapp Message error",
            toast = True,
 	    )
        print(e)
        os._exit(0)



today = str(datetime.date.today())
today_2 = f"{today} "
content = bytes(today_2,'utf-8')

year_str = str(datetime.datetime.now().year)#.decode('utf-8') can do like b'xyz' but this is optimized
year_edit = bytes(year_str,'utf-8').decode('utf-8')

date_str = str(datetime.datetime.now().day)
date_edit = bytes(date_str,'utf-8').decode('utf-8')
edit = {"1":"01",
        "2":"02",
        "2":"03",
        "4":"04",
        "5":"05",
        "6":"06",
        "7":"07",
        "8":"08",
        "9":"09",}
print(date_edit)
try:
    file = open("database.txt", "x")
    messanger()
    file.write(today_2)
    file.close()
except Exception as e:
##    file = open()
    file = open("database.txt", "a+b")
##    print(file.tell(),"j")
##    file.read()
    try:
        try:
            file.seek(-11,2) # seek will not work in negative in text mode, only in byte mode
##           print(file.tell())
        except OSError as e:
            print(e)
            messanger()
            file.write(content)
            file.close()
            os._exit(0)
        year = file.read(10).decode('utf-8')
        file.seek(-11,2)
        date = file.read(10).decode('utf-8')


        if year_edit != year[:4]:
            file.close()
            file = open("database.txt", "wb")
            file.close()
            file = open("database.txt", "a+b")
            messanger()
            file.write(content)
            file.close()
        for x in edit.keys():
            if x == date_edit:
                date_edit = edit.get(x)
                break
        
        if date_edit != date[8:14]:
            messanger()
            file.write(content)
            file.close()
            os._exit(0)


    except Exception as e:
        print(e)


