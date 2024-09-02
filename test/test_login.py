from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

def test_login():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-search-engine-choice-screen")
    driver = webdriver.Chrome(options=options)
    driver.get("http://localhost:3000/admin")
    
    email_input = driver.find_element(By.NAME, "email")
    password_input = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    email_input.send_keys("test@test.fr")
    password_input.send_keys("tesoijdzat")
    login_button.click()

    WebDriverWait(driver, 10).until(EC.title_contains("Dashboard"))
    
    assert "Dashboard" in driver.title
    driver.quit()
