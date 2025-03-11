import pytest
from selenium import webdriver

# Fixture pour initialiser le WebDriver
@pytest.fixture
def driver():
    #initialisation du WebDriver (Ouvre Chrome)
    driver = webdriver.Chrome()

    #indique à pytest que le driver est prêta être utilisé par les tests
    yield driver    #Le yield fait en sorte que la fixture "retourne" le WebDriver aux tests

    # Ce code sera exécuté après le test, pour ne ttoyer et fermer le navigateur
    driver.quit()   #Fermeture du navigateur après le test.