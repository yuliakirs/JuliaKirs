from selenium import webdriver
import time


link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"



def welcome_text1(link1):
    browser = webdriver.Chrome()
    browser.get(link1)
    # Ваш код, который заполняет обязательные поля
    name = browser.find_element_by_css_selector('.first_block .first')
    name.send_keys("Мое имя")
    first_name = browser.find_element_by_css_selector('.first_block .second')
    first_name.send_keys("Моя фамилия")
    email = browser.find_element_by_css_selector('.first_block .third')
    email.send_keys("Моя почта")
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
    browser.quit()

def welcome_text2(link2):
    browser = webdriver.Chrome()
    browser.get(link2)
    # Ваш код, который заполняет обязательные поля
    name = browser.find_element_by_css_selector('.first_block .first')
    name.send_keys("Мое имя")
    first_name = browser.find_element_by_css_selector('.first_block .second')
    first_name.send_keys("Моя фамилия")
    email = browser.find_element_by_css_selector('.first_block .third')
    email.send_keys("Моя почта")
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
    browser.quit()

welcome_text1(link1)
welcome_text2(link2)

