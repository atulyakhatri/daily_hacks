from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

url ="https://web.whatsapp.com/send?phone=+91xxxxxxxxxx"

message_content = "Sorry!"
path = r"D:\All_code\chrome_driver\chromedriver.exe"


options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\srk\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_argument("--start-maximized")

driver = webdriver.Chrome(executable_path=path, options=options)
driver.get(url)
time.sleep(30)

type_it = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
time.sleep(20)

type_it.send_keys(message_content + Keys.ENTER)

driver.quit()
