from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com/")

input("Press anything after QR scan")
time.sleep(5)
print("loged in")

# add names of contact that are saved in your phone as it is. in the list
names = ["name_of_contact"]

for name in names:

    person = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    person.click()
    
    # n = number os messages to be send...
    n = 10000
    for i in range(0,n):
        reply = driver.find_element_by_class_name("_3u328.copyable-text.selectable-text")
        reply.clear()
        # message to be send. 
        reply.send_keys("Hi there...")
        reply.send_keys(Keys.RETURN)
        print(i)
