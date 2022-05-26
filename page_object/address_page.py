import os
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from address_data import Address


class AddressPage:

    BASE_URL = os.environ['BASE_URL']
    url = BASE_URL + '/demo/index.php?route=account/address/add'

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)

    def fill_form(self, address: Address):
        d = {
            'firstname': address.first_name,
            'lastname': address.last_name,
            'address_1': address.address_1,
            'city': address.city
        }

        for key, value in d.items():
            el = self.driver.find_element(By.NAME, key)
            el.send_keys(value)

        country_selector = Select(self.driver.find_element(By.NAME, 'country_id'))
        country_selector.select_by_visible_text(address.country)

        # Свое собственное условие по ожиданию.

        def options_is_present(option_value: str):

            def predicate(driver) -> bool:
                elements = driver.find_elements(By.TAG_NAME, 'option')
                is_present = option_value in [element.text for element in elements]
                return is_present

            return predicate

        WebDriverWait(self.driver, timeout=5).until(options_is_present(address.region_state))

        region_state_selector = Select(self.driver.find_element(By.NAME, 'zone_id'))
        region_state_selector.select_by_visible_text(address.region_state)

        continue_button = self.driver.find_element(By.CSS_SELECTOR, '[value=Continue]')
        continue_button.click()
