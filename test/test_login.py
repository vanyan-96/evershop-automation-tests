import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

def test_login():
    print("Début du test de login")
    
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-search-engine-choice-screen")
    options.add_argument("--headless")  # Exécuter Chrome en mode headless
    options.add_argument("--no-sandbox")  # Nécessaire pour certains environnements CI
    options.add_argument("--disable-dev-shm-usage")  # Éviter les problèmes de mémoire partagée
    options.add_argument("--remote-debugging-port=9222")  # Pour le débogage

    print("Initialisation du WebDriver")
    driver = webdriver.Chrome(options=options)

    try:
        print("Accès à la page de login")
        driver.get("http://localhost:3000/admin")
        
        print("Recherche du champ email")
        email_input = driver.find_element(By.NAME, "email")
        
        print("Recherche du champ mot de passe")
        password_input = driver.find_element(By.NAME, "password")
        
        print("Recherche du bouton de connexion")
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

        print("Envoi des informations de login")
        email_input.send_keys("test@test.fr")
        password_input.send_keys("tesoijdzat")
        
        print("Clique sur le bouton de connexion")
        login_button.click()

        print("Attente du chargement du tableau de bord")
        WebDriverWait(driver, 10).until(EC.title_contains("Dashboard"))
        
        print("Vérification du titre de la page")
        assert "Dashboard" in driver.title

        print("Test réussi")

    except Exception as e:
        print(f"Erreur lors de l'exécution du test : {e}")
    
    finally:
        print("Fermeture du WebDriver")
        driver.quit()
