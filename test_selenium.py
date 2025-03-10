from selenium import webdriver

# on instancie le driver d'un navigateur en utilisant la commande suivante
# driver = webdriver.NAVIGATEUR() "Navigateur = votre navigateur"


driver = webdriver.Chrome()

# Définir une variable options
options =webdriver.ChromeOptions()

# Garder le navigateur ouvert après exécution
options.add_experimental_option("detach", True)

# Lancer le navigateur Chrome
driver = webdriver.Chrome(options)

# la navigation
# Permet de naviguer vers une URL
driver = driver.get("https://www.free.fr")

# Permet d'aller à la page suivante
# driver = driver.forward()

# Permet d'aller à la page précédente
# driver = driver.back()

# Permet de rafraichir la page suivante
# driver = driver.refresh()

# Renvoie le titre de la page affichée
driver = driver.title

# Renvoie l'URL de la page affichée
driver = driver.current_url


html_content = driver.page_source
