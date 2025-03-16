from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class AppointmentPage:
    def __init__(self, driver, wait):
        
        # | ENVIRONNEMENT
        # |
        # v Ici, on met le driver et le wait

        self.driver = driver
        self.wait = wait

        # | LOCATORS
        # |
        # v Ici, vous pouvez mettre les locators

        self.facility_combo = (By.CSS_SELECTOR, '#combo_facility')
        self.readmission = (By.NAME, 'hospital_readmission')
        self.program_medicare = (By.ID, "radio_program_medicare")
        self.program_medicaid = (By.ID, "radio_program_medicaid")
        self.program_none = (By.ID, "radio_program_none")
        self.date_input = (By.CSS_SELECTOR, '[placeholder="dd/mm/yyyy"]')
        self.comment_input = (By.CSS_SELECTOR, '[placeholder="Comment"]')
        self.book_button = (By.ID, "btn-book-appointment")
        self.confirmation_message = (By.TAG_NAME, "h2")


    # | FONCTIONS
    # | Ici, vous pouvez définir les fonctions pour interagir avec les éléments,
    # v et effectuer des actions utilisateurs
    def facility_choice(self):
     # 04. Choisir une « Facility ». J’aimerais avoir une fonction qui permet de choisir la facility en fonction de la valeur qu’on lui donne.
        facility_select = Select(self.wait.until(EC.element_to_be_clickable(self.facility_combo)))
        assert facility_select.first_selected_option.text == 'Tokyo CURA Healthcare Center' # Vérifie que le 1er élément de la liste est bien 'Tokyo...'

        facility_select.select_by_value('Seoul CURA Healthcare Center') #Sélectionne l'élément 'Combo facility' stocké dans la variable et va choisir le choix 'Seoul...'
        assert facility_select.first_selected_option.text == 'Seoul CURA Healthcare Center' # Vérifie que le 1er élément de la liste est bien 'Tokyo...'

    def apply_readmission(self):
    # 05. Cocher la case « Apply for hospital readmission » et vérifier qu’elle est cochée
        selected_check = self.wait.until(EC.element_to_be_clickable(self.readmission)) # Stocke l'élement 'Hospital...' dans la variable
        assert selected_check.is_selected() == False # Vérifie que la variable sélectionnée est à False
        selected_check.click()                 # On fait l'action de cliquer sur l'élément  
        assert selected_check.is_selected() == True     # Vérifie que la variable sélectionnée est à True


    def choice_healthcare(self):
    # 06. Choisir un « Healthcare program ». J’aimerais avoir une fonction qui permet de choisir le Healthcare program en fonction de la valeur qu’on lui donne.
        selected_medicare = self.wait.until(EC.element_to_be_clickable(self.program_medicare)) # Stocke l'élement 'Hospital...' dans la variable
        selected_medicaid = self.wait.until(EC.element_to_be_clickable(self.program_medicaid)) # Stocke l'élement 'Hospital...' dans la variable
        selected_none = self.wait.until(EC.element_to_be_clickable(self.program_none)) # Stocke l'élement 'Hospital...' dans la variable
    
        # Sélectionner l'option "None"
        if not selected_none.is_selected():
            selected_none.click()
        
        # Vérifier que "None" est bien sélectionné et les autres non
        assert selected_none.is_selected() == True
        assert selected_medicare.is_selected() == False
        assert selected_medicaid.is_selected() == False
            
    def date_appointment(self):
    # 07. Saisir une date
        date = self.wait.until(EC.element_to_be_clickable(self.date_input)) # Stocke l'élement 'Date...' avec le CCS Selector dans la variable
        date.send_keys('31/03/2025')

    def comment(self):
    # 08. Ecrire un commentaire dans le formulaire
        comment = self.wait.until(EC.element_to_be_clickable(self.comment_input)) # Stocke l'élement 'Date...' avec le CCS Selector dans la variable
        comment.clear()
        comment.send_keys('Bonjour, \n Ceci est mon Commentaire')

    def book_appointment(self):
    # 09. Cliquer sur le bouton « Book Appointment »
        self.wait.until(EC.element_to_be_clickable(self.book_button)).click()

    def confirmation_display(self):
    # 10. Vérifier que le message « Appointment Confirmation » est affiché
        self.wait.until(EC.visibility_of_element_located(self.confirmation_message)).is_displayed()
