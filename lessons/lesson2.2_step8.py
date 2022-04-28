from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'lesson2.2_step8.txt')
try:
    browser.get(link)
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("test@email.dot")
    input_file = browser.find_element(By.ID, "file")
    input_file.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(4)
    browser.quit()
