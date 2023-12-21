from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from time import sleep 

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# Navigate to the website
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Find the username, password, and login elements
username = driver.find_element(by=By.NAME, value="username").send_keys("Admin")
password = driver.find_element(by=By.NAME, value="password").send_keys("admin123")
login_button = driver.find_element(by=By.XPATH, value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
# Wait for the dashboard page to load
WebDriverWait(driver, 10).until(EC.url_to_be("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard"))

# Navigate to the Admin page
admin_menu = driver.find_element(By.ID, "menu_admin_viewAdminModule")
admin_menu.click()

# Wait for the Admin page to load
WebDriverWait(driver, 10).until(EC.url_to_be("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewAdminModule"))

# Validate the presence of menu items
menu_items = [
    "menu_admin_UserManagement",
    "menu_admin_Job",
    "menu_admin_Organization",
    "menu_admin_Qualifications",
    "menu_admin_Configuration",
    "menu_admin_DisplayOptions",
]

for item in menu_items:
    menu_item = driver.find_element(By.ID, item)
    assert menu_item.is_displayed(), f"{item} is not displayed on the Admin page."

# Close the browser
driver.quit()