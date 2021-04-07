from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from os import getcwd


options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options, executable_path=r'C:\chromedriver/chromedriver.exe')

driver.get('http://google.com') #접속할 url

driver.implicitly_wait(15) #맹목적 대기
driver.find_element_by_css_selector('.gb_4.gb_5.gb_ae.gb_4c').click()
driver.implicitly_wait(15) #맹목적 대기
driver.find_element_by_css_selector('.whsOnd.zHQkBf').click()
driver.implicitly_wait(15) #맹목적 대기
driver.find_element_by_css_selector('.whsOnd.zHQkBf').send_keys('0131202020620@onedu.jje.go.kr')
driver.implicitly_wait(15) #맹목적 대기
driver.find_element_by_css_selector('.VfPpkd-RLmnJb').click()
driver.implicitly_wait(15) #맹목적 대기
driver.find_element_by_css_selector('.whsOnd.zHQkBf').send_keys('epdrm645@@'epdrm645@@'epdrm645@@'epdrm645@@'epdrm645@@'epdrm645@@'epdrm645@@'epdrm645@@'epdrm645@@'epdrm645@@'epdrm645@@'epdrm645@@'epdrm645@@'epdrm645@@'epdrm645@@'epdrm645@@'epdrm645@@'epdrm645@@'epdrm645@@'epdrm645@@'epdrm645@@')
driver.implicitly_wait(15) #맹목적 대기
driver.find_element_by_css_selector('.VfPpkd-RLmnJb').click()
