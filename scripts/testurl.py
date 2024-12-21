from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('C:\Python27\Lib\chromedriver.exe')
driver.get('https://team.infogix.com/')
wait(driver, 5).until(EC.alert_is_present())
alert = driver.switch_to_alert()
alert.send_keys('rbmishra')
alert.send_keys(Keys.TAB)
alert.send_keys('345@Password')
alert.accept()

driver.get('http://username:password@example.com')
