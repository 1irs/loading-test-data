import unittest
from selenium.webdriver.common.by import By

from address_data import addresses_from_csv
from page_object.address_page import AddressPage
from webdriver_factory import WebDriverFactory


class FillAddressTest(unittest.TestCase):

    driver = None
    address_page = None

    @classmethod
    def setUpClass(cls) -> None:
        """Предустановка. Выполняется один раз перед всеми тестами."""
        cls.driver = WebDriverFactory.get_driver()

        # Предусловие: открыта страница поиска.
        cls.address_page = AddressPage(cls.driver)

    def setUp(self) -> None:
        self.address_page = FillAddressTest.address_page
        self.driver = FillAddressTest.driver

    @classmethod
    def tearDownClass(cls) -> None:
        """Выполняется один раз после всех тестов"""
        cls.driver.quit()

    def tearDown(self) -> None:
        self.driver.save_screenshot('test-reports/' + self.id() + '.png')

    def test(self):
        email = 'test+26052022@example.com'
        password = '8nDv69GkQwLbzev'
        self.driver.get('http://tutorialsninja.com/demo/index.php?route=account/login')
        self.driver.find_element(By.NAME, 'email').send_keys(email)
        self.driver.find_element(By.NAME, 'password').send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, '[value=Login]').click()

        for address in addresses_from_csv():
            self.address_page.open()
            self.address_page.fill_form(address)

        self.driver.quit()
