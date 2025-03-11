from selenium import webdriver
from selenium.webdriver.common.by import By
 
 
"""
Définir des options pour le driver. Pour chrome, garder
le navigateur ouvert si driver.quit() n'est pas appelée
"""
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
 
#  Instancier le navigateur Chrome avec les options
driver = webdriver.Chrome(options)
 
# Ouvrir en plein écran
driver.maximize_window()
 
# Naviguer vers le site de décathlon
driver.get("https://www.decathlon.fr/")
 
# Vérifier que le titre de la page est correct
assert driver.title == 'DECATHLON | Magasin de Sport'
 
# Vérifier que le titre de la page est correct
assert driver.current_url == 'https://www.decathlon.fr/'

# Localisation par la balise
driver.find_element(By.TAG_NAME, "h1")

# Localisation par texte
driver.find_element(By.LINK_TEXT, "Retour page accueil")

# Localisation par texte partiel
driver.find_element(By.PARTIAL_LINK_TEXT, "page accueil")

# Localisation par Xpath
driver.find_element(By.XPATH, "//p[text()='Text pour Xpath']")

# Localosation par CSS Selector
driver.find_element(By.CSS_SELECTOR, "btn-css")
 
# Fermer le navigateur
driver.quit()
 