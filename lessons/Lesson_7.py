from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = "http://suninjuly.github.io/get_attribute.html"

# Функция для подсчета x
def calc(x):
    # Возвращает значение функции
    return str(math.log(abs(12*math.sin(int(x)))))

try:

    # Обозначает под браузером google chrome
    browser = webdriver.Chrome()
    # Открывает заданную 'link' ссылку
    browser.get(link)
    # Находит элемент на странице по ID 'treasure'
    x_element = browser.find_element(By.ID, 'treasure')
    # Находит значение атрибута 'valuex'
    x_element_checked = x_element.get_attribute("valuex")
    # Переводит найденное значение в переменную 'x'
    x = x_element_checked
    # Обращается к функции 'calc' со значением 'x'
    y = calc(x)
    # Вводит значение 'y' в поле для ответа
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    # Отмечает checkbox 'robotCheckbox'
    option1 = browser.find_element(By.ID, 'robotCheckbox')
    option1.click()
    # Выбирает radiobutton 'robotsRule'
    option2 = browser.find_element(By.ID, 'robotsRule')
    option2.click()
    # Нажимает на кнопку 'Submit' с одним из классов 'btn'
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
