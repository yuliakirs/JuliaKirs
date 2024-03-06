from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

link="https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

x_find=browser.find_element(by='id', value='num1')
x=x_find.text
y_find=browser.find_element(by='id', value='num2')
y=y_find.text
num1 = int(x)
num2 = int(y)
sum_el = num1 + num2

select = Select(browser.find_element(by='tag name', value="select"))
select.select_by_value(str(sum_el)) 

button = browser.find_element(by='css selector', value="button.btn")
button.click()
