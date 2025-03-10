from selenium import webdriver

# Démarrer le WebDriver (par exemple, Chrome)
driver = webdriver.Chrome()
url ="https://www.decathlon.fr"
# Ouvrir une URL (par exemple, Google)
driver.get(url)
print(driver.get(url))
# Maximiser la fenêtre du navigateur
driver.maximize_window()

# Récupérer le titre de la page
assert driver.title == 'DECATHLON | Magasin de Sport'

# Vérifier si l'URL de lap age est correcte
print("URL actuelle :", driver.current_url)
assert driver.current_url == "https://www.decathlon.fr/"

driver.quit()