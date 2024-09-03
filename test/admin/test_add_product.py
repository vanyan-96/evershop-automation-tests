import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_products import TestProducts

class TestAddProduct(TestProducts):

    def test_add_new_product(self, driver):
        # Assurez-vous que vous êtes sur la page des produits
        self.test_click_on_product(driver)
        
        # Cliquer sur le bouton "New Product"
        new_product_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/admin/products/new' and contains(@class, 'button primary')]"))
        )
        new_product_button.click()

        # Vérifier que la page de création de produit est bien chargée
        create_product_heading = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h1[text()='Create A New Product']"))
        )
        assert create_product_heading.is_displayed(), "Create New Product page did not load correctly"

        # Remplir les champs requis pour créer un nouveau produit
        name_input = driver.find_element(By.ID, "name")
        sku_input = driver.find_element(By.ID, "sku")
        price_input = driver.find_element(By.ID, "price")
        weight_input = driver.find_element(By.ID, "weight")
        
        name_input.send_keys("Test Product")
        sku_input.send_keys("TP-12345")
        price_input.send_keys("99.99")
        weight_input.send_keys("1.5")

        # Sélectionner la catégorie du produit
        select_category = driver.find_element(By.XPATH, "//a[text()='Select category']")
        select_category.click()
        # Simuler la sélection de la catégorie, en fonction de l'implémentation du sélecteur
        
        # Sélectionner la classe de taxe
        tax_class_dropdown = driver.find_element(By.ID, "tax_class")
        tax_class_dropdown.click()
        tax_class_option = driver.find_element(By.XPATH, "//option[text()='Taxable Goods']")
        tax_class_option.click()

        # Ajouter une description
        description_input = driver.find_element(By.XPATH, "//textarea[@id='description']")
        description_input.send_keys("This is a test product description.")

        # Soumettre le formulaire
        save_button = driver.find_element(By.XPATH, "//button[contains(@class, 'button primary') and contains(., 'Save')]")
        save_button.click()

        # Vérifier que le produit a été créé avec succès (Cela dépend de la façon dont la page se comporte après la soumission)
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Product created successfully')]"))
        )
        assert success_message.is_displayed(), "Product was not created successfully"
