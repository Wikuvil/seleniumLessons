from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
browser = webdriver.Chrome()


class TestReg(unittest.TestCase):
    def test_reg1(self):
        browser.get('http://suninjuly.github.io/registration1.html')
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys("Ivan")
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys("Petrov")
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys("12345678910")
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Bad")

    def test_reg2(self):
        browser.get('http://suninjuly.github.io/registration2.html')
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys("Ivan")
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys("Petrov")
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys("12345678910")
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Bad")


if __name__ == "__main__":
    unittest.main()


#
# link = "http://suninjuly.github.io/registration1.html"
# browser = webdriver.Chrome()
# browser.get(link)
# input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
# input1.send_keys("Ivan")
# input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
# input2.send_keys("Petrov")
# input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
# input3.send_keys("12345678910")
#
# button = browser.find_element(By.CSS_SELECTOR, "button.btn")
# button.click()
#
# time.sleep(1)
#
# welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
# welcome_text = welcome_text_elt.text
#
# assert "Congratulations! You have successfully registered!" == welcome_text
#
# time.sleep(2)
# browser.quit()
