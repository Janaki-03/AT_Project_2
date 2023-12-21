from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from Data import data
from Locators import locators


class Suman:
    def __init__(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
   
    def login(self):
        try:
            self.driver.maximize_window()
            self.driver.get(data.WebApp_Data().url)
            self.driver.implicitly_wait(10)
            self.driver.find_element(by=By.NAME, value=locators.WebApp_Locators().username_input_box).send_keys(data.WebApp_Data().username)
            self.driver.find_element(by=By.NAME, value=locators.WebApp_Locators().password_input_box).send_keys(data.WebApp_Data().password)
            self.driver.find_element(by=By.XPATH, value=locators.WebApp_Locators().submit_button).click()
            self.driver.find_element(by=By.XPATH, value=locators.WebApp_Locators().admin_button).click()
            admin_button = WebDriverWait(self.driver,10).until(
                EC.presence_of_element_located((By.ID, 'menu_admin_viewAdminModule'))
             )
            admin_button.click()

# Validate title of the page
            assert "OrangeHRM" in self.driver.title, "Title not matching with OrangeHRM"

# Validate options on Admin page
            options_to_validate = ['User Management', 'Job', 'Organization', 'Qualification', 'Nationalities', 'Corporate Banking', 'Configuration']

            for option in options_to_validate:
                option_element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.LINK_TEXT, option))
                )
                assert option_element.is_displayed(), f"Option '{option}' is not displayed on Admin page"

                
        except NoSuchElementException as selenium_error:
            print(selenium_error)
        finally:
            self.driver.quit()


Suman().login()
