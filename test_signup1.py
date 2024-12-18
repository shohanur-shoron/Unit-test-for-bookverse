# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestSignup1():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
def test_signup1(self):
    self.driver.get("http://127.0.0.1:8000/accounts/create-account/")
    time.sleep(0.5)
    self.driver.maximize_window()
    time.sleep(0.5)
    self.driver.find_element(By.NAME, "firstname").click()
    time.sleep(0.5)
    self.driver.find_element(By.NAME, "firstname").send_keys("Shohanur")
    time.sleep(0.5)
    self.driver.find_element(By.NAME, "lastname").click()
    time.sleep(0.5)
    self.driver.find_element(By.NAME, "lastname").send_keys("Rahman")
    time.sleep(0.5)
    self.driver.find_element(By.NAME, "phone").click()
    time.sleep(0.5)
    self.driver.find_element(By.NAME, "phone").send_keys("01723077854")
    time.sleep(0.5)
    self.driver.find_element(By.NAME, "email").click()
    time.sleep(0.5)
    self.driver.find_element(By.NAME, "email").send_keys("shorons328@gmail.com")
    time.sleep(0.5)
    self.driver.find_element(By.NAME, "gender").click()
    time.sleep(0.5)
    dropdown = self.driver.find_element(By.NAME, "gender")
    dropdown.find_element(By.XPATH, "//option[. = 'Male']").click()
    time.sleep(0.5)
    self.driver.find_element(By.ID, "passwordFld").click()
    time.sleep(0.5)
    self.driver.find_element(By.ID, "passwordFld").send_keys("1234")
    time.sleep(0.5)
    self.driver.find_element(By.ID, "passwordConfirmFld").click()
    time.sleep(0.5)
    self.driver.find_element(By.ID, "passwordConfirmFld").send_keys("1234")
    time.sleep(0.5)
    self.driver.find_element(By.CSS_SELECTOR, ".submitBtn").click()
    time.sleep(0.5)
    self.driver.find_element(By.CSS_SELECTOR, ".submitBtn").click()
    time.sleep(0.5)
    self.driver.find_element(By.ID, "imageUpload").send_keys("C:\\Users\\User\\Downloads\\tlp_hero_book-cover-adb8a02f82394b605711f8632a44488b.jpg")
    time.sleep(0.5)
    self.driver.find_element(By.CSS_SELECTOR, ".submitBtn").click()
    time.sleep(0.5)
    self.driver.find_element(By.CSS_SELECTOR, ".boxes:nth-child(1)").click()
    time.sleep(0.5)
    self.driver.find_element(By.CSS_SELECTOR, ".boxes:nth-child(3)").click()
    time.sleep(0.5)
    self.driver.find_element(By.CSS_SELECTOR, ".boxes:nth-child(4)").click()
    time.sleep(0.5)
    self.driver.find_element(By.CSS_SELECTOR, ".boxes:nth-child(8)").click()
    time.sleep(0.5)
    self.driver.find_element(By.CSS_SELECTOR, ".boxes:nth-child(10)").click()
    time.sleep(0.5)
    self.driver.find_element(By.CSS_SELECTOR, ".boxes:nth-child(18)").click()
    time.sleep(0.5)
    self.driver.find_element(By.CSS_SELECTOR, ".boxes:nth-child(16)").click()
    time.sleep(0.5)
    self.driver.find_element(By.CSS_SELECTOR, ".boxes:nth-child(15)").click()
    time.sleep(0.5)
    self.driver.find_element(By.CSS_SELECTOR, ".boxes:nth-child(21)").click()
    time.sleep(0.5)
    self.driver.find_element(By.LINK_TEXT, "Let\'s GO!").click()
    time.sleep(0.5)

  
