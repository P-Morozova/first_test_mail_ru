from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyautogui
from selenium import webdriver


class MainPage:
    def __init__(self, email):
        self.email = email

    def send_letter(self, driver, letter_theme, letter_text):

        post_button = WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Почта')]")))
        post_button.click()
        send_letter_button = WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.XPATH, "//body/div[@id=\"app-canvas\"]//a[@href=\"/compose/\"]")))
        send_letter_button.click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//body//input[1]"))).send_keys(
            self.email)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.NAME, "Subject"))).send_keys(
            letter_theme + Keys.TAB + Keys.TAB + letter_text)

        driver.find_element(By.XPATH, "//span[contains(text(),'Отправить')]").click()

    def exit_from_account(self, driver):
        driver.find_element(By.XPATH, "//body/div[@id='headline']/div[@id='ph-whiteline']//span[2]").click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Выйти')]"))).click()

    def check_letter_receive(self, driver):

        received_letter_sender = WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.XPATH, "//body/div[@id='app-canvas']/div[1]/div[1]/div[1]/div[1]/div[2]/span[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/div[4]/div[1]/div[1]/span[1]"))).get_attribute("title")

        received_letter_theme = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(
            (By.XPATH, "//body/div[@id='app-canvas']/div[1]/div[1]/div[1]/div[1]/div[2]/span[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/div[4]/div[1]/div[4]/span[1]/div[1]/span[1]"))).text

        idx1 = received_letter_sender.find('<')
        idx2 = received_letter_sender.find('>')
        received_letter_sender_email = received_letter_sender[idx1 + 1:idx2]

        return received_letter_sender_email, received_letter_theme
           # driver.find_element(By.XPATH, "//body/div[@id='app-canvas']//div[@class=\"letter-list__react\"]//a[1]//span[4]")


