from pages.homepage import HomePage
from pages.login import LoginPage
from pages.appointment import AppointmentPage

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
 

@pytest.fixture
def driver():

    # Tout ce qui vient avant le yield sera exécuté avant
    # le lancement des tests.

    # Instancier le driver Chrome avec ses options
    browser = webdriver.Chrome()
    
    # 01. Naviguer sur le site de CURA Healthcare Service : https://katalon-demo-cura.herokuapp.com/
    browser.get("https://katalon-demo-cura.herokuapp.com/")

    # Maximiser la fenêtre
    browser.maximize_window()

    yield browser  # Provide the driver to the test

    # Tout ce qui vient après le yield sera exécuté
    # à la fin des tests
    browser.quit()  # Fermeture du navigateur


@pytest.fixture
def wait(driver):
    # Instancier le wait explicit pour le driver
    return WebDriverWait(driver, 10)


def test_healthcare(driver, wait):

   home_page = HomePage(driver, wait)
   login_page = LoginPage(driver, wait)
   appointment_page = AppointmentPage(driver, wait)

   home_page.verifier_titre_homepage()
   home_page.cliquer_bouton_appointment()

   login_page.login()

   appointment_page.choice_healthcare()
   appointment_page.apply_readmission()
   appointment_page.choice_healthcare()
   appointment_page.date_appointment()
   appointment_page.comment()
   appointment_page.book_appointment()
   appointment_page.confirmation_display()
   