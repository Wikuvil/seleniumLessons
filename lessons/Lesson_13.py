from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
import math

link = 'http://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get(link)
    WebDriverWait(browser, 12).until(
        ec.text_to_be_present_in_element((By.ID, "price"), '$100'))
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    func = calc(x)
    input_answer = browser.find_element(By.ID, 'answer')
    input_answer.send_keys(func)
    button2 = browser.find_element(By.ID, "solve")
    button2.click()
    print(browser.switch_to.alert.text.split(': ')[-1])
finally:
    browser.quit()
