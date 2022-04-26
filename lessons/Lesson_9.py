from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get(link)
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    func = calc(x)
    print(func)
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(func)
    option1 = browser.find_element(By.CSS_SELECTOR, '[for = "robotCheckbox"]')
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, '[for = "robotsRule"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", option2)
    option2.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(3)
    browser.quit()
