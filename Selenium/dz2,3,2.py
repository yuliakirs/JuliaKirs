from selenium import webdriver
import math

link="http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(by='css selector', value="button.btn")
button.click()

#ДАЕМ ИМЯ ВТОРОЙ ВКЛАДКЕ
new_window = browser.window_handles[1]
#ГОВОРИМ ЧТО НУЖНО ПЕРЕКРЮЧИТЬСЯ НА НОВУЮ ВКЛАДКУ
browser.switch_to.window(new_window)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
x_find = browser.find_element(by='id', value='input_value')
x = x_find.text
y=(calc(x))

input1 = browser.find_element(by='id',value='answer')
print(input1)
input1.send_keys(y)

button = browser.find_element(by='css selector', value="button.btn")
button.click()

