from selenium import webdriver
import time
import math

link="https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
x_element = browser.find_element(by='id', value='input_value')
x = x_element.text
y=(calc(x))

input1 = browser.find_element(by='id',value='answer')
print(input1)
input1.send_keys(y)

option1 = browser.find_element(by='id', value='robotCheckbox')
option1.click()

option2 = browser.find_element(by='id', value='robotsRule')
option2.click()

button = browser.find_element(by='css selector', value="button.btn")
button.click()

