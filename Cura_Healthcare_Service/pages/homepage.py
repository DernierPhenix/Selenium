from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class HomePage:
    def __init__(self, driver, wait):
        
        # | ENVIRONNEMENT
        # |
        # v Ici, on met le driver et le wait

        self.driver = driver
        self.wait = wait

        # | LOCATORS
        # |
        # v Ici, vous pouvez mettre les locators

        self.bouton_appointment = (By.LINK_TEXT, "Sign In")
        self.welcome_message = (By.ID, "WelcomeContent")


    # | FONCTIONS
    # | Ici, vous pouvez définir les fonctions pour interagir avec les éléments,
    # v et effectuer des actions utilisateurs

    def verifier_titre_homepage(self):
       assert self.driver.title == 'CURA Healthcare Service' # Vérification du titre de la page


    def cliquer_bouton_appointment(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#btn-make-appointment'))).click()  # 02. Cliquer sur « Make an appointment »

