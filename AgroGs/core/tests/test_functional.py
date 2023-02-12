from time import sleep
from django.test import TestCase
from selenium.webdriver.common.by import By
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from AgroGs.users.tests.test_base_functional import UserBaseTest


class CartTest(StaticLiveServerTestCase, TestCase, UserBaseTest):
    
    def test_add_to_cart(self):
        browser = self.make_login()
        browser.execute_script("window.scrollTo(0, 850);")
        sleep(2)
        browser.find_element(By.XPATH, "/html/body/main/section[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[1]/a").click()
        browser.find_element(By.XPATH, "/html/body/main/div/div/div/div[2]/div/div[5]/a").click()
        assert browser.current_url == "http://localhost:8000/cart/"
        browser.quit()

    def test_remove_from_cart(self):
        browser = self.make_login()
        browser.execute_script("window.scrollTo(0, 850);")
        sleep(2)
        browser.find_element(By.XPATH, "/html/body/main/section[2]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[1]/a").click()
        browser.find_element(By.XPATH, "/html/body/main/div/div/div/div[2]/div/div[5]/a").click()
        browser.find_element(By.XPATH, "/html/body/main/section/div/div/div/form/div[1]/table/tbody/tr/td[6]/a").click()
        assert browser.current_url == "http://localhost:8000/cart/"
        browser.quit()