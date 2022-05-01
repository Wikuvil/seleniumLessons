from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/registration1.html"
try:
    browser.get(link)
    # Тут идет заполнение полей из первого блока, который хранил в себе обязательные поля,
    # но это решение не подошло для следующего задания, где просто исчезло поле из блока
    # elements = browser.find_elements(By.CSS_SELECTOR, ".first_block .form-control")
    # for element in elements:
    #     element.send_keys("Answer")
    browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys("Ivan")
    # Поле Last name отсутствует, поэтому возникает ошибка NoSuchElementException
    browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys("Petrov")
    browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys("12345678910")
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(2)
    browser.quit()
