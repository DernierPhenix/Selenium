from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# À partir de l'exercice 2 mettre en place un implicite wait 
# Wait implicit agit sur tous les éléments du code
"""
Définir des options pour le driver. Pour chrome, garder
le navigateur ouvert si driver.quit() n'est pas appelée
"""
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

#  Instancier le navigateur Chrome avec les options
driver = webdriver.Chrome(options)
wait = WebDriverWait(driver, 10)

# Ouvrir en plein écran
driver.maximize_window()

# Naviguer vers le site de décathlon
driver.get("https://www.decathlon.fr/")

# Vérifier que le titre de la page est correct
assert driver.title == 'DECATHLON | Magasin de Sport', "Le titre devrait être 'DECATHLON | Magasin de Sport'"

# Continuer sans accepter les cookies
try:
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'didomi-continue-without-agreeing'))).click()
    # driver.find_element(By.CLASS_NAME, 'didomi-continue-without-agreeing').click()
except NoSuchElementException:
    print("Cookies pop-up is not present")

# Récupérer le champ de recherche en utilisant le xpath
search_box = driver.find_element(By.XPATH, "//input[@type='search']")

# Ecrire Vélo dans le champ de recherche et simuler le bouton Entrée
search_box.clear()
search_box.send_keys("ballon de football")
search_box.send_keys(Keys.RETURN)

# Vérifier que nous sommes sur la page des vélos
# resultatRecherche = driver.find_element(By.TAG_NAME, 'h1').text
resultatRecherche = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'h1'))).text
assert resultatRecherche == "Ballons de football"

#  Vérifier qu'il y a au moins un produit affiché
product_list = driver.find_element(By.CLASS_NAME, 'product-list')
assert product_list.is_displayed(), "Products should be visible"

# Fermer le navigateur
driver.quit()