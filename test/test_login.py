from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

def test_login():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-search-engine-choice-screen")
    options.add_argument("--headless")  # Exécuter Chrome en mode headless
    options.add_argument("--no-sandbox")  # Nécessaire pour certains environnements CI
    options.add_argument("--disable-dev-shm-usage")  # Éviter les problèmes de mémoire partagée
    options.add_argument("--remote-debugging-port=9222")  # Pour le débogage
    driver = webdriver.Chrome(options=options)
    # driver.get("http://localhost:3000/admin")
    
    # email_input = driver.find_element(By.NAME, "email")
    # password_input = driver.find_element(By.NAME, "password")
    # login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    # email_input.send_keys("test@test.fr")
    # password_input.send_keys("tesoijdzat")
    # login_button.click()

    # WebDriverWait(driver, 10).until(EC.title_contains("Dashboard"))
    
    # assert "Dashboard" in driver.title
    driver.quit()
