from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()
try:
    browser.get(link)
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    func = calc(x)
    input_answer = browser.find_element(By.ID, 'answer')
    input_answer.send_keys(func)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    print(browser.switch_to.alert.text.split(': ')[-1])
    browser.quit()
