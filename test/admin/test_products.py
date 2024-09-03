import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_login import TestLogin

class TestProducts(TestLogin):

    def test_click_on_product(self, driver):
        # Wait for the 'Catalog' menu item to be visible and click it
        catalog_menu = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[text()='Catalog']"))
        )
        catalog_menu.click()

        # Wait for the 'Products' menu item to be visible and click it
        products_menu = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[contains(@href, '/admin/products') and contains(., 'Products')]"))
        )
        products_menu.click()

        # Verify that the 'Products' page is loaded by checking for the presence of the page title
        page_heading = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h1[text()='Products']"))
        )
        assert page_heading.is_displayed(), "Products page did not load correctly"
