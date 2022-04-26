from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# link = "http://suninjuly.github.io/selects1.html"
link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    num1_element = browser.find_element(By.ID, 'num1')
    num1 = num1_element.text
    num2_element = browser.find_element(By.ID, 'num2')
    num2 = num2_element.text
    total = (int(num1)+int(num2))
    print(total)
    browser.find_element(By.CSS_SELECTOR, f'[value = "{total}"]').click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(3)
    browser.quit()
