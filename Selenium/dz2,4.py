from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

button = browser.find_element(by='css selector', value="button.btn")
# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
button.click()

browser.execute_script("window.scrollBy(0, 500);") 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
x_find = browser.find_element(by='id', value='input_value')
x = x_find.text
y=(calc(x))
  
input1 = browser.find_element(by='id',value='answer')
print(input1)
input1.send_keys(y)

button1 = browser.find_element(by='id', value="solve")
button1.click()



