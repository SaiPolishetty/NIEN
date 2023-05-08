import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select



import pytest


class TestItemDashboard:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://ec2-52-14-64-70.us-east-2.compute.amazonaws.com/login")
    driver.maximize_window()

    def testAdminLogin(self):
        username = self.driver.find_element(By.XPATH, "//input[contains(@placeholder, 'Enter Email Address')]")
        username.send_keys("nien.verify01@gmail.com")
        password = self.driver.find_element(By.XPATH, "//input[contains(@placeholder, 'Enter Password')]")
        password.send_keys("Techgrit123")
        loginbutton = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]")
        loginbutton.click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.url_contains('admin'))
        adminurl = self.driver.current_url
        assert adminurl == "http://ec2-52-14-64-70.us-east-2.compute.amazonaws.com/admin"

    def testItemDashboardTitle(self):
        dashboard = self.driver.find_element(By.XPATH, "//a[contains(@href, '/admin/product/transcation')]")
        self.driver.execute_script("arguments[0].click();", dashboard)
        dashboardtitle = self.driver.find_element(By.XPATH, "//span[contains(text(), 'Item Dashboard')]")
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Item Dashboard')]")))
        print("Current Dashboard Title is " + dashboardtitle.text)
        assert dashboardtitle.text == "Item Dashboard"

    def testShowEntries(self):
        time.sleep(10)
        showentries = Select(self.driver.find_element(By.XPATH, "//select[@name = 'pageSize']"))
        current_value = showentries.first_selected_option.get_attribute("value")
        print("Current Show Entries Selected  = " + current_value)

    def testProductCount(self):
        entries = self.driver.find_element(By.XPATH, "//span[@class = 'show-grid-total-count']")
        entriescount = entries.text
        ecount = entriescount.split("of")
        print("Total Records = " + ecount[1].strip())

    def testPages(self):
        pages = self.driver.find_element(By.XPATH, "//ul[@class = 'pagination']")
        from_page = pages.find_elements(By.TAG_NAME, "li")[1]
        to_page = pages.find_elements(By.TAG_NAME, "li")[3]
        print("From " + from_page.text + "to " + to_page.text)










