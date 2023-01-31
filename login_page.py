from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time


class LoginPage:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def do_login(self, driver):

        login_button = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".ph-login")))
        login_button.click()

        iframe = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//body/div[3]/div[1]/iframe[1]")))
        driver.switch_to.frame(iframe)

        login_field = driver.find_element(By.NAME, "username")
        login_field.send_keys(self.login)
        next_button = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, "//div["
                                                                                                 "@id=\"root\"]//button[1]")))
        next_button.click()
        #login_field.send_keys(Keys.ENTER)

        password_field = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.NAME, "password")))
        password_field.send_keys(self.password)
        next_button = WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@id=\"root\"]//div[@class=\"login-row\"]//button[1]")))
        next_button.click()
