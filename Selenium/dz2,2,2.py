from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

link="https://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
x_find = browser.find_element(by='id', value='input_value')
x = x_find.text
y=(calc(x))

#скроллим вниз
browser.execute_script("window.scrollBy(0, 100);")

#вставляем значение
input1 = browser.find_element(by='id',value='answer')
print(input1)
input1.send_keys(y)

option1 = browser.find_element(by='id', value='robotCheckbox')
option1.click()

option2 = browser.find_element(by='id', value='robotsRule')
option2.click()

button = browser.find_element(by='css selector', value="button.btn")
button.click()
