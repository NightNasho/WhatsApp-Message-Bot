import time
from selenium import webdriver

print("*"*50 + "\nPython auto WhatsApp Messaging Bot ver 1.0\nMade by N4sh0_N1ghtm4r3"+"\n"+"*"*50)
name = input("[*] Enter the contact name: ")
msg = input("[*] Enter the message: ")
count = int(input("[*] Enter the message count: "))
wait_period = int(input("[*] Enter the cycle size(after n messages): "))
time_delay = int(input("[*] Enter the delay between cycles: "))

print("\n[+] Configuration Gathered")
print("[+] Opening Browser...")

driver = webdriver.Chrome('C:\chromedriver\chromedriver')

driver.get('http://web.whatsapp.com/')

name = 'Diana'
msg = '.'
count = 11000
cycle = 1

input("[*] Enter after scanning the QR")

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

parent_div = driver.find_element_by_class_name('_2AuNk')
msg_box = parent_div.find_element_by_class_name('_1awRl')
#msg_box.send_keys(msg)

#button = driver.find_element_by_class_name('_2Ujuu')
#button.click()

print("[+] Bot Messaging Started."
for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_2Ujuu')
    button.click()
    if (range%wait_period == 0):
        print("[+] Cycle " + cycle + " Completed.")
        print("[*] Paused Execution For Dodge Spam Filters...")
        time.sleep(time_delay)
        cycle += 1
