from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class LoginPage():
    def __init__(self, driver, wait):
        
        # | ENVIRONNEMENT
        # |
        # v Ici, on met le driver et le wait

        self.driver = driver
        self.wait = wait

        # | LOCATORS
        # |
        # v Ici, vous pouvez mettre les locators

        self.username = (By.CSS_SELECTOR, '#txt-username')
        self.password = (By.CSS_SELECTOR, '#txt-password')
        self.button = (By.CSS_SELECTOR, '#btn-login')


    # | FONCTIONS
    # | Ici, vous pouvez définir les fonctions pour interagir avec les éléments,
    # v et effectuer des actions utilisateurs
   
    def login(self):
    # 03. Se connecter sur le site en tant qu’utilisateur
        self.wait.until(EC.element_to_be_clickable(self.username)).send_keys('John Doe')
        self.wait.until(EC.element_to_be_clickable(self.password)).send_keys('ThisIsNotAPassword')
        self.wait.until(EC.element_to_be_clickable(self.button)).click()