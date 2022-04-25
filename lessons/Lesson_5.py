from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Тут идет заполнение полей из первого блока, который хранил в себе обязательные поля,
    # но это решение не подошло для следующего задания, где просто исчезло поле из блока
    # elements = browser.find_elements(By.CSS_SELECTOR, ".first_block .form-control")
    # for element in elements:
    #     element.send_keys("Answer")
    input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
    input1.send_keys("Ivan")
    # Поле Last name отсутствует, поэтому возникает ошибка NoSuchElementException
    input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
    input3.send_keys("12345678910")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(2)
    browser.quit()
