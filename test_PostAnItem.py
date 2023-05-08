from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://ec2-52-14-64-70.us-east-2.compute.amazonaws.com/login")
driver.maximize_window()


username = driver.find_element(By.XPATH, "//input[contains(@placeholder, 'Enter Email Address')]")
username.send_keys("nien.verify01@gmail.com")
password = driver.find_element(By.XPATH, "//input[contains(@placeholder, 'Enter Password')]")
password.send_keys("Techgrit123")
loginbutton = driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]")
loginbutton.click()

dashboard = driver.find_element(By.XPATH, "//a[contains(@href, '/admin/product/transcation')]")
driver.execute_script("arguments[0].click();", dashboard)
dashboardtitle = driver.find_element(By.XPATH, "//span[contains(text(), 'Item Dashboard')]")
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Item Dashboard')]")))
print("Current Dashboard Title = " + dashboardtitle.text)
assert dashboardtitle.text == "Item Dashboard"


showentries = Select(driver.find_element(By.XPATH, "//select[@name = 'pageSize']"))
current_page = showentries.__getattribute__("Value")
print(current_page)