from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
btn = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
button = browser.find_element_by_id("book")
button.click()

browser.execute_script("return arguments[0].scrollIntoView(true);", button)

x_element = browser.find_element_by_id('input_value')
x = x_element.text

#Посчитать математическую функцию от x
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)

input1 = browser.find_element_by_id('answer')
input1.send_keys(y)

# submit
button = browser.find_element_by_xpath("//button[@type='submit']")
button.click()

time.sleep(30)
browser.quit()
